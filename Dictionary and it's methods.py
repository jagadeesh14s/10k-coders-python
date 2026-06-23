class DictionaryManager:
    """A class to manage CRUD operations on a dictionary."""

    def __init__(self):
        # Create an empty dictionary
        self.dictionary: dict = {}

    def create_dictionary(self) -> dict:
        """Reset and return an empty dictionary."""
        self.dictionary = {}
        return self.dictionary

    def add_key_value(self, key, value) -> bool:
        """Add a new key-value pair. Returns True if added."""
        self.dictionary[key] = value
        return True

    def remove_key_value(self, key):
        """Remove a key-value pair and return its value, or a message if not found."""
        return self.dictionary.pop(key, "Key not found")

    def update_value(self, key, value) -> bool:
        """Update the value of an existing key. Returns True if updated."""
        if key in self.dictionary:
            self.dictionary[key] = value
            return True
        return False

    def get_value(self, key):
        """Retrieve the value associated with a given key."""
        return self.dictionary.get(key, "Key not found")


def main():
    manager = DictionaryManager()

    # Example use case: Create an empty dictionary
    print("Empty Dictionary:")
    print(manager.create_dictionary())

    # Example use case: Add key-value pairs
    manager.add_key_value("name", "Jagadeesh")
    manager.add_key_value("age", 22)
    manager.add_key_value("course", "AI & ML")
    print("\nDictionary after adding items:")
    print(manager.dictionary)

    # Example use case: Retrieve a value
    print("\nValue for key 'name':")
    print(manager.get_value("name"))

    # Example use case: Update a value
    manager.update_value("age", 23)
    print("\nDictionary after updating age:")
    print(manager.dictionary)

    # Example use case: Remove a key-value pair
    removed_value = manager.remove_key_value("course")
    print("\nRemoved value:")
    print(removed_value)
    print("\nDictionary after removing course:")
    print(manager.dictionary)


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
