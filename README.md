# 🛍️ Stylehub — Modern E-Commerce Platform

**Stylehub** is a high-performance, responsive e-commerce solution built with Django. It bridges the gap between a sleek consumer experience and a powerful, data-driven management suite. Featuring dynamic theme toggling, advanced JS filtering, and a bespoke administrative portal.

---
<img width="2879" height="1384" alt="Screenshot 2026-02-20 220428" src="https://github.com/user-attachments/assets/6eb9b4ed-4375-497a-aa91-0b3e49d6bb48" />
<img width="2879" height="1526" alt="Screenshot 2026-02-20 220448" src="https://github.com/user-attachments/assets/e4aeea9a-12e8-4c79-b169-cef9671c3698" />
<img width="2879" height="963" alt="Screenshot 2026-02-20 220507" src="https://github.com/user-attachments/assets/aa3f010b-df24-4151-802a-23d753667613" />
<img width="2879" height="1540" alt="Screenshot 2026-02-20 220338" src="https://github.com/user-attachments/assets/fa16aad2-046e-4cfb-b7ce-8a830fb2d808" />
<img width="2879" height="1535" alt="Screenshot 2026-02-20 220552" src="https://github.com/user-attachments/assets/6f64e721-9c6c-47b7-b169-b3b58bdf6cef" />
<img width="2879" height="1534" alt="Screenshot 2026-02-20 220533" src="https://github.com/user-attachments/assets/8688a47d-3cd4-4e30-a4b7-15707266f146" />
<img width="2879" height="1533" alt="Screenshot 2026-02-20 220750" src="https://github.com/user-attachments/assets/3ae2d700-5303-4dca-a40a-5c367f41c8b8" />
<img width="2871" height="1441" alt="Screenshot 2026-02-20 220729" src="https://github.com/user-attachments/assets/fdeb6e74-9d12-4b4b-9c57-24b4507251ad" />
<img width="2870" height="1538" alt="Screenshot 2026-02-20 220704" src="https://github.com/user-attachments/assets/41d622ce-54f1-4155-a859-0cf4c39ccf33" />
<img width="2879" height="1214" alt="Screenshot 2026-02-20 220643" src="https://github.com/user-attachments/assets/065c1e87-b05a-45f9-80c7-64cb0e949fd9" />
<img width="2879" height="1508" alt="Screenshot 2026-02-20 220617" src="https://github.com/user-attachments/assets/344586f9-9422-48cc-97ed-9c6be322a92b" />

## 🌟 New Features: Multi-Vendor & Admin Isolation

* **🔐 Dedicated Admin Auth:** A standalone `/custom-admin/auth/` portal exclusively for vendors and store administrators.
* **🛡️ Data Isolation:** Each Admin gets a perfectly isolated dashboard. They can only see, edit, and delete their own products and orders.
* **📈 Accurate Revenue Tracking:** Revenue charts are automatically calculated based on only the products owned by the currently logged-in admin.
* **⚡ Backward Compatibility:** Products without an explicitly assigned admin (legacy items) automatically fall back to the main superuser to ensure nothing gets lost.

*(Please add screenshots of the new Admin Auth page and Isolated Dashboard here)*


## ✨ Key Features

### 🛒 Customer Experience

* **🌓 Adaptive Theming:** Native Dark/Light mode support with persistent user preferences and dynamic background transitions.
* **✨ Modern UI & Animations:** Fluid SPA-like page navigation transitions, grayscale-to-color bloom hover effects, and elegant pop-and-reveal overlays for product cards.
* **⚡ Dynamic Discovery:** JavaScript-powered filtering by price, size, and category with zero page reloads.
* **💳 Secure Checkout:** Fully integrated with **Stripe API** for secure, PCI-compliant payment processing.
* **📦 Order Lifecycle:** Full checkout simulation, real-time order tracking, and automated email notifications.
* **❤️ Wishlist & Cart:** Persistent storage for user favorites and a seamless multi-item checkout flow.

### ⚙️ Custom Admin Dashboard (`/custom-admin/`)

* **📊 Business Intelligence:** Real-time metrics for total revenue, order volume, and product inventory based directly on the admin's own assigned items.
* **🚀 Bulk Operations:** Quickly categorize inventory with comma-separated tag inputs.
* **🎯 Visibility Control:** One-click toggles to feature products on the Homepage, New Arrivals, or the Main Shop.
* **🔒 Seamless Isolation:** Automatically tracks the ownership of every product and category you create.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.11+, Django 6.0+
* **Payments:** Stripe API (Python Library)
* **Database:** PostgreSQL (Production), SQLite (Development/CI)
* **Frontend:** HTML5, CSS3 (Modular CSS Variables), Vanilla JavaScript
* **Auth & Security:** Django Identity & GitHub Actions CI/CD
* **Communications:** SMTP Integration for transactional emails

---

## 🚀 Installation & Setup

### 1. Clone & Environment

```bash
git clone https://github.com/yourusername/stylehub.git
cd stylehub
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

```

### 2. Dependencies & Environment Variables

Install the core requirements:

```bash
pip install -r requirements.txt

```

Create a `.env` file in the root directory and add your credentials (do not commit this file!):

```env
DEBUG=True
SECRET_KEY=your_secret_key

# Database
DB_NAME=stylehub_db
DB_USER=postgres
DB_PASSWORD=your_password

# Stripe Keys
STRIPE_PUBLIC_KEY=pk_test_your_public_key
STRIPE_SECRET_KEY=sk_test_your_secret_key

# Email
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

```

### 3. Database Initialization

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

### 4. Launch

```bash
python manage.py runserver

```

---

## 📁 Project Architecture

```text
├── core/               # Project settings & WSGI
├── store/              # Main application logic
│   ├── models.py       # Product, Cart, Order, UserProfile
│   ├── views.py        # Logic for Storefront, Stripe Checkout & Admin
│   └── templates/      # Split into /shop and /admin_custom
├── static/
│   ├── css/            # Modular style1.css to style11.css
│   └── js/             # Filtering, Stripe Elements, & Theme logic
└── .github/workflows/  # CI/CD Pipeline configuration

```

---

## 👥 Core Team

* **Sadgyan ji Jaiswal** — *Frontend Architect*
* **P.V.S Narayana Murthy** — *Backend Systems*
* **Bhanu Teja Sangula** — *Database & Admin Logic*
* **Aniket Dutta** — *DevOps & Deployment*

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
