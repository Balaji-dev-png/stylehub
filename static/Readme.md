## 🛒 Full-Stack Store Application

A **modern, responsive e-commerce platform** built using **Django REST Framework** and a **custom modular design system**.
The application delivers a **seamless shopping experience** with real-time cart updates, persistent dark mode, and secure order handling.

This project blends **backend robustness** with **frontend polish**, closely mirroring real-world production systems.

---

## 🧱 Project Architecture Overview

The application is structured into **three core layers**:

1. Backend API (Data & Security)
2. Design System (Visual Consistency)
3. Interactive Logic (User Experience)

Each layer is isolated, scalable, and purpose-driven.

---

## 🔗 Backend API (`/api`)

The backend API is built using **Django REST Framework (DRF)** and serves as the **data access layer** for the frontend.

### 📦 Serializers (`serializers.py`)

* Uses **ModelSerializer** for clean data conversion
* Transforms Product, Cart, and Order models into JSON
* Ensures consistent data representation across views

---

### ⚙️ ViewSets (`views.py`)

* Implements **ModelViewSet** for standard CRUD operations
* Reduces boilerplate while maintaining clarity
* REST-compliant endpoint design

---

### 🔐 API Security

* Uses **IsAuthenticatedOrReadOnly**
* Public access for browsing products
* Authenticated access required for:

  * Cart actions
  * Orders
* Custom `get_queryset` ensures users can only view **their own orders**

This guarantees **data privacy and access control**.

---

## 🎨 Design System (`/static/css`)

The UI is powered by a **custom CSS variable engine** that enables **instant theme switching** and consistent styling across all pages.

### 🧩 Modular Stylesheet Strategy

Each page loads only its required stylesheet, ensuring:

* Faster page load times
* Clean separation of concerns
* Easier long-term maintenance

#### 📁 Stylesheet Breakdown

* **theme.css**
  Global core styles
  Defines Light/Dark mode variables and toast notification styles

* **style1.css — Home**
  Hero sections with parallax effects
  High-curvature product cards (32px radius)

* **style2.css — Shop / Catalog**
  Sidebar filters
  Price range sliders
  Pagination controls

* **style3.css — Product Detail**
  Interactive image galleries
  Thumbnail switching
  Size-selection pills

* **style8.css — Authentication**
  Animated login/signup tab switching
  Clean form transitions

* **style11.css — User Profile**
  Dashboard sidebar layout
  Order history tables
  Status badges

* **style5.css & style6.css — Cart & Checkout**
  Flexbox-based cart layouts
  Sticky order summary panel

---

## ⚡ Interactive Logic (`/static/js`)

Vanilla JavaScript powers the **interactive and dynamic behavior** of the UI, bridging frontend components with the backend API.

---

### 🔌 `api.js` — API Communication Layer

* Securely retrieves **CSRF token** from cookies
* Handles AJAX-based “Add to Cart”
* Updates cart data without page reload
* Ensures secure POST requests

---

### 🎯 `main.js` — UI & UX Engine

#### 🌓 Theme Engine

* Handles Light/Dark mode switching
* Persists preference using `localStorage`
* Applies changes instantly across the UI

#### ✨ Scroll Reveal Animations

* Uses **IntersectionObserver**
* Animates products and sections on viewport entry
* Improves visual engagement

#### 🍞 Toast Notification System

* WhatsApp-style slide-in toasts
* Success & error feedback for user actions
* Non-intrusive and theme-aware

#### 🔐 Auth Helpers

* Password visibility toggle
* Login/Signup tab switching
* Smooth authentication UX

---

## 🌓 Dark Mode Implementation

The project uses a **data-attribute-based theming strategy**.

### 🌗 How It Works

* Theme toggle applies a `data-theme` attribute to the `<body>`
* CSS variables are overridden dynamically
* No DOM re-rendering required

This approach ensures:

* Instant theme switching
* Clean and maintainable CSS
* Consistent behavior across components

---

## 🚀 Getting Started

### 🧰 Environment Setup

* Docker environment running
* PostgreSQL configured
* Django backend active

### 🔗 API Access

* Visit `/api/products/` to explore browsable API endpoints

### 🎨 Static Assets

* Ensure all **11 CSS files** and **2 JavaScript files** are available in the `static/` directory
* Required for correct UI rendering and interactions

---

## ✨ Key UI Components

### 🛠 Floating Admin Button

* Quick-access dashboard shortcut
* Appears conditionally for admins
* Automatically adapts to Light/Dark themes

---

### 📦 Order Status Badges

* Color-coded indicators:

  * Pending
  * Shipped
  * Delivered
* Visible in user profile dashboard
* Improves order clarity at a glance

---

### 💬 WhatsApp-Style Toasts

* Slide-in notifications
* Used for:

  * Cart updates
  * Success messages
  * Error alerts
* Enhances real-time feedback

---

## ✅ Why This Architecture Works

* Clean API-first design
* Modular and scalable CSS system
* Real-time UX without frameworks
* Secure and privacy-focused backend
* Production-grade UI patterns

This full-stack store application demonstrates **industry-ready design thinking**, combining **robust backend engineering** with a **polished frontend experience**.

---
