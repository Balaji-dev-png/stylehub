# 🛍️ Stylehub — Modern E-Commerce Platform

**Stylehub** is a high-performance, responsive e-commerce solution built with Django. It bridges the gap between a sleek consumer experience and a powerful, data-driven management suite. Featuring dynamic theme toggling, advanced JS filtering, and a bespoke administrative portal.

---

## ✨ Key Features

### 🛒 Customer Experience

* **🌓 Adaptive Theming:** Native Dark/Light mode support with persistent user preferences.
* **⚡ Dynamic Discovery:** JavaScript-powered filtering by price, size, and category with zero page reloads.
* **📦 Order Lifecycle:** Full checkout simulation, real-time order tracking, and automated email notifications.
* **❤️ Wishlist & Cart:** Persistent storage for user favorites and a seamless multi-item checkout flow.

### ⚙️ Custom Admin Dashboard (`/custom-admin/`)

* **📊 Business Intelligence:** Real-time metrics for total revenue, order volume, and product inventory.
* **🚀 Bulk Operations:** Quickly categorize inventory with comma-separated tag inputs.
* **🎯 Visibility Control:** One-click toggles to feature products on the Homepage, New Arrivals, or the Main Shop.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.11+, Django 4.x
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
DB_NAME=stylehub_db
DB_USER=postgres
DB_PASSWORD=your_password
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
├── shop/               # Main application logic
│   ├── models.py       # Product, Cart, Order, UserProfile
│   ├── views.py        # Logic for Storefront & Custom Admin
│   └── templates/      # Split into /shop and /admin_custom
├── static/
│   ├── css/            # Modular style1.css to style11.css
│   └── js/             # Filtering & Theme logic
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

---

