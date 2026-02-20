## 🛒 Store API Module

This module powers the **data layer and business logic** of the StyleHub e-commerce platform.
Built using **Django REST Framework (DRF)**, it exposes a **secure, scalable, and well-structured API** for products, carts, and orders.

The API is designed with **real-world security rules** and **user-level data isolation** in mind.

---

## 📋 Key Features

### 🔄 Automated Serialization

* Converts complex Django models into clean JSON
* Enables seamless frontend and API communication
* Reduces manual data handling

---

### 🔐 Restricted Access Control

* Public users can browse products freely
* Sensitive operations require authentication
* Prevents unauthorized data access

---

### 👤 User-Specific Data Isolation

* Orders are filtered at the database level
* Users can only view and manage **their own orders**
* Eliminates the risk of data leakage

---

## 🛠 Technical Overview

---

### 🧠 Serializers (`serializers.py`)

Serializers act as the **bridge between PostgreSQL and the frontend/UI layer**.

They define how data is exposed and validated before being sent to clients.

#### 🏷 Product Serializer

* Exposes product name, price, description, images, and stock
* Used by shop pages and product detail views

#### 🛒 Cart Serializer

* Handles temporary shopping cart data
* Supports session-based and user-linked carts
* Ensures accurate quantity and price calculations

#### 📦 Order Serializer

* Processes final checkout data
* Includes order items, totals, and status
* Used for order history and confirmations

---

### ⚙️ ViewSets (`views.py`)

The API uses **ModelViewSet** to provide standard REST operations automatically.

This ensures:

* Cleaner code
* REST-compliant endpoints
* Consistent behavior across resources

---

### 🔗 API Endpoint Behavior

#### 🏪 Products

* **View Products** → Public access
* **Add Products** → Admin-only access

#### 📦 Orders

* **View Orders** → Authenticated users only
* **Place Orders** → Authenticated users only
* Orders are strictly limited to the logged-in user

---

### 🔐 Security Logic — Order Isolation

To protect user privacy:

* Order queries are overridden internally
* Even if an order ID is guessed, access is denied
* Each request is automatically scoped to the current user

This guarantees **strict ownership enforcement** at the database level.

---

## 🚀 Getting Started with the API

### 🧰 Environment

* Ensure Docker containers for:

  * PostgreSQL
  * Django backend
    are running correctly

---

### 🔗 Browsable API

* Visit the products endpoint to explore available items
* DRF’s browsable interface allows easy testing and inspection

---

### 🔑 Authentication

* Orders endpoint requires authentication
* Supported methods:

  * Session Authentication
  * Bearer Token Authentication
* Ensures secure access for user-specific data

---

## ✅ Why This API Design Works

* REST-standard architecture
* Strong authentication boundaries
* Zero data leakage risk
* Clean serializer-driven data flow
* Frontend-ready JSON responses

This module transforms StyleHub into a **true API-driven e-commerce platform**, suitable for **web, mobile, or future integrations**.

