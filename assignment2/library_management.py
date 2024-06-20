def add_book(title, author, genre):
    return {"title": title, "author": author, "genre": genre}

def add_to_library(book, library):
    if book['title'] in library:
        return f"Duplicate book '{book['title']}'. Not added to the library."
    else:
        library[book['title']] = book
        return f"Book '{book['title']}' by {book['author']} added to the library."

def remove_from_library(title, library):
    if title in library:
        del library[title]
        return f"Book '{title}' removed from the library."
    else:
        return f"Book '{title}' not found in the library."

def search_books(search_term, library):
    search_term_lower = search_term.lower()
    results = [book for book in library.values() if search_term_lower in book['title'].lower() or search_term_lower in book['author'].lower()]
    return results

def list_books(library):
    if library:
        print("All Books in the Library:")
        for book in library.values():
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
    else:
        print("The library is empty.")

def categorize_books(library):
    genre_dict = {}
    for book in library.values():
        genre = book['genre']
        if genre not in genre_dict:
            genre_dict[genre] = []
        genre_dict[genre].append(book)
    return genre_dict

def check_duplicates(library):
    seen_books = {}
    for book in library:
        key = (book[1], book[2])
        if key in seen_books:
            seen_books[key].append(book)
        else:
            seen_books[key] = [book]
    duplicates = {key: books for key, books in seen_books.items() if len(books) > 1}
    if duplicates:
        print("Duplicate books found:")
        for key, books in duplicates.items():
            print(f"Title: {key[0]}, Author: {key[1]}")
            for book in books:
                print(f"  ID: {book[0]}, Copies: {book[3]}, Price: {book[4]}")
    else:
        print("No duplicate books found.")

def display_books(books):
    if books:
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
    else:
        print("No books to display.")

def display_genres(genre_dict):
    for genre, books in genre_dict.items():
        print(f"\nGenre: {genre}")
        for book in books:
            print(f"  Title: {book['title']}, Author: {book['author']}")

def main_class():
    library = {}
    while True:
        print("\n LIBRARY MANAGEMENT SYSTEM ")
        print("1) Add a Book to the library")
        print("2) Remove a Book from the library")
        print("3) Search Books by title or author")
        print("4) List All Books in the library")
        print("5) Categorize Books by genre")
        print("6) Check for duplicate entries of books")
        print("7) Exit")

        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            genre = input("Enter the book genre: ").strip()
            book = add_book(title, author, genre)
            print(add_to_library(book, library))

        elif choice == 2:
            title = input("Enter the title of the book to remove: ").strip()
            print(remove_from_library(title, library))

        elif choice == 3:
            search_term = input("Enter the title or author to search for: ").strip()
            results = search_books(search_term, library)
            if results:
                print("Search Results:")
                display_books(results)
            else:
                print("No books found matching the search criteria.")

        elif choice == 4:
            list_books(library)

        elif choice == 5:
            categorized_books = categorize_books(library)
            if categorized_books:
                print("Books Categorized by Genre are as follows:")
                display_genres(categorized_books)
            else:
                print("No books available to categorize.")

        elif choice == 6:
            check_duplicates(library)

        elif choice == 7:
            print("Exited from Library Management System")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main_class()