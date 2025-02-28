
def character_count(book) -> dict:
    working_book = book.lower()

    char_inventory = {}
    for c in working_book:
        if c not in char_inventory.keys():
            char_inventory[c] = 1
        else:
            char_inventory[c] += 1

    return char_inventory


