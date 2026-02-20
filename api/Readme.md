🛒 Store API ModuleThis module handles the data transformation and logic for the e-commerce store, utilizing Django REST Framework (DRF) to provide a robust, scalable API.

📋 FeaturesAutomated Serialization: Converts complex Product, Cart, and Order models into JSON for client-side consumption.
Restricted Access: Implements IsAuthenticatedOrReadOnly to ensure public visibility for products while protecting sensitive data.
User-Specific Queries: The Order system is filtered at the database level so users can only view and manage their own history.

🛠 Technical Overview1.

 Serializers (serializers.py)
 The serializers act as the bridge between your PostgreSQL database and the frontend.
 ProductSerializer: Exposes all product details including price, description, and stock.
 CartSerializer: Manages temporary session-based or user-linked shopping carts.
 OrderSerializer: Handles the final checkout data.
 
 2. ViewSets (views.py)
 
 We use ModelViewSet to provide standard CRUD (Create, Retrieve, Update, Delete) actions automatically.
 EndpointMethodPermissionDescription/api/products/GETPublicView all available products./api/products/POSTAdminAdd new products to the store./api/orders/GETUserView only your past orders./api/orders/POSTUserPlace a new order.
 🔐 Security Logic:
  Order IsolationTo prevent data leaks, the OrderViewSet overrides the default get_queryset method.
 
 Python
 def get_queryset(self):
    # Ensures that even if an ID is guessed, 
    # a user can't see someone else's order.
    return Order.objects.filter(user=self.request.user)
🚀 Getting StartedEnsure your Docker containers (Postgres & Django) are running.Navigate to http://localhost:8000/api/products/ to view the browsable API.Use a Bearer Token or Session Auth to access the /orders/ endpoint. 

api    readme file