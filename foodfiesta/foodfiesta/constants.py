

#Order
PENDING   = 0
ACCEPTED  = 1
REJECTED  = 2
DELIVERED = 3
PLACED    = 4
PREPARED  = 5
# 
ORDER_STATUS =(
    (PENDING,'Pending'),
    (ACCEPTED,'Accepted'),
    (REJECTED,'Rejected'),
    (PLACED,'Placed'),
    (DELIVERED,'Delivered'),
    (PREPARED,'Prepared')
    )
#Delivery Person

AVAILABLE     = True
NOT_AVAILABLE = False

DELIVERY_STATUS = (
    (AVAILABLE,'Available'),
    (NOT_AVAILABLE,'Not Available'),
)

#Restaurant 

OPEN  = True
CLOSE = False

OPEN_STATUS = (
    (OPEN,'Open'),
    (CLOSE,'Close'),
)

ACTIVE   = True
DEACTIVE = False

ACTIVE_STATUS = (
    (ACTIVE,'Active'),
    (DEACTIVE,'Deactive'),
)

REQUEST_STATUS =(
    
    (PENDING,'Pending'),
    (ACCEPTED,'Accepted'),
    (REJECTED,'Rejected'),
    ) 
