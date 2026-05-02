import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", required=False, type=float)

args = parser.parse_args()

if not validate_side(args.side):
    print("ERROR: Invalid side. Use BUY or SELL")

elif not validate_order_type(args.type):
    print("ERROR: Invalid order type. Use MARKET or LIMIT")

elif not validate_quantity(args.quantity):
    print("ERROR: Quantity must be greater than 0")

elif not validate_price(args.price, args.type):
    print("ERROR: Price is required and must be greater than 0 for LIMIT order")

else:
    result = place_order(args.symbol, args.side, args.type, args.quantity, args.price)

    print("\n----- ORDER REQUEST SUMMARY -----")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)
    if args.price:
        print("Price:", args.price)

    print("\n----- ORDER RESPONSE DETAILS -----")

    if "error" in result:
        print("FAILED:", result["error"])
    else:
        print("Order ID:", result.get("orderId"))
        print("Status:", result.get("status"))
        print("Executed Qty:", result.get("executedQty"))
        print("Average Price:", result.get("avgPrice"))
        print("SUCCESS: Order placed successfully")