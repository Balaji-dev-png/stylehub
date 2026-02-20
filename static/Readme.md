🛒 Full-Stack Store Application

A modern, responsive e-commerce platform built with Django REST Framework and a custom Modular Design System. This project features a seamless user experience with real-time cart updates, dark mode persistence, and secure order management.

📂 Project Architecture

1. Backend API (/api)
The backend is built using Django REST Framework (DRF) to handle data serialization and secure view logic.

Serializers (serializers.py): Utilizes ModelSerializer to convert Product, Order, and Cart models into JSON.
ViewSets (views.py): Implements ModelViewSet for standard CRUD operations.
Security: Uses IsAuthenticatedOrReadOnly to protect data, ensuring users can only access their own specific orders via custom get_queryset filtering.

2. Design System (/static/css)

The UI is built on a custom CSS variable engine that supports instant theme switching.
ModulePurposeFeaturestheme.cssGlobal CoreDefines the master CSS variables for Light/Dark modes and global toast styles.style1.cssHome PageHigh-curvature product cards (32px radius) and hero parallax effects.style2.cssShop/CatalogSidebar filters, price range sliders, and pagination controls.style3.cssProduct DetailInteractive image galleries with thumbnail switching and size-selection pills.style8.cssAuth (Login/Reg)Animated tab switching for login/signup forms and social login integration.style11.cssUser ProfileDashboard sidebar, order history tables with status badges, and settings forms.style5.css & style6.cssCart & CheckoutFlexbox-based cart layouts and sticky order summaries for the checkout process.

3. Interactive Logic (/static/js)

Vanilla JavaScript provides the interactive layer, connecting the design to the API.
api.js (Communication):
Retrieves the Django CSRF Token from cookies to secure POST requests.
Handles AJAX "Add to Cart" functionality to update the cart without a page reload.

main.js (UI/UX):
Theme Engine: Manages Dark/Light mode switching and persists preferences in localStorage.
Scroll Reveal: Uses IntersectionObserver to animate elements (products/headers) as they enter the viewport.
Toast System: Provides real-time visual feedback (Success/Error toasts) for user actions.
Auth Helpers: Manages password visibility toggling and form tab switching.

🌓 Dark Mode Implementation

The site utilizes a data-attribute strategy. When the theme is toggled, the data-theme attribute is applied to the body, overriding global variables.

CSS
/* theme.css */
:root { --bg-body: #ffffff; --text-main: #333; }
[data-theme="dark"] { --bg-body: #121212; --text-main: #e0e0e0; }


🚀 Getting Started

Environment: Ensure your Docker environment is running with PostgreSQL and Django.
API Access: Navigate to /api/products/ to view the browsable API endpoints.Static Assets: Ensure all 11 CSS files and 2 JS files are collected in your static/ directory for the UI to render correctly.

✨ Key UI Components

Floating Admin Button: A quick-access dashboard button that adapts its colors based on the current theme.
Order Status Badges: Color-coded status indicators (Pending, Shipped, Delivered) in the User Profile.
WhatsApp-Style Toasts: Clean, slide-in notifications for successful cart additions.


static readme file