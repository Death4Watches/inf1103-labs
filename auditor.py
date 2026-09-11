inventory = 0
failed_entries = 0

while True:
    inventory_input = input("Enter the Stock Quantity (type quit to leave): ")        

    if inventory_input == "quit" | "Quit":
        print("Final Inventory: " + str(inventory))
        print("Failed Enteries: " + str(failed_entries))
        print("Goodbye!")
        break

    try:
        amount = int(inventory_input)
    except ValueError:
          print("Error: Input does not accept strings")
          failed_entries += 1
          continue

    inventory += int(inventory_input)
    print(inventory)

    if inventory > 500:
            inventory = 500
            
            print("Warning: Inventory exceeds over 500 capacity!\nSet to 500")
            print("Final Inventory: " + str(inventory))
            print("Failed Enteries: " + str(failed_entries))
            print("Goodbye!")
            break
    elif inventory < 0:
            inventory = 0
            
            print("Warning: Inventory exceeds below 0 capacity!\nSet to 0")
            print("Final Inventory: " + str(inventory))
            print("Failed Enteries: " + str(failed_entries))
            print("Goodbye!")
            break