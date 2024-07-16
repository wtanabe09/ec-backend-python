
def handleCancel(timestamp, querys, queryLine, availableShip, orders):
    orderId = querys[queryLine]
    queryLine += 1

    cancelOrder = orders.pop(orderId)
    shipDate = cancelOrder['shipDate']
    for itemId, amount in cancelOrder['items'].items():
        availableShip[shipDate][itemId] += amount
    print(f"{timestamp} Canceled {orderId}")

    return queryLine