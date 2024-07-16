def handleShip(timestamp, orders):
    date = timestamp.split("T")[0]
    orderIds = []
    shipCount = 0

    for orderId, orderDetails in orders.items():
        if orderDetails['shipDate'] == date:
            orders[orderId]['isShiped'] = True
            orderIds.append(orderId)
            shipCount += 1

    print(f"{timestamp} Shipped {shipCount} Orders")
    print(" ".join(orderIds))

    return