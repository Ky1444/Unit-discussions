"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program demonstrates how Python dictionaries behave
like hash tables by performing insert, lookup, update,
delete, and edge‑case operations.
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================
    #
    # Python dictionaries *are* hash tables.
    # Each key is hashed internally, and the hash determines
    # where the value is stored in memory. This allows
    # O(1) average-time lookup, insert, update, and delete.

    print("\n=== INSERT OPERATIONS ===")

    hash_table = {}  # empty dictionary (empty hash table)

    # Add at least 5 key-value pairs
    hash_table["A101"] = "Laptop"
    hash_table["B202"] = "Keyboard"
    hash_table["C303"] = "Mouse"
    hash_table["D404"] = "Monitor"
    hash_table["E505"] = "Headset"

    print("Hash table after inserts:")
    print(hash_table)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Lookup works by hashing the key and jumping directly
    # to the memory location where the value is stored.
    item1 = hash_table["A101"]
    item2 = hash_table["D404"]

    print(f"Lookup A101 → {item1}")
    print(f"Lookup D404 → {item2}")

    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(hash_table)

    # Updating a key simply overwrites the value stored
    # at that hashed location.
    hash_table["C303"] = "Wireless Mouse"

    print("After update (C303 changed):")
    print(hash_table)

    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:")
    print(hash_table)

    # Deleting removes the key-value pair entirely.
    del hash_table["B202"]

    print("After deleting B202:")
    print(hash_table)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # 1. Lookup a missing key (raises KeyError)
    print("\nEdge Case 1: Lookup missing key")
    try:
        print(hash_table["Z999"])
    except KeyError:
        print("KeyError: Z999 does not exist in the hash table.")

    # 2. Safely delete a missing key using .pop()
    print("\nEdge Case 2: Safe delete missing key")
    removed = hash_table.pop("ZZZ", None)
    print(f"Attempted delete of ZZZ → Result: {removed}")

    # 3. Updating a missing key simply inserts it
    print("\nEdge Case 3: Update missing key (becomes insert)")
    hash_table["NEW1"] = "New Item"
    print("After inserting NEW1:")
    print(hash_table)

    # 4. Using an empty dictionary
    print("\nEdge Case 4: Operations on an empty dictionary")
    empty_dict = {}
    print("Empty dictionary:", empty_dict)
    print("Trying to lookup in empty dictionary:")
    print(empty_dict.get("anything", "Key not found (safe lookup)."))


if __name__ == "__main__":
    main()
