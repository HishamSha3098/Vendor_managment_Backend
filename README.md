# Vendor Management System with Performance Metrics
This Django-based Vendor Management System (VMS) handles vendor profiles, purchase order tracking, and calculates performance metrics.

# Setup
Clone the Repository:


git clone https://github.com/your-username/vendor-management-system.git
Navigate to the Project Directory:


cd vendor-management-system
Create and Activate Virtual Environment:

python -m venv venv
source venv/bin/activate   # For Linux/Mac
# or
.\venv\Scripts\activate    # For Windows
Install Dependencies:

pip install -r requirements.txt
Apply Migrations:

python manage.py migrate
Run the Development Server:


python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/api/.

# API Endpoints
Vendors:

Create: POST /api/vendors/
List: GET /api/vendors/
Retrieve: GET /api/vendors/{vendor_id}/
Update: PUT /api/vendors/{vendor_id}/
Delete: DELETE /api/vendors/{vendor_id}/
Purchase Orders:

Create: POST /api/purchase_orders/
List: GET /api/purchase_orders/
Retrieve: GET /api/purchase_orders/{po_id}/
Update: PUT /api/purchase_orders/{po_id}/
Delete: DELETE /api/purchase_orders/{po_id}/
Vendor Performance:

Metrics: GET /api/vendors/{vendor_id}/performance

# Backend Logic for Performance Metrics
On-Time Delivery Rate:

Calculated on PO status change to 'completed'.
Quality Rating Average:

Updated on completion of each PO with a quality rating.
Average Response Time:

Calculated on PO acknowledgment.
Fulfilment Rate:

Calculated on any PO status change.

# Technical Requirements

Django and Django REST Framework
RESTful API design
Django ORM for database interactions
Token-based authentication
PEP 8 style guidelines

# Test Suite
Run the test suite with:


python manage.py test

# Submission Guidelines

Host on GitHub or [GitLab].
Provide clear setup instructions in README.
Include details on API endpoints and backend logic.
