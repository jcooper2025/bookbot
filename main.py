import sys
from stats import character_count

# def sort_on(dict):
#     return dict[]


def count_words(book):
    return len(book.split())

def main():

    list_of_char_inv = []

    with open(sys.argv[1]) as f:
        file_contents = f.read()

    words = count_words(file_contents)
    print(f"{words} words found in the document\n")

    count_characters = character_count(file_contents)

    for key, item in count_characters.items():
        if key.isalpha():
            list_of_char_inv.append({key: item})

    list_of_char_inv.sort(key=lambda d: list(d.values())[0], reverse=True)

    for ele in list_of_char_inv:
        key, item = next(iter(ele.items()))
        print(f"{key}: {item}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
