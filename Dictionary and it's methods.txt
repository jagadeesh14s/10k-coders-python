class DictionaryManager:
    def __init__(self):
        """Create an empty dictionary"""
        self.data = {}

    def add_item(self, key, value):
        """Add a new key-value pair"""
        self.data[key] = value
        print(f"Added: {key} -> {value}")

    def remove_item(self, key):
        """Remove a key-value pair"""
        if key in self.data:
            del self.data[key]
            print(f"Removed key: {key}")
        else:
            print(f"Key '{key}' not found.")

    def update_item(self, key, value):
        """Update the value of an existing key"""
        if key in self.data:
            self.data[key] = value
            print(f"Updated: {key} -> {value}")
        else:
            print(f"Key '{key}' not found.")

    def get_value(self, key):
        """Retrieve the value associated with a given key"""
        return self.data.get(key, "Key not found")

    def display(self):
        """Display the dictionary"""
        print("Current Dictionary:", self.data)


def main():
    # Create DictionaryManager object
    manager = DictionaryManager()

    print("----- Dictionary Operations -----")

    # Add key-value pairs
    manager.add_item("name", "Jagadeesh")
    manager.add_item("age", 22)
    manager.add_item("course", "AI & ML")
    manager.display()

    # Retrieve value
    print("\nValue for key 'name':", manager.get_value("name"))

    # Update existing key
    manager.update_item("age", 23)
    manager.display()

    # Remove key-value pair
    manager.remove_item("course")
    manager.display()

    # Try retrieving a removed key
    print("\nValue for key 'course':", manager.get_value("course"))


if __name__ == "__main__":
    main()

output:
----- Dictionary Operations -----
Added: name -> Jagadeesh
Added: age -> 22
Added: course -> AI & ML
Current Dictionary: {'name': 'Jagadeesh', 'age': 22, 'course': 'AI & ML'}

Value for key 'name': Jagadeesh
Updated: age -> 23
Current Dictionary: {'name': 'Jagadeesh', 'age': 23, 'course': 'AI & ML'}
Removed key: course
Current Dictionary: {'name': 'Jagadeesh', 'age': 23}

Value for key 'course': Key not found
