import datetime

def getWeekday(dt):
    # 日曜日1~土曜日7に変換。isoweekday は月曜日1~日曜日7だから。
    weekday = (dt.isoweekday() + 1) % 7
    return 7 if weekday == 0 else weekday

def skipOrderItems(queryLine, kindOfOrderItem):
    return queryLine + int(kindOfOrderItem)


def handleOrder(querys, queryLine, timestamp, shipFlags, availableShip, itemAvailableShip, orders):
    orderId, shipDate, kindOfOrderItem = querys[queryLine].split()
    queryLine += 1

    # check weekday of available ship
    dtShipDate = datetime.datetime.strptime(shipDate, '%Y-%m-%d')
    weekdayOfShip = getWeekday(dtShipDate)
    if shipFlags[weekdayOfShip-1] == 0:
        print(f"{timestamp} Ordered {orderId} Error: the number of available shipments has been exceeded.")
        queryLine = skipOrderItems(queryLine, kindOfOrderItem)
        return queryLine
    
    # check number of available ship
    ## 発送が入っていない日付だった場合発送可能数の上限をセット
    if shipDate not in availableShip:
        availableShip[shipDate] = itemAvailableShip.copy()

    orderItems = {}
    canShipAllItems = True
    ## check all items can be shiped
    for _ in range(int(kindOfOrderItem)):
        itemId, amount = querys[queryLine].split()
        amount = int(amount)

        if availableShip[shipDate][itemId] < amount:
            canShipAllItems = False
            
        orderItems[itemId] = amount
        queryLine += 1
    ## update available ship 
    if canShipAllItems:
        for itemId, amount in orderItems.items():
            availableShip[shipDate][itemId] -= amount
        orders[orderId] = {'shipDate': shipDate, 'items': orderItems.copy(), 'isShiped': False}
        print(f"{timestamp} Ordered {orderId}")
    else:
        print(f"{timestamp} Ordered {orderId} Error: the number of available shipments has been exceeded.")

    return queryLine