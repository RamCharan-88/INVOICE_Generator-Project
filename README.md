# Invoice Generator

A Python console application for managing and generating invoices. The application allows for the addition of multiple items, tax calculations, discounts, and comments. It generates a detailed invoice breakdown that can be displayed.

## Features

- **Sender and Recipient Details:** Input and store details for both sender and recipient.
- **Item Management:** Add items with their prices and tax rates.
- **Comment Section:** Add and view comments related to the invoice.
- **Discount Application:** Apply discounts to the total amount.
- **Detailed Invoice Display:** View a complete invoice with all entered details and calculations.

## Usage

To use the application, run the script and follow the prompts to enter the required information.

### Example

```python
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
