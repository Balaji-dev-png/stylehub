import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Q
import stripe
from django.conf import settings
from django.urls import reverse
from .models import Product, Category, Cart, CartItem, Order, OrderItem, UserProfile, Wishlist






# --- Custom Admin Check ---
def is_admin(user):
    return user.is_authenticated and user.is_superuser

# ==========================================
# 1. CATALOG VIEWS
# ==========================================

def home(request):
    # Only show products with is_featured=True
    featured = Product.objects.filter(is_available=True, is_featured=True)[:9]
    return render(request, 'home.html', {'featured_products': featured})




def new_arrivals(request):
    # Only show products with is_new_arrival=True
    new_products = Product.objects.filter(is_available=True, is_new_arrival=True).order_by('-created_at')[:20]
    return render(request, 'new_arrivals.html', {'products': new_products})





def product_list(request, category_slug=None):
    category = None
    all_categories = Category.objects.all()
    # Adding select_related ensures category data is available to the template
    products = Product.objects.filter(is_available=True, show_in_shop=True).select_related('category').order_by('-created_at')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    price_max = request.GET.get('price_max')
    if price_max:
        products = products.filter(price__lte=price_max)
        
    context = {'products': products, 'category': category, 'all_categories': all_categories}
    return render(request, 'pro_list.html', context)







def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    in_wishlist = False
    
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        if product in wishlist.products.all():
            in_wishlist = True
            
    return render(request, 'pro_detail.html', {'product': product, 'in_wishlist': in_wishlist})






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
# 2. CUSTOM ADMIN DASHBOARD VIEWS
# ==========================================

@user_passes_test(is_admin, login_url='home')
def admin_dashboard(request):
    products = Product.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    total_revenue = sum(order.total_price for order in orders if order.status != 'Cancelled')
    
    context = {
        'products': products,
        'recent_orders': orders[:10],
        'total_orders': orders.count(),
        'total_revenue': total_revenue,
        'total_products': products.count(),
        'categories': categories,
    }
    return render(request, 'admin_dashboard.html', context)








@user_passes_test(is_admin, login_url='home')
def admin_add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category = get_object_or_404(Category, id=request.POST.get('category'))
        
        Product.objects.create(
            name=request.POST.get('name'),
            category=category,
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            image_url=request.POST.get('image_url'),
            # SAVING VISIBILITY OPTIONS
            is_featured = request.POST.get('is_featured') == 'on',
            is_new_arrival = request.POST.get('is_new_arrival') == 'on',
            show_in_shop = request.POST.get('show_in_shop') == 'on'
        )
        messages.success(request, "Product added successfully!")
        return redirect('admin_dashboard')

    return render(request, 'admin_product_form.html', {'categories': categories})







@user_passes_test(is_admin, login_url='home')
def admin_edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category = get_object_or_404(Category, id=request.POST.get('category'))
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.description = request.POST.get('description')
        
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        if request.POST.get('image_url'):
            product.image_url = request.POST.get('image_url')
            
        product.is_available = request.POST.get('is_available') == 'on'
        
        # SAVING VISIBILITY OPTIONS
        product.is_featured = request.POST.get('is_featured') == 'on'
        product.is_new_arrival = request.POST.get('is_new_arrival') == 'on'
        product.show_in_shop = request.POST.get('show_in_shop') == 'on'
        
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('admin_dashboard')

    return render(request, 'admin_product_form.html', {'product': product, 'categories': categories})







@user_passes_test(is_admin, login_url='home')
def admin_delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('admin_dashboard')






@user_passes_test(is_admin, login_url='home')
def admin_cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if order.status not in ['Cancelled', 'Delivered']:
        order.status = 'Cancelled'
        order.save()
        for item in order.items.all():
            item.product.stock += item.quantity
            item.product.save()
        try:
            send_mail(
                subject=f'Update regarding your Order #{order.id} | Stylehub',
                message=f"Hi {order.full_name},\n\nWe apologize to inform you that we cannot deliver your recent order #{order.id}. Your order has been cancelled.\n\nBest Regards,\nThe Stylehub Team",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[order.email],
                fail_silently=True,
            )
        except:
            pass
        messages.success(request, f'Order #{order.id} cancelled.')
    else:
        messages.error(request, 'Order cannot be cancelled.')
    return redirect('admin_dashboard')








# --- CATEGORY VIEWS (COMMA SEPARATED) ---
@user_passes_test(is_admin, login_url='home')
def admin_add_category(request):
    if request.method == 'POST':
        names = request.POST.get('name')
        if names:
            category_names = [n.strip() for n in names.split(',') if n.strip()]
            created_count = 0
            for name in category_names:
                obj, created = Category.objects.get_or_create(name=name)
                if created:
                    created_count += 1
            
            if created_count > 0:
                messages.success(request, f"Successfully added {created_count} categories! ({', '.join(category_names)})")
            else:
                messages.warning(request, "No new categories were added (they might already exist).")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Category name cannot be empty.")
    
    return render(request, 'admin_category_form.html')






