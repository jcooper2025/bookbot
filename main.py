
def count_words(book):
    return len(book.split())

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(count_words(file_contents))


if __name__ == "__main__":
    main()
