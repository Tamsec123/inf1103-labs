total_inventory = 0
rejected_entries = 0

while True:
    entry = input("Enter stock quantity (or type 'quit' to finish): ")
    if entry.lower() == 'quit':
        break
    if not entry.isdigit():
        print("Invalid entry. Please enter a valid number.")
        rejected_entries += 1
        continue
    quantity = int(entry)
    total_inventory += quantity
        
print(f"Total inventory: {total_inventory}")
print(f"Rejected entries: {rejected_entries}")