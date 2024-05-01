# 1. Setup the project
1. Project created with 3.12.3
2. git clone https://github.com/Exile404/Vendor_Management_System.git
3. pip install -r requirements.txt

# 2. Run the testcase using tests.py

    --> Run: 
    python manage.py test vendor_management.tests

# 3. Test using Postman
    Run the following command at beginning: 
    python manage.py runserver

1.  To add a new vendor\
    a) url: http://127.0.0.1:8000/api/vendors \
    b) METHOD: POST \
    c) JSON:\
        {\
    "name": "Example Vendor3",\
    "contact_details": "example2@example.com",\
    "address": "123 Example St",\
    "vendor_code": "VENDOR002"\
    }

2.  To get all information of vendors\
    a) url: http://127.0.0.1:8000/api/vendors \
    b) METHOD: GET

3.  To get all information of  one vendor\
    a) url: http://127.0.0.1:8000/api/vendors/{vendor_id} \
    b) METHOD: GET

4.  To update a vendor information\
    a) url: http://127.0.0.1:8000/api/vendors/{vendor_id} \
    b) METHOD: PUT\
    c) JSON:\
        {\
        "name": "Updated Vendor Name",\
        "contact_details": "updated@example.com",\
        "address": "456 Updated St",\
        "vendor_code": "VENDOR003"\
        }

5. To delete all information of one vendor\
    a) url: http://127.0.0.1:8000/api/vendors/{vendor_id} \
    b) METHOD: GET
    
6.  Add a new purchase order\
    a) url: http://127.0.0.1:8000/api/purchase_orders \
    b) METHOD: POST \
    c) JSON:\
        {\
    "po_number": "PO001",\
    "vendor": "1",\
    "order_date": "2024-05-01T12:00:00Z",\
    "delivery_date": "2024-05-10T12:00:00Z",\
    "items": [{"name": "Item 1", "quantity": 5}],\
    "quantity": 5,\
    "status": "pending"\
    }

7.  To get all information of all purchases\
    a) url: http://127.0.0.1:8000/api/purchase_orders \
    b) METHOD: GET

8.  To get all information of one purchase\
    a) url: http://127.0.0.1:8000/api/purchase_orders/{purchase_id} \
    b) METHOD: GET

9.  To update the status of a purchase\
    a) url: http://127.0.0.1:8000/api/purchase_orders/{purchase_id} \
    b) METHOD: PUT\
    c) JSON:\
        {\
        "po_number": "PO001",\
        "vendor": "3",  \
        "delivery_date": "2024-05-10T12:00:00Z",\
        "items": [{"name": "Item 1", "quantity": 5}],\
        "quantity": 5,\
        "status": "completed",\
        "quality_rating": 4.5\
        }

10. To acknowledge a Purchase Order\
    url: http://localhost:8000/api/purchase_orders/{purchase_id}/acknowledge \
    METHOD: PUT

11. To get a vendor's performance rating\
    url: http://localhost:8000/api/vendors/{vendor_id}/performance \
    METHOD: GET
