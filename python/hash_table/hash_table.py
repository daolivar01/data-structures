class HashTable:
    # Initialize the HashTable with a default size of 7.
    # The data_map array will store the key-value pairs.
    def __init__(self, size=7):
        self.data_map = [None] * size

    # Private method to compute a hash index for a given key.
    # It uses the ordinal values of each character in the key.
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # Prints the contents of the hash table, showing index and values stored.
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    # Inserts a key-value pair into the hash table.
    # Uses __hash to determine the index and handles collisions with chaining.
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # Retrieves the value associated with a given key.
    # If the key is found, returns the value; otherwise, returns None.
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    # Returns a list of all keys in the hash table.
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:  # Check for non-empty buckets
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
