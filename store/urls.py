
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('shop/', views.product_list, name='pro_list'),
#     path('shop/<slug:category_slug>/', views.product_list, name='pro_list_by_category'),
#     path('product/<slug:slug>/', views.product_detail, name='pro_detail'),
#     path('new-arrivals/', views.new_arrivals, name='new'),
#     path('search/', views.search_result, name='search_result'),
    
#     # Cart
#     path('cart/', views.cart_view, name='cart'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
#     # Checkout & Orders
#     path('checkout/', views.checkout, name='checkout'),
#     path('place-order/', views.place_order, name='place_order'),
#     path('my-orders/', views.my_orders, name='my_orders'),
#     path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'), # New Line
    
#     # Auth
#     path('auth/', views.auth_view, name='auth'),
#     path('login/', views.user_login, name='login'),
#     path('signup/', views.user_signup, name='signup'),
#     path('logout/', views.user_logout, name='logout'),
    
#     # Contact
#     path('contact/', views.contact, name='contact'),
#     path('contact/submit/', views.contact_submit, name='contact_submit'),
# ]