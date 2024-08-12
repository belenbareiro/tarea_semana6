from ownable import set_owner


class Cart:
    from item_manager import show_items

    def __init__(self, owner):
        set_owner(self, owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Not enough funds to complete the purchase.")
            return False
        total_item_cost = self.total_amount()
        self.owner.wallet.withdraw(total_item_cost)
        # Process each item in the cart
        for item in self.items_list():
            # Transfer money from cart owner's wallet to item owner's wallet
            print("💰 Transfering " + str(total_item_cost) + " to " + item.owner.name)
            item.owner.wallet.deposit(total_item_cost)
            break

        for item in self.items_list():
            # Transfer ownership of the item
            item.owner = self.owner

        # Clear the cart after checkout
        self.items.clear()
        print("Checkout successful. Cart is now empty.")
        print("✅ Purchase confirmed")
        return True
