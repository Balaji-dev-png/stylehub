# 🛍️ Stylehub — Modern E-Commerce Platform

**Stylehub** is a high-performance, responsive e-commerce solution built with Django. It bridges the gap between a sleek consumer experience and a powerful, data-driven management suite. Featuring dynamic theme toggling, advanced JS filtering, and a bespoke administrative portal.

<img width="2879" height="1540" alt="image" src="https://github.com/user-attachments/assets/38020464-0304-451c-8806-a719fca16493" />
<img width="2879" height="1384" alt="image" src="https://github.com/user-attachments/assets/d017469b-4843-428f-bb4d-2f241a9cb487" />
<img width="2879" height="1526" alt="image" src="https://github.com/user-attachments/assets/94e95b7e-529a-4183-bb51-6cceab79a3c2" />
<img width="2879" height="963" alt="image" src="https://github.com/user-attachments/assets/b3a623df-7481-4feb-bfc5-4b8ba70bc4ac" />
<img width="2879" height="1534" alt="image" src="https://github.com/user-attachments/assets/8aa784b8-d195-4d7e-91e3-e05a3266b8c2" />
<img width="2879" height="1535" alt="image" src="https://github.com/user-attachments/assets/06af2804-9101-4ef6-bce4-abe7980a2078" />
<img width="2879" height="1508" alt="image" src="https://github.com/user-attachments/assets/e0b55321-40bf-47a1-a5d3-d62cdf7e6e92" />
<img width="2879" height="1214" alt="image" src="https://github.com/user-attachments/assets/6c733056-60b2-4ff3-a867-6e982658ce9f" />
<img width="2870" height="1538" alt="image" src="https://github.com/user-attachments/assets/1e170f7d-c8cf-40b3-845f-53051f83e752" />
<img width="2871" height="1441" alt="image" src="https://github.com/user-attachments/assets/95cb92d3-c005-46a8-957e-221fe2a3aae7" />
<img width="2879" height="1533" alt="image" src="https://github.com/user-attachments/assets/45aabe53-9b42-4227-8e4c-6b41d192ddc4" />




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

