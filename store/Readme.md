🛍️ Stylehub: The Core Store Application

This directory contains the primary logic, data structures, and administrative controls for the Stylehub e-commerce platform. It is designed to handle everything from product discovery to secure checkout and user management.

🚀 Features at a Glance

Dynamic Product Catalog: Categorized browsing, price filtering, and full-text search.
Custom Admin Dashboard: A dedicated interface for staff to manage products, categories, and track revenue.
Persistent Shopping Cart: AJAX-enabled cart updates with global badge tracking.
Automated User Profiles: Real-time profile generation via Django signals to prevent data inconsistency.
Order Management: Complete order lifecycle from "Pending" to "Delivered," including automated stock adjustment and email confirmations.
Wishlist System: One-click product saving for registered users.

📂 Core Component Breakdown

1. models.py — The Data Engine

This file defines the heart of the application using four distinct modules:

ModulePurposeKey ModelsProduct CatalogManages inventory and categorization.Category, ProductCart SystemHandles temporary item storage for users.Cart, CartItemOrder ManagementTracks final sales, shipping details, and items.Order, OrderItemUser & LoyaltyHandles user data and saved items.UserProfile, Wishlist

2. views.py — The Business Logic

The views are organized into high-level modules to manage the user journey:

Catalog Views: Handles the homepage, arrivals, and product details.
Admin Dashboard: Restricted views (is_admin) for adding/editing products and categories.
Cart & Checkout: Manages the logic for item quantity updates and "Randomized" payment simulation.
Auth & Dashboard: Handles secure login, signup, and personal order history.

3. admin.py — The Control Panel

The Django admin is heavily customized to provide a "pro" experience for site owners:

Product Management: Includes editable lists for quick price and stock updates.
Order Inlines: View every item in an order directly from the main Order view using TabularInline.
Searchable Profiles: Find users quickly via phone number or city.

4. context_processors.py — The Global Helper

This small but mighty file provides the cart_count variable to every single template in the project, ensuring the navigation bar badge always reflects the user's current cart size.

🛠 Reliability Features

🛡️ Smart Profile Signals

To prevent the common RelatedObjectDoesNotExist error, the app uses a robust signal receiver. It automatically creates a UserProfile whenever a new User is created and ensures it exists during every save operation.

📦 Stock Control

When an order is placed, the system automatically decrements product stock. Conversely, if an admin or user cancels a "Pending" order, the inventory is automatically returned to the shelves.


store readme file