## ⚙️ StyleHub — Core Configuration

This directory represents the **central brain of the StyleHub e-commerce platform**.
It is responsible for **global configuration, URL routing, environment security, and deployment readiness**.

Every request, feature, and integration in StyleHub is governed from here.

---

## 📂 Files Overview

---

### 🧠 `settings.py` — The Control Center

This file defines **all global configurations** required to run StyleHub efficiently and securely.
It is fully modernized for **Django 6.0** and follows production-level best practices.

#### 🔐 Security

* Sensitive data is loaded using **environment variables**
* Secrets like **SECRET_KEY**, database passwords, and email credentials are never hardcoded
* Enhances security and prevents accidental leaks

#### 🗄️ Database Configuration

* Uses **PostgreSQL** for reliable and high-performance data handling
* Designed for scalability and real-world traffic

#### 🔑 Authentication System

* Supports **Session Authentication** for web users
* Supports **Token Authentication** for API access (DRF)
* Enables both frontend and API-based interactions

#### 🎨 Static & Media Handling

* Static files (CSS, JS) served from `static/`
* User-uploaded content (product images) stored in `media/`
* Fully configured paths for development and production

#### ✉️ Email Integration

* Gmail SMTP configured for:

  * Order confirmations
  * Password reset emails
* Secure credential handling via environment variables

#### 🛒 Context Processors

* Custom **cart_count** context processor
* Displays live cart item count on every page
* Improves real-time user experience across the site

---

### 🗺️ `urls.py` — The Router

This file acts as the **navigation map** of the entire application.
It connects user-friendly URLs to their respective views and features.

#### 🔗 URL Categories Covered

**🏪 Storefront**

* Home
* About
* Contact
* Shop
* New Arrivals

**🔐 Authentication**

* Login
* Signup
* Logout
* Password Reset

**🛒 Shopping**

* Cart
* Add to Cart
* Checkout
* Place Order

**👤 User Profile**

* Profile Dashboard
* My Orders
* Wishlist

**🛠 Custom Admin**

* Admin Dashboard
* Product Management (Add / Edit / Delete)
* Category Management

📌 **Development Note**

* Includes a conditional setup to serve **media files (images)** during development mode
* Ensures images display correctly without external servers

---

### 🌐 `wsgi.py` — The Server Interface

WSGI (Web Server Gateway Interface) allows Django to **communicate with production servers**.

* Acts as the bridge between Django and servers like **Gunicorn** or **Apache**
* Required for deploying StyleHub to live environments
* Ensures smooth request-response handling in production

---

## 🛠 Setup & Environment Requirements

To run StyleHub correctly, a **`.env` file** must be created in the project root directory.

This file stores all sensitive configuration details required by `settings.py`.

### 🔑 Required Environment Variables

* Secret Key
* Debug mode
* PostgreSQL credentials
* Email (SMTP) credentials

📌 **Best Practice**

* `.env` is never committed to version control
* `.env.example` is shared for team collaboration

---

## 🗺 Application Workflow (Request Lifecycle)

### 🔄 How a Request is Processed

1. **Request**

   * User enters a URL (example: `/shop/`)

2. **Routing**

   * `urls.py` matches the URL to the correct view

3. **Configuration**

   * `settings.py` provides:

     * Database connections
     * Static and media paths
     * Authentication rules

4. **Response**

   * Server returns:

     * Rendered HTML page **or**
     * JSON response (API)

This clean flow ensures **performance, security, and reliability**.

---

## ✅ Why This Configuration Matters

* Secure by default
* Production-ready architecture
* Easy to scale and deploy
* Clean separation of concerns
* Industry-standard Django setup

---

