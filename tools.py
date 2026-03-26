# tools.py
def get_order_status(order_id):
    fake_db = {
        "123": "Shipped",
        "456": "Out for delivery"
    }
    return fake_db.get(order_id, "Order not found")