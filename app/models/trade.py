class Trade:
    def __init__(self, trade_id, symbol, quantity, price, trade_type, timestamp):
        self.trade_id = trade_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type
        self.timestamp = timestamp

    def __repr__(self):
        return f"<Trade {self.trade_type} {self.quantity} {self.symbol} @ {self.price}>"
