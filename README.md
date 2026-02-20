🛍️ Stylehub - Modern E-Commerce Platform

![alt text](https://img.shields.io/badge/Style-Hub-ff4757?style=for-the-badge&logo=django&logoColor=white)


![alt text](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)


![alt text](https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django)


![alt text](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)


![alt text](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)


![alt text](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

Stylehub is a fully-featured, responsive, and dynamic e-commerce web application built using the Django framework. It provides a seamless shopping experience for users with a modern UI, Dark/Light mode, and a powerful custom admin dashboard for store management.
✨ Key Features
🛒 Customer Experience

    Modern UI/UX: Responsive design that works flawlessly on desktop, tablet, and mobile devices.

    🌙 Dark/Light Mode: Seamless theme toggling that saves user preference.

    Product Discovery: Advanced JavaScript-based filtering (by category, price, size) and sorting (price low/high, newest) without page reloads.

    Dedicated Sections: Segmented views for "Featured" (Home), "New Arrivals", and "Main Shop".

    User Accounts: Secure Login, Signup, and Password Reset (via Email).

    Profile Management: Users can update shipping addresses, contact info, and view recent orders.

    Shopping Cart & Wishlist: Add/remove items, update quantities, and save favorite products for later.

    Order Management: Checkout simulation, view order history, and the ability to cancel pending orders (with automated email notifications).

    Live Search: Search bar to quickly find products by name or description.

⚙️ Custom Admin Dashboard

    Secure Access: Only superusers can access the custom /custom-admin/ portal.

    Quick Add Categories: Add multiple categories at once using comma-separated values (e.g., MenWear, WomenWear, KidsWear).

    Product Management: Full CRUD (Create, Read, Update, Delete) for products.

    Visibility Toggles: Control exactly where products show up using checkboxes (Featured on Home, Show in Shop, Show in New Arrivals).

    Order Tracking: View all customer orders, total revenue, total products, and cancel orders on behalf of the store.

🛠️ Tech Stack

    Backend: Python, Django

    Frontend: HTML5, CSS3 (Modular structure with CSS Variables), Vanilla JavaScript

    Database: SQLite (default) / PostgreSQL (production-ready)

    Authentication: Django Built-in Auth System

    Email Service: Django SMTP integration (for password resets and order confirmations)

🚀 Installation & Setup

Follow these steps to get the project running locally on your machine.
1. Clone the repository
code Bash

git clone https://github.com/yourusername/stylehub.git
cd stylehub

2. Create and activate a virtual environment
code Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

(If you have a requirements.txt file)
code Bash

pip install -r requirements.txt

(If you don't have one, just install Django)
code Bash

pip install django pillow

4. Setup the Database

Run the migrations to create the database tables.
code Bash

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Admin)

You will need this account to access the custom admin dashboard.
code Bash

python manage.py createsuperuser

(Follow the prompts to set your email and password)
6. Run the Development Server
code Bash

python manage.py runserver

Visit http://127.0.0.1:8000 in your browser to view the application!
📧 Email Configuration (Important)

For the password reset and order cancellation emails to work, you must configure your SMTP settings in settings.py.

Open stylehub/settings.py and add/update the following at the bottom:
code Python

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # Or your email provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password' # Use an App Password, not your real password

📁 Project Structure Highlights

    models.py: Contains Category, Product, Cart, CartItem, Order, OrderItem, UserProfile, and Wishlist.

    views.py: Handles all logic including catalog display, cart operations, checkout, auth, and the custom admin portal.

    theme.css: Contains the global color variables for Light and Dark mode.

    style1.css - style11.css: Modular stylesheets for specific pages to keep code clean and organized.

👥 Core Team

Built by a dedicated team of developers:

    Sadgyan ji Jaiswal - Frontend Developer

    P.V.S Narayana Murthy - Backend Developer

    Bhanu Teja Sangula - Admin/Database

    Aniket Dutta - Deployment

📜 License

This project is open-source and available under the MIT License.
