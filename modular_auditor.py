def get_valid_input():
    while True:
        stock_quantity = input("Enter the Stock Quantity: ")
    
        if stock_quantity == "quit":
            return "quit", True
        try:
            quantity = int(stock_quantity)
            return quantity, True
        except ValueError:
            print("Error: Input does not accept strings")
            return None, False
        
    
def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):

    return amount * 0.1

def generate_report(total_units, failed_attempts):
    print("---- Final Summary ----")
    print("Total Delieveries Processed: " + str(total_units))
    print("Number of Failed Entries: " + str(failed_attempts))


def main():
    final_inventory = 0
    invalid_inventory = 0
    tax = 0

    while True:

        result, ok = get_valid_input()

        if result == "quit":
            print(generate_report(final_inventory, invalid_inventory))
            print("Goodbye!")
            break
        elif not ok:
            invalid_inventory += 1
            continue

        print("Input Value: " + str(result))

        final_inventory = process_delivery(final_inventory, result)
        print("New Total: " + str(final_inventory))

        tax = calculate_tax(final_inventory)
        print("Tax (SGD): $" + str(tax))


if __name__ == "__main__":
    main()