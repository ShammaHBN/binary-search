# Function to perform binary search for a chocolate based on specified criteria (price or weight)
def binary_search(chocolates, target, criteria):
    # Initialize the search interval
    low = 0
    high = len(chocolates) - 1

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2
        if chocolates[mid][criteria] == target:
            return mid  # Return the index of the chocolate if found
        elif chocolates[mid][criteria] < target:
            low = mid + 1  # Update the lower bound
        else:
            high = mid - 1  # Update the upper bound

    return -1  # Return -1 if the chocolate is not found


# Test case 1: Searching for a chocolate by weight
chocolates_1 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
target_weight = 30
index_1 = binary_search(chocolates_1, target_weight, criteria=1)
print("Chocolate with weight", target_weight, "found at index:", index_1)

# Test case 2: Searching for a chocolate by price
chocolates_2 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
target_price = 1
index_2 = binary_search(chocolates_2, target_price, criteria=2)
print("Chocolate with price", target_price, "found at index:", index_2)

# Test case 3: Searching for a chocolate that does not exist
chocolates_3 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
target_not_exist = 35
index_3 = binary_search(chocolates_3, target_not_exist, criteria=1)
print("Chocolate with weight", target_not_exist, "not found. Index:", index_3)

