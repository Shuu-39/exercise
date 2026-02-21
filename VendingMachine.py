class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0

        self.balance = 0
                 
    def restock(self, amount):
        assert amount >= 0 , "Input can't be minus!"
        self.stock += amount
        return f'Current {self.product} stock: {self.stock}'
    
    def add_funds(self, amount):
        assert amount >= 0 , "Input can't be minus!"
        if self.stock > 0:
            self.balance += amount
            return f'Current balance: ${self.balance}'
        elif self.stock == 0:
            return f'Nothing left to vend. Please restock. Here is your ${amount}.'

    def vend(self):
        if self.stock == 0:
            return f'Nothing left to vend. Please restock.'
        else:
            if self.balance < self.price:
                return f'Please add ${self.price - self.balance} more funds.'
            else:
                change = self.balance - self.price
                self.stock -= 1       # 库存减1
                self.balance = 0      # 余额清零
                if change == 0:
                    return f'Here is your {self.product}.'
                else:
                    return f'Here is your {self.product} and ${change} change.'