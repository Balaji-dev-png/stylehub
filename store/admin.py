from django.contrib import admin
from .models import Category, Product, Order, OrderItem, UserProfile

# --- Category Admin ---
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# --- Product Admin ---
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_available', 'rating', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    list_editable = ['price', 'stock', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

# --- User Profile Admin (New) ---
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'country']
    search_fields = ['user__username', 'user__email', 'phone', 'address']

# --- Order Admin ---
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0  # Removes empty extra rows

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'email', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['id', 'user__username', 'email', 'full_name']
    inlines = [OrderItemInline]
    readonly_fields = ['created_at']