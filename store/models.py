from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# ==========================================
# 1. PRODUCT CATALOG MODULE
# ==========================================
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"





class Product(models.Model):
    # Change this line in your Product model
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True) 

    image_url = models.URLField(blank=True, null=True)
    stock = models.IntegerField(default=10)
    
    # B2C SEO & Analytics Enhancements
    views_count = models.PositiveIntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    # VISIBILITY TOGGLES
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)      # Shows on Home Page
    is_new_arrival = models.BooleanField(default=True)   # Shows on New Arrivals Page
    show_in_shop = models.BooleanField(default=True)     # Shows on Shop Page
    
    rating = models.FloatField(default=4.5)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.product.name}"

# ==========================================
# 2. CART MODULE
# ==========================================
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return sum(item.get_cost() for item in self.items.all())





class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.product.price * self.quantity









# ==========================================
# 3. ORDER MANAGEMENT MODULE
# ==========================================
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    # B2B Enhancements
    is_po = models.BooleanField(default=False)
    manifest_id = models.CharField(max_length=100, blank=True, null=True)
    freight_status = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"





class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity









# ==========================================
# 4. USER PROFILE MODULE
# ==========================================
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Customer', 'Customer'),
        ('Seller', 'Seller'),
        ('Distributor', 'Distributor'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Customer')
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username






@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
    else:
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()
        else:
            UserProfile.objects.create(user=instance)





class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

# ==========================================
# 5. B2C ADVANCED MODULES (Seller)
# ==========================================
class Coupon(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coupons')
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percent}%)"

class SupportTicket(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_created')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_received')
    subject = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.subject}"


# ==========================================
# 6. B2B ENTERPRISE MODULES (Distributor)
# ==========================================
class Warehouse(models.Model):
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='warehouses')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.location})"

class InventoryBatch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batches')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventory')
    batch_number = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    inward_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Batch {self.batch_number} - {self.product.name}"

class TieredPricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tier_prices')
    min_quantity = models.PositiveIntegerField(default=1000)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (>{self.min_quantity} units @ ${self.discount_price})"

class CreditAccount(models.Model):
    STATUS_CHOICES = (
        ('Good Standing', 'Good Standing'),
        ('Overdue', 'Overdue'),
        ('Suspended', 'Suspended'),
    )
    retailer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_accounts')
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='b2b_clients')
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=50000.00)
    outstanding_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Good Standing')

    def __str__(self):
        return f"{self.retailer.username} Credit with {self.distributor.username}"