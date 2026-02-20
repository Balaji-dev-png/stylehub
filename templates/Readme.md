🛍️ Stylehub: The Templates Engine
This directory contains the 19 HTML templates that form the frontend of the Stylehub e-commerce platform. These files utilize the Django Template Language (DTL) to create a dynamic, secure, and highly interactive user experience.

📂 Template Architecture
The frontend is built on a Modular Page Strategy, where each template is paired with a specific stylesheet (from static/css) to ensure optimal performance and design consistency.

1. 🏠 Marketing & Discovery
These pages are designed for high conversion and brand storytelling.

home.html: The landing page featuring a hero section, featured product grids, and scroll-reveal animations.

pro_list.html: A comprehensive shop catalog with interactive JavaScript-driven filtering (by category, price range, and size) and pagination.

pro_detail.html: A deep-dive product view featuring high-fidelity image galleries, size selection, and real-time "next day delivery" timers.

new_arrivals.html: A focused landing page for the latest collection drops, utilizing "Quick Add" slide-up buttons.

search_result.html: A dynamic results page that handles empty states gracefully with "No matches found" UI.

about.html: Showcases the brand's mission and the core team members.

2. 🛒 Commerce & Checkout
The logic-heavy templates that handle the transition from browsing to buying.

cart.html: A detailed view of the user's current selections with itemized sub-totals.

checkout.html: A multi-step form for contact info, shipping address, and randomized Payment Simulation logic.

success.html: A professional order confirmation page featuring a receipt-style box and animated checkmark.

3. 👤 User Experience & Account
Secure templates for managing personal data and preferences.

auth.html: A unified, tabbed interface for seamless switching between Login and Signup forms.

profile.html: The user control center for updating shipping details and viewing recent order history.

my_orders.html: A specialized dashboard where users can track the status (Pending, Shipped, Delivered) of their purchases and cancel pending orders.

wishlist.html: A personalized gallery of saved items, featuring a "Quick Remove" heart button.

4. 🔑 Security & Password Recovery
A complete suite for user credential management.

password_reset.html: The starting point for account recovery.

password_reset_done.html: Confirmation that instructions have been sent.

password_reset_confirm.html: The secure form to set a new password.

password_reset_complete.html: The final "Success" notification before redirecting to login.

🛠️ Key Technical Features
🌓 Theme Engine Integration
Every template is fully compatible with the global Dark/Light Mode switch. The theme-toggle in the navbar interacts with main.js to flip CSS variables across all components instantly.

🍞 Dynamic Feedback System
We use the Django Messages Framework integrated into the templates to show:

Success Toasts: For "Item Added to Cart" or "Profile Updated".

Error Alerts: For "Payment Failed" or "Invalid Credentials".

🚀 Performance UI
Intersection Observer: Templates use the reveal-on-scroll class to trigger smooth entry animations for sections and cards.

AJAX Ready: The ajax-add-to-cart class allows users to shop without the page refreshing, updating the global badge count in real-time.

🗺️ Template Global Helper: Context Processor
The cart_count variable seen in all navbar snippets is powered by a custom Context Processor. This ensures that whether a user is on the home page or the contact page, their shopping cart badge is always accurate and up-to-date.


templates readme file