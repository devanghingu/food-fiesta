# Order
PENDING = 0
ACCEPTED = 1
REJECTED = 2
DELIVERED = 3

ORDER_STATUS = (

    (PENDING, 'Pending'),
    (ACCEPTED, 'Accepted'),
    (REJECTED, 'Rejected'),
    (DELIVERED, 'Delivered'),
)

# Delivery Person

AVAILABLE = True
NOT_AVAILABLE = False

DELIVERY_STATUS = (
    (AVAILABLE, 'Available'),
    (NOT_AVAILABLE, 'Not Available'),
)

# Restaurant

OPEN = True
CLOSE = False

OPEN_STATUS = (
    (OPEN, 'Open'),
    (CLOSE, 'Close'),
)

ACTIVE = True
DEACTIVE = False

ACTIVE_STATUS = (
    (ACTIVE, 'Active'),
    (DEACTIVE, 'Deactive'),
)
