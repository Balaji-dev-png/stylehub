## 🛍️ StyleHub — Core Store Application

This directory contains the **core business logic, data models, and administrative controls** for the StyleHub e-commerce platform.
It is responsible for managing the **entire shopping lifecycle**, from product discovery to order fulfillment and user engagement.

---

## 🚀 Features at a Glance

### 🏷️ Dynamic Product Catalog

* Category-based product browsing
* Price filtering and search
* Clean product detail pages
* Optimized database queries

---

### 🛠 Custom Admin Dashboard

* Dedicated staff-only views
* Product & category management
* Revenue and order tracking
* Secure admin-restricted access

---

### 🛒 Persistent Shopping Cart

* AJAX-enabled cart updates
* Quantity changes without page reload
* Global cart badge tracking
* Smooth checkout transition

---

### 👤 Automated User Profiles

* Profile creation via **Django Signals**
* No manual profile handling
* Prevents data inconsistency
* Ensures user-related data integrity

---

### 📦 Order Management System

* Complete order lifecycle:

  * Pending
  * Confirmed
  * Delivered
* Automated stock adjustment
* Email confirmations on order placement

---

### ❤️ Wishlist System

* One-click product saving
* User-specific wishlist
* Improves return visits and engagement

---

## 📂 Core Component Breakdown

---

### 🧠 `models.py` — The Data Engine

Defines the **database schema and relationships** that power the entire store.
The models are organized into **four logical modules** for clarity and scalability.

#### 🏷️ Product Catalog

* Manages inventory and categorization
* **Models:** Category, Product

#### 🛒 Cart System

* Temporary item storage per user/session
* **Models:** Cart, CartItem

#### 📦 Order Management

* Tracks completed purchases and items
* Stores shipping and order status
* **Models:** Order, OrderItem

#### 👤 User & Loyalty

* Handles extended user information
* Manages saved products
* **Models:** UserProfile, Wishlist

---

### ⚙️ `views.py` — The Business Logic

Controls how users interact with the application.
Views are structured into **high-level functional modules**.

#### 🏪 Catalog Views

* Homepage
* New arrivals
* Product detail pages

#### 🛠 Admin Dashboard Views

* Restricted using admin checks
* Add / edit / delete products
* Category management

#### 🛒 Cart & Checkout Views

* Add/remove items
* Quantity updates
* Checkout flow
* Simulated payment handling

#### 🔐 Auth & User Dashboard

* Secure login and signup
* Order history
* Profile access

---

### 🛠 `admin.py` — The Control Panel

The Django Admin is **custom-tailored** for a professional store-owner experience.

#### 📦 Product Management

* Editable product lists
* Inline price and stock updates
* Faster inventory control

#### 📑 Order Inlines

* View all items inside an order
* Uses **TabularInline** for clarity
* No need to open each item separately

#### 🔍 Searchable User Profiles

* Search users by:

  * Phone number
  * City
* Faster customer lookup

---

### 🌍 `context_processors.py` — The Global Helper

A lightweight but powerful utility file.

* Injects **cart_count** into every template
* Keeps navbar cart badge updated globally
* Eliminates repeated logic in views
* Enhances real-time user feedback

---

## 🛡 Reliability & Data Safety

---

### 🧠 Smart Profile Signals

To prevent common Django errors like **RelatedObjectDoesNotExist**:

* UserProfile is created automatically on user creation
* Profile existence is guaranteed on every save
* Ensures stable user-model relationships

---

### 📦 Intelligent Stock Control

* Product stock decreases automatically on order placement
* If a **Pending** order is cancelled:

  * Stock is restored automatically
* Prevents over-selling
* Maintains inventory accuracy

---

## ✅ Why This Store App Matters

* Clean separation of concerns
* Real-world e-commerce logic
* Automated data consistency
* Admin-friendly controls
* Scalable and maintainable design

This module forms the **core engine** of StyleHub and reflects **production-ready Django architecture**.

---

