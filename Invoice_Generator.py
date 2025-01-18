from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email,
                 invoice_date):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.date = invoice_date

        # internally determined variables
        self.cost = 0
        self.items = []
        self.comments = []  # Stores comments related to the invoice

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            total += price + (price * tax)
        # Apply discount as a percentage
        total_after_discount = total * (1 - discount / 100)
        return total_after_discount

    def add_comment(self, comment):
        # Add a comment to the invoice.
        self.comments.append(comment)

    def view_comments(self):
        return "\n".join(self.comments)

    def display_invoice(self, discount):
        print()
        print("============ INVOICE ============")
        print()
        print("Invoice Date:", self.date.strftime("%Y-%m-%d"))
        print("\nSender Details:")
        print(f"Name: {self.sender_name}")
        print(f"Address: {self.sender_address}")
        print(f"Email: {self.sender_email}\n")

        print("Recipient Details:")
        print(f"Name: {self.recipient_name}")
        print(f"Address: {self.recipient_address}")
        print(f"Email: {self.recipient_email}\n")

        print("Item Details:")
        for item in self.items:
            print(f"Name: {item['name']}, Price: {item['price']}, Tax: {item['tax']}")

        print("\nComments:")
        print(self.view_comments())

        print(f"\nTotal after discount ({discount}%): {self.calculate_total(discount)}")


# Main Program
if __name__ == '__main__':
    # Get the invoice date from the user
    invoice_date_input = input("Enter the invoice date (DD-MM-YYYY): ")
    invoice_date = datetime.strptime(invoice_date_input, "%d-%m-%Y")

    # Get sender details
    sender_name = input("Enter the sender's name: ")
    sender_address = input("Enter the sender's address: ")
    sender_email = input("Enter the sender's email: ")

    # Get recipient details
    recipient_name = input("Enter the recipient's name: ")
    recipient_address = input("Enter the recipient's address: ")
    recipient_email = input("Enter the recipient's email: ")

    invoice = Invoice(
        sender_name,
        recipient_name,
        sender_address,
        recipient_address,
        sender_email,
        recipient_email,
        invoice_date
    )

    # Add items to the invoice
    while True:
        item_name = input("Enter the item/property name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input("Enter the price of the item: "))
        item_tax = float(input("Enter the tax of the item (as a decimal): "))
        invoice.add_item(item_name, item_price, item_tax)

    # Add comments to the invoice
    while True:
        comment = input("Enter a comment (or type 'done' to finish): ")
        if comment.lower() == 'done':
            break
        invoice.add_comment(comment)

    # Display the final invoice
    discount = float(input("Enter the discount percentage: "))
    invoice.display_invoice(discount)

