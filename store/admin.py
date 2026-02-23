from django.contrib import admin
from .models import Category, Product, Order, OrderItem, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Added the new booleans so you can see them at a glance
    list_display = ['name', 'category', 'price', 'is_available', 'is_featured', 'show_in_shop', 'is_new_arrival']

    list_filter = ['category', 'is_available', 'is_featured', 'is_new_arrival', 'show_in_shop']

    list_editable = ['is_available', 'is_featured', 'show_in_shop', 'is_new_arrival']

    prepopulated_fields = {'slug': ('name',)}
    
    search_fields = ['name']








@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'country']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0








@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'status', 'total_price', 'created_at']
    list_filter = ['status']
    inlines = [OrderItemInline]
    readonly_fields = ['created_at']