@user_passes_test(is_admin, login_url='home')
def admin_delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_name = category.name
    category.delete()
    messages.success(request, f"Category '{category_name}' deleted.")
    return redirect('admin_dashboard')







# ==========================================
# 3. CART & CHECKOUT MODULE
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
        
    # Check if it's an AJAX request from your Javascript
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success', 
            'cart_count': cart.items.count(),
            'message': f'Added {product.name} to cart!'  # <-- THIS LINE FIXES THE "UNDEFINED" ISSUE
        })
        
    return redirect('cart')







@login_required(login_url='auth')
def update_cart(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if action == 'inc':
        item.quantity += 1
        item.save()
    elif action == 'dec':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
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
    profile = UserProfile.objects.filter(user=request.user).first()
    return render(request, 'checkout.html', {'cart': cart, 'profile': profile})







# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='auth')
def place_order(request):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        
        request.session['checkout_data'] = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'address': f"{request.POST.get('address')}, {request.POST.get('city')}, {request.POST.get('zip')}",
            'city': request.POST.get('city'),
        }

        line_items = []
        for item in cart.items.all():
            line_items.append({
                'price_data': {
                    'currency': 'usd', 
                    'product_data': {
                        'name': item.product.name,
                    },
                    # Converting Decimal to Float, then to Integer cents
                    'unit_amount': int(float(item.product.price) * 100), 
                },
                'quantity': item.quantity,
            })

        # Ensure API key is set right before calling it (Fixes .env loading issues)
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # We removed try/except so it WILL crash and show us the error!
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success')),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )
        
        return redirect(checkout_session.url, code=303)
        
    return redirect('checkout')






# --- NEW VIEW: Runs only if Stripe payment is successful ---
@login_required(login_url='auth')
def payment_success(request):
    cart = get_object_or_404(Cart, user=request.user)
    checkout_data = request.session.get('checkout_data')

    if not checkout_data or not cart.items.exists():
        # Check if they just completed an order successfully (it clears the session)
        latest_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
        if latest_order and (latest_order.status == 'Pending' or latest_order.status == 'Shipped' or latest_order.status == 'Delivered'):
             return render(request, 'success.html', {'order': latest_order})
        return redirect('home')

    # Create the actual order now that payment is confirmed
    order = Order.objects.create(
        user=request.user,
        full_name=f"{checkout_data['first_name']} {checkout_data['last_name']}",
        email=checkout_data['email'],
        address=checkout_data['address'],
        city=checkout_data['city'],
        total_price=cart.get_total()
    )
    
    for item in cart.items.all():
        OrderItem.objects.create(
            order=order, 
            product=item.product, 
            price=item.product.price, 
            quantity=item.quantity
        )
        if item.product.stock >= item.quantity:
            item.product.stock -= item.quantity
            item.product.save()
    
    # Clear cart and session data
    cart.items.all().delete()
    del request.session['checkout_data']
    
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








# --- NEW VIEW: Runs if user clicks "back" on the Stripe page ---
@login_required(login_url='auth')
def payment_cancel(request):
    messages.error(request, "Payment was cancelled. Please try again.")
    return redirect('checkout')






# ==========================================
# 4. USER DASHBOARD & PROFILE
# ==========================================

@login_required(login_url='auth')
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.save()

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
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been successfully deleted.")
        return redirect('home')
    return redirect('profile')



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
        for item in order.items.all():
            item.product.stock += item.quantity
            item.product.save()
        messages.success(request, 'Order cancelled.')
    return redirect('my_orders')






@login_required(login_url='auth')
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'Removed {product.name} from wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'Added {product.name} to wishlist.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))








@login_required(login_url='auth')
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_products': wishlist.products.all()})







# ==========================================
# 5. AUTHENTICATION MODULE
# ==========================================

def auth_view(request):
    return render(request, 'auth.html')





def user_login(request):
    if request.method == 'POST':
        user_obj = User.objects.filter(email=request.POST.get('email')).first()
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Invalid email or password.')
        return redirect('auth')
    return redirect('auth')






def user_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if password != request.POST.get('confirm_password'):
            messages.error(request, "Passwords do not match.")
            return redirect('auth')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('auth')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = request.POST.get('full_name')
        user.save()
        messages.success(request, "Account created! Please login.")
        return redirect('/auth/?tab=login') 
    return redirect('auth')





def user_logout(request):
    logout(request)
    return redirect('home')




def contact(request):
    return render(request, 'contact.html')





def contact_submit(request):
    if request.method == 'POST':
        messages.success(request, 'Message sent successfully!')
    return redirect('contact')




def about(request):
    return render(request, 'about.html')





def team_emails(request):
    return render(request, 'team_emails.html')