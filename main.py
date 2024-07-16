import sys

from cancel_order import handleCancel
from order import handleOrder
from ship import handleShip

def initializeAvailableShip(items, numOfAvailableShip):
    itemAvailableShip = {item: numOfAvailableShip for item in items}
    return {}, itemAvailableShip

def main(lines):
    # interpret basic information
    kindsOfItem, numOfAvailableShip, maxDateOfShip = list(map(int, lines[0].split()))
    items = lines[1].split()
    shipFlags = list(map(int, lines[2].split()))
    numOfQuery = int(lines[3])
    querys = lines[4:]
    queryLine = 0

    # create data base
    availableShip, itemAvailableShip = initializeAvailableShip(items, numOfAvailableShip)
    orders = {}
    
    # handle command
    for _ in range(numOfQuery):
        command, timestamp = querys[queryLine].split()
        queryLine += 1
        if command == "ORDER":
            queryLine = handleOrder(querys, queryLine, timestamp, shipFlags, availableShip, itemAvailableShip, orders)
        elif command == "CANCEL":
            queryLine = handleCancel(timestamp, querys, queryLine, availableShip, orders)
        elif command == "SHIP":
            handleShip(timestamp, orders)
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
