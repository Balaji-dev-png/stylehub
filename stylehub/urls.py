
"""
URL configuration for stylehub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Custom Admin Dashboard
    path('custom-admin/', views.admin_dashboard, name='admin_dashboard'),
    path('custom-admin/product/add/', views.admin_add_product, name='admin_add_product'),
    path('custom-admin/product/edit/<int:product_id>/', views.admin_edit_product, name='admin_edit_product'),
    path('custom-admin/product/delete/<int:product_id>/', views.admin_delete_product, name='admin_delete_product'),
    path('custom-admin/order/cancel/<int:order_id>/', views.admin_cancel_order, name='admin_cancel_order'),
    path('custom-admin/category/add/', views.admin_add_category, name='admin_add_category'),
    path('custom-admin/category/delete/<int:category_id>/', views.admin_delete_category, name='admin_delete_category'),

    # Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('team-emails/', views.team_emails, name='team_emails'), # ADDED THIS LINE
    
    # Shop & Product
    path('shop/', views.product_list, name='pro_list'),
    path('shop/<slug:category_slug>/', views.product_list, name='pro_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='pro_detail'),
    path('new-arrivals/', views.new_arrivals, name='new'),
    path('search/', views.search_result, name='search_result'),

    # Cart & Checkout
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place-order/', views.place_order, name='place_order'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),

    # Authentication
    path('auth/', views.auth_view, name='auth'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    # User Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/delete/', views.delete_account, name='delete_account'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),

    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
