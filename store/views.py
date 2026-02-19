import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Q

# Import all necessary models
from .models import Product, Category, Cart, CartItem, Order, OrderItem, UserProfile, Wishlist

# ==========================================
# 1. CATALOG VIEWS
# ==========================================

def home(request):
    featured = Product.objects.filter(is_available=True)[:9]
    return render(request, 'home.html', {'featured_products': featured})

def new_arrivals(request):
    new_products = Product.objects.filter(is_available=True).order_by('-created_at')[:20]
    return render(request, 'new_arrivals.html', {'products': new_products})

def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    price_max = request.GET.get('price_max')
    if price_max:
        products = products.filter(price__lte=price_max)
        
    context = {'products': products, 'category': category}
    return render(request, 'pro_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'pro_detail.html', {'product': product})

def search_result(request):
    query = request.GET.get('q')
    products = []
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query), 
            is_available=True
        )
    return render(request, 'search_result.html', {'products': products, 'query': query})

# ==========================================
# 2. CART & CHECKOUT MODULE
# ==========================================

@login_required(login_url='auth')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required(login_url='auth')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success', 
            'cart_count': cart.items.count(), 
            'message': f'Added {product.name} to cart'
        })
    return redirect('cart')

@login_required(login_url='auth')
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart')

@login_required(login_url='auth')
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('pro_list')
    return render(request, 'checkout.html', {'cart': cart})

@login_required(login_url='auth')
def place_order(request):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        
        # Create Order
        order = Order.objects.create(
            user=request.user,
            full_name=f"{request.POST.get('first_name')} {request.POST.get('last_name')}",
            email=request.POST.get('email'),
            address=f"{request.POST.get('address')}, {request.POST.get('city')}, {request.POST.get('zip')}",
            city=request.POST.get('city'),
            total_price=cart.get_total()
        )
        
        # Move items from Cart to Order
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order, 
                product=item.product, 
                price=item.product.price, 
                quantity=item.quantity
            )
            # Reduce Stock
            item.product.stock -= item.quantity
            item.product.save()
        
        cart.items.all().delete()
        
        # Simulate Payment Success (75% success rate)
        payment_success = random.choice([True, True, True, False]) 
        if not payment_success:
            order.delete() 
            messages.error(request, 'Payment failed. Please try again.')
            return redirect('checkout')

        # Send Confirmation Email
        try:
            send_mail(
                'Order Confirmed | Stylehub', 
                f'Thank you for your order #{order.id}.\nTotal Amount: ${order.total_price}', 
                settings.EMAIL_HOST_USER, 
                [order.email], 
                fail_silently=True
            )
        except: 
            pass
            
        return render(request, 'success.html', {'order': order})
    return redirect('checkout')

# ==========================================
# 3. USER DASHBOARD & PROFILE
# ==========================================

@login_required(login_url='auth')
def profile_view(request):
    # Safety: Ensure UserProfile exists
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Update User Basic Info
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.save()

        # Update Profile Address Info
        user_profile.address = request.POST.get('address', '')
        user_profile.city = request.POST.get('city', '')
        user_profile.state = request.POST.get('state', '')
        user_profile.zip_code = request.POST.get('zip_code', '')
        user_profile.country = request.POST.get('country', '')
        user_profile.phone = request.POST.get('phone', '')
        user_profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'profile.html', {'orders': recent_orders, 'profile': user_profile})

@login_required(login_url='auth')
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})

@login_required(login_url='auth')
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if order.status == 'Pending':
        order.status = 'Cancelled'
        order.save()
        
        # Restore stock logic
        for item in order.items.all():
            item.product.stock += item.quantity
            item.product.save()

        # Send Cancellation Email
        try:
            send_mail(
                subject=f'Order #{order.id} Cancelled',
                message=f'Hi {order.full_name},\n\nYour order #{order.id} has been cancelled successfully.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[order.email],
                fail_silently=True,
            )
        except:
            pass

        messages.success(request, 'Order cancelled and items returned to stock.')
    else:
        messages.error(request, 'This order cannot be cancelled as it is already processed.')
        
    return redirect('my_orders')



# 1. Update your existing product_detail view:
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    in_wishlist = False
    
    if request.user.is_authenticated:
        # Check if product is in user's wishlist
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        if product in wishlist.products.all():
            in_wishlist = True
            
    return render(request, 'pro_detail.html', {'product': product, 'in_wishlist': in_wishlist})

# 2. Add these two NEW views at the bottom of views.py:
@login_required(login_url='auth')
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'Removed {product.name} from your wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'Added {product.name} to your wishlist.')
        
    # Redirect back to the page the user was on
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required(login_url='auth')
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_products': wishlist.products.all()})

# ==========================================
# 4. AUTHENTICATION MODULE
# ==========================================

def auth_view(request):
    return render(request, 'auth.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            # Authenticate using email as username
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('auth')
    return redirect('auth')

def user_signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('auth')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('auth')

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name
            user.save()
            
            # Welcome Email
            send_mail(
                'Welcome to Stylehub!', 
                f'Hi {full_name}, thank you for joining us.', 
                settings.EMAIL_HOST_USER, 
                [email], 
                fail_silently=True
            )
            
            messages.success(request, "Account created! Please login.")
            return redirect('/auth/?tab=login') 
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('auth')
    return redirect('auth')

def user_logout(request):
    logout(request)
    return redirect('home')

# ==========================================
# 5. CONTACT & SUPPORT
# ==========================================

def contact(request):
    return render(request, 'contact.html')

def contact_submit(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_body = f"From: {full_name} ({email})\nSubject: {subject}\n\n{message}"

        try:
            send_mail(
                subject=f'Contact Form: {subject}',
                message=email_body,
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=[settings.EMAIL_HOST_USER], 
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
        except Exception as e:
            messages.error(request, 'Failed to send message.')
            print(f"Email Error: {e}")

    return redirect('contact')



def about(request):
    return render(request, 'about.html')