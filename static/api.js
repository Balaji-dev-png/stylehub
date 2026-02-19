// Function to get Django CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// 1. ADD TO CART LOGIC
document.querySelectorAll('.add-cart, .add-to-cart-btn').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Ensure your HTML buttons have a data-id attribute: <button data-id="{{ product.id }}">
        const productId = this.getAttribute('data-id'); 
        
        fetch('/api/cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'product_id': productId,
                'quantity': 1
            })
        })
        .then(response => {
            if (response.status === 403) {
                alert("Please login to add items to cart.");
                window.location.href = "/login/";
            }
            return response.json();
        })
        .then(data => {
            if(data.message) {
                // Update badge using the main.js logic you already have
                const badge = document.querySelector('.badge');
                if(badge) badge.innerText = data.cart_total;
                alert("Item added!");
            }
        });
    });
});

// 2. SEARCH LOGIC
const searchForm = document.querySelector('.search-form');
if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const query = this.querySelector('input').value;

        fetch(`/api/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            console.log("Search Results:", data);
            // Logic to render these results dynamically 
            // OR simply redirect to a Django search results page:
            // window.location.href = `/shop/?search=${query}`;
        });
    });
}