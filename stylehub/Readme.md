⚙️ StyleHub: Core Configuration

This directory contains the central brain of the StyleHub e-commerce platform. It manages global settings, URL routing, and server deployment interfaces.

📂 Files Overview

1. settings.py — The Control Center
This file contains all the configurations for the StyleHub project. It has been modernized for Django 6.0 with several professional features:

Security: Uses python-dotenv to load sensitive data (Secret Keys, Database Passwords) from environment variables to keep the project secure.
Database: Configured to use PostgreSQL for high-performance data management.Authentication: Supports both standard Session Authentication and DRF Token Authentication for API access.Static & Media: Fully configured to handle CSS/JS (static/) and user-uploaded product images (media/).
Email System: Integrated with Gmail SMTP to handle order confirmations and password resets.
Context Processors: Includes a custom cart_count processor to display the live cart item count on every page.

2. urls.py — The Router
This is the "Map" of the entire application. It connects user-friendly URLs to the logic in your views.

CategoryKey EndpointsStorefronthome, about, contact, shop, new-arrivalsAuthlogin, signup, logout, password_resetShoppingcart, add-to-cart, checkout, place-orderProfileprofile, my-orders, wishlistCustom AdminDashboard, Product/Category management (Add/Edit/Delete)

Note: The urls.py also includes a special conditional check to serve Media files (images) during development mode.

3. wsgi.py — The Server Interface

The Web Server Gateway Interface (WSGI) is the standard used by Django to communicate with web servers like Gunicorn or Apache. It ensures that StyleHub can be deployed to production environments efficiently.

🛠 Setup & Requirements

To run this project correctly, ensure you have a .env file in your root directory with the following keys:

Bash
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=stylehub_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password

🗺 Application Workflow

Request: A user enters a URL (e.g., /shop/).
Routing: urls.py identifies the URL and sends the request to the correct view.
Configuration: settings.py provides the view with the necessary database connections and static file paths.
Response: The server sends back the rendered HTML page or JSON data to the user.

stylehub readme file