/* static/main.js */

document.addEventListener('DOMContentLoaded', function () {

    // ==============================================
    // 1. SCROLL REVEAL ANIMATION (Intersection Observer)
    // ==============================================

    const observerOptions = {
        root: null,
        rootMargin: '0px', // Trigger exactly when element enters viewport
        threshold: 0.1     // Trigger when 10% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add the class that triggers the CSS transition
                entry.target.classList.add('is-visible');
                // Stop observing this element (animate only once)
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Attach observer to all elements with the 'reveal-on-scroll' class
    const scrollElements = document.querySelectorAll('.reveal-on-scroll');
    scrollElements.forEach((el) => {
        observer.observe(el);
    });


    // ==============================================
    // 2. AJAX ADD TO CART LOGIC
    // ==============================================

    const addToCartBtns = document.querySelectorAll('.ajax-add-to-cart');

    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault(); // Stop the browser from navigating to the URL

            const url = this.getAttribute('href'); // Get the Django URL from the <a> tag

            // Optional: Visual feedback on button (e.g., slight opacity change)
            this.style.opacity = '0.7';

            fetch(url, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Marks request as AJAX for Django
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    // Reset button style
                    this.style.opacity = '1';

                    // Check if Django redirected (e.g., if user wasn't logged in)
                    if (response.redirected) {
                        window.location.href = response.url; // Manually follow redirect
                        return null;
                    }
                    return response.json();
                })
                .then(data => {
                    if (data && data.status === 'success') {
                        // A. Update the Cart Badge Count in Navbar
                        const badges = document.querySelectorAll('.badge, .cart-badge');
                        badges.forEach(b => b.innerText = data.cart_count);

                        // B. Show Success Toast Notification
                        showToast(data.message);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    this.style.opacity = '1';
                });
        });
    });

    // Helper Function: Create and Show Toast
    function showToast(message) {
        // Check if container exists, if not create it
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        // Create the toast element
        const toast = document.createElement('div');
        toast.className = 'toast toast-success';

        // Add content (Message + Close Button)
        toast.innerHTML = `
            <span>${message}</span>
            <span class="toast-close" style="margin-left:15px; cursor:pointer;">&times;</span>
        `;

        // Add close functionality
        toast.querySelector('.toast-close').onclick = function () {
            removeToast(toast);
        };

        // Append to container (triggers CSS animation)
        container.appendChild(toast);

        // Auto remove after 3 seconds
        setTimeout(() => {
            removeToast(toast);
        }, 3000);
    }

    function removeToast(toast) {
        toast.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (toast.parentElement) toast.remove();
        }, 500);
    }


    // ==============================================
    // 3. THEME TOGGLE (Dark/Light Mode)
    // ==============================================

    const themeToggleBtn = document.getElementById('theme-toggle');

    // Check Local Storage on load
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        document.body.setAttribute('data-theme', currentTheme); // Kept for backwards compatibility
        if (themeToggleBtn && currentTheme === 'dark') {
            themeToggleBtn.innerText = '☀️';
        }
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            let theme = document.documentElement.getAttribute('data-theme');
            if (theme === 'dark') {
                document.documentElement.removeAttribute('data-theme'); // Switch to Light
                document.body.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
                themeToggleBtn.innerText = '🌙';
            } else {
                document.documentElement.setAttribute('data-theme', 'dark'); // Switch to Dark
                document.body.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                themeToggleBtn.innerText = '☀️';
            }
        });
    }


    // ==============================================
    // 4. GLOBAL HELPERS (Auth & Password)
    // ==============================================

    // Toggle Password Visibility (used in auth.html)
    window.togglePassword = function (fieldId, btn) {
        const input = document.getElementById(fieldId);
        if (input.type === "password") {
            input.type = "text";
            btn.innerText = "🙈";
        } else {
            input.type = "password";
            btn.innerText = "👁️";
        }
    };

    // Toggle Login/Signup Tabs (used in auth.html)
    window.toggleAuth = function (tabName) {
        const loginForm = document.getElementById('login-form');
        const signupForm = document.getElementById('signup-form');
        const btns = document.querySelectorAll('.tab-btn');

        // Remove active class from all buttons
        btns.forEach(b => b.classList.remove('active'));

        if (tabName === 'login') {
            loginForm.classList.add('active');
            signupForm.classList.remove('active');
            if (btns[0]) btns[0].classList.add('active');
        } else {
            signupForm.classList.add('active');
            loginForm.classList.remove('active');
            if (btns[1]) btns[1].classList.add('active');
        }
    };

    // ==============================================
    // 5. PAGE TRANSITION ANIMATION
    // ==============================================

    // Start Enter Animation immediately
    document.body.classList.add('page-enter-active');

    // Remove the enter animation class after it completes (500ms)
    // This is CRITICAL because the CSS 'transform' property on the body
    // breaks 'position: fixed' for children elements like the floating admin button!
    setTimeout(() => {
        document.body.style.opacity = '1'; // Lock opacity so it doesn't vanish
        document.body.classList.remove('page-enter-active');
    }, 550); // slight buffer past 500ms css duration

    // Intercept internal link clicks to trigger exit animation
    const allLinks = document.querySelectorAll('a[href]:not([target="_blank"])');

    allLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');

            // Only animate for absolute/relative internal URLs, ignore hashes or external links
            if (href && !href.startsWith('#') && !href.startsWith('mailto:') && !href.startsWith('tel:') && !this.classList.contains('ajax-add-to-cart')) {
                const targetUrl = this.href;
                const currentOrigin = window.location.origin;
                const targetOrigin = new URL(targetUrl, currentOrigin).origin;

                if (currentOrigin === targetOrigin) {
                    e.preventDefault(); // Stop immediate navigation

                    // Add the exit animation class
                    document.body.classList.add('page-exit-active');

                    // Wait for the CSS transition duration before navigating
                    setTimeout(() => {
                        window.location.href = href;
                    }, 400); // 400ms matches the CSS animation duration
                }
            }
        });
    });

});