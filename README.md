# 🛒 StyleHub — Full-Stack E-Commerce Platform

---

## 📅 Project Overview

**StyleHub** is a modern **full-stack e-commerce application** developed using **Django 6.0**, **Django REST Framework**, and **PostgreSQL**.
The project focuses on **real-world system design**, **clean architecture**, and **scalable workflows**, similar to production-level applications.

The goal was not only to build features, but to understand **how a real e-commerce system works internally**.

---

## 🧠 What is StyleHub?

StyleHub is a **complete shopping platform** where users can:

* Browse products
* Add items to cart
* Place orders
* Track purchases
* Manage profiles
* Experience a premium UI with light & dark themes

Admins can manage products, stock, and orders from a powerful backend dashboard.

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



## 🚀 Core Features Implemented

### 🎨 Modular UI Design

* Page-specific CSS loading
* 11 optimized stylesheets
* Clean, minimal, Apple-inspired layout
* Faster load times and better maintainability

---

### 🌓 Light & Dark Theme Support

* Theme preference stored in browser
* Automatically applied on page load
* Instant toggle without refresh
* Implemented using CSS variables

---

### ⚡ Real-Time User Interactions

* AJAX-powered “Add to Cart”
* No page reload during cart updates
* Smooth slide-in notifications
* Better user experience and responsiveness

---

### 🔐 Secure Authentication System

* Session-based authentication for users
* Token-based authentication for APIs
* Protected routes for orders, cart, and profile
* Secure access control across the platform

---

### 👤 Automated User Profile Creation

* User profile generated instantly on signup
* Implemented using Django Signals
* Eliminates manual profile handling
* Ensures consistent user data

---

## 🧩 Core Functional Modules

### 🛍️ Product Management

* Product categories
* Product images & descriptions
* Price and stock handling
* Admin-controlled visibility

---

### 🛒 Cart System

* Add/remove products dynamically
* Quantity management
* Cart persists per user
* Seamless checkout flow

---

### 📦 Order Management

* Order creation after checkout
* Order status tracking
* User-specific order history
* Admin approval and cancellation

---

### 🔄 Inventory Automation

* Stock reduces automatically after order placement
* Stock restores when order is cancelled
* Prevents over-selling
* Maintains data integrity

---

## 🗂️ Project Architecture Explained

### 🧠 Backend Configuration (stylehub/)

Acts as the **brain of the project**.

* Global settings and configurations
* Secure environment-based variables
* URL routing for all modules
* Serializer layer for API communication

---

### 🏪 Store Application (store/)

Handles **all business logic**.

Includes:

* Product & category models
* Cart and order logic
* User profiles & wishlist
* Views managing user journeys

---

### 🖥️ Frontend Templates (templates/)

* 19 structured HTML templates
* Built using Django Template Language
* Marketing pages, cart pages, dashboards
* Reusable layout components

---

### 🎯 Static Assets (static/)

* Modular CSS architecture
* JavaScript for:

  * Theme switching
  * Animations
  * Secure background requests
* Only required assets load per page

---

## ⚙️ Environment & Security Design

### 🔐 Environment Variables

All sensitive data is stored securely using environment variables:

* Database credentials
* Secret keys
* Debug configuration
* Email credentials

This ensures:

* Security
* Clean codebase
* Safe deployment
* Easy team collaboration

---

## ✉️ Email Integration

* Gmail SMTP configured
* Ready for notifications and alerts
* Credentials managed securely
* Extendable for future features

---

## 🧪 Reliability & Best Practices

* Django Signals for automation
* Clean separation of concerns
* Defensive checks for data consistency
* Admin-level control for safety

---

## 🛠️ Development Philosophy

* Clean & readable structure
* Modular and scalable design
* Production-oriented mindset
* Real-world workflows over demo logic

This project is structured like a **company-level codebase**, not a basic tutorial.

---

## 📈 Future Enhancements

* Online payment gateway
* Order tracking system
* Product reviews & ratings
* Admin analytics dashboard
* Docker & CI/CD integration
* Mobile-ready API expansion

---

## 🏁 Final Note

**StyleHub** demonstrates a complete understanding of:

* Backend development with Django
* API design using DRF
* Database handling with PostgreSQL
* UI/UX structuring
* Secure, scalable system design

It is **deployment-ready** and designed with **industry standards** in mind.
