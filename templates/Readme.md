## 🛍️ StyleHub — Templates Engine

This directory contains **19 structured HTML templates** that form the **entire frontend layer** of the StyleHub e-commerce platform.
All templates are built using **Django Template Language (DTL)** to deliver a **dynamic, secure, and highly interactive user experience**.

---

## 🧱 Template Architecture

The frontend follows a **Modular Page Strategy**:

* Each template is mapped to a **specific stylesheet**
* CSS is loaded **page-wise** from `static/css`
* Ensures design consistency and optimal performance
* Prevents unnecessary asset loading

This approach keeps the UI **lightweight, scalable, and easy to maintain**.

---

## 📂 Template Categories

---

### 🏠 Marketing & Discovery

These pages focus on **brand presence, engagement, and product discovery**.

* **home.html**
  Landing page with hero sections, featured product grids, and scroll-reveal animations

* **pro_list.html**
  Full shop catalog with JavaScript-driven filtering
  (category, price range, size) and pagination

* **pro_detail.html**
  Product deep-dive view featuring:

  * Image galleries
  * Size selection
  * Real-time “next-day delivery” timers

* **new_arrivals.html**
  Highlight page for new collections
  Includes “Quick Add” slide-up actions

* **search_result.html**
  Dynamic results handling with clean empty-state UI
  (“No matches found” feedback)

* **about.html**
  Brand story, mission statement, and team showcase

---

### 🛒 Commerce & Checkout

Templates responsible for **converting interest into purchases**.

* **cart.html**
  Detailed cart view with:

  * Item breakdown
  * Quantity control
  * Sub-total calculations

* **checkout.html**
  Multi-step checkout flow including:

  * Contact information
  * Shipping address
  * Randomized payment simulation logic

* **success.html**
  Order confirmation page with:

  * Receipt-style layout
  * Animated success indicator

---

### 👤 User Experience & Account

Secure pages for **personal data and order management**.

* **auth.html**
  Unified login & signup interface
  Tab-based switching for seamless authentication

* **profile.html**
  User control center for:

  * Updating shipping details
  * Viewing recent orders

* **my_orders.html**
  Order tracking dashboard displaying:

  * Pending
  * Shipped
  * Delivered
    Includes cancellation for pending orders

* **wishlist.html**
  Personalized saved-items gallery
  One-click “Quick Remove” heart button

---

### 🔑 Security & Password Recovery

Complete credential-management workflow.

* **password_reset.html**
  Initiates account recovery

* **password_reset_done.html**
  Confirms reset instructions were sent

* **password_reset_confirm.html**
  Secure password update form

* **password_reset_complete.html**
  Final success screen before login redirect

---

## 🛠️ Key Technical Features

---

### 🌓 Theme Engine Integration

* All templates support **Light & Dark Mode**
* Navbar toggle interacts with `main.js`
* CSS variables update instantly across components
* Theme preference persists across sessions

---

### 🍞 Dynamic Feedback System

Integrated with the **Django Messages Framework** to provide real-time user feedback.

* **Success Messages**

  * Item added to cart
  * Profile updated

* **Error Messages**

  * Payment failure
  * Invalid login credentials

Messages are styled as clean, non-intrusive alerts.

---

### 🚀 Performance-Focused UI

* **Scroll-Reveal Animations**

  * Powered by Intersection Observer
  * Smooth entry effects for sections and cards

* **AJAX-Ready Components**

  * `ajax-add-to-cart` enables shopping without refresh
  * Global cart badge updates in real time

---

## 🌍 Global Template Helper — Context Processor

The **cart_count** variable visible in the navbar is powered by a **custom context processor**.

* Injected into every template
* Always reflects real-time cart size
* Eliminates repetitive logic in views
* Ensures consistent UX across all pages

---

## ✅ Why This Template Engine Matters

* Clean separation of UI concerns
* Performance-optimized asset loading
* Real-world e-commerce UX patterns
* Fully theme-aware and interactive
* Easy to scale and extend

This layer transforms StyleHub from a backend project into a **polished, user-ready product**.

---
