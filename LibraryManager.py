#initialize empty lists, set and dictionary
book_list = []
authors_set = set ()
books_dict = {}

book_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

book_list.append("Python Fundamentals")
authors_set.add("Jane Doe")
books_dict["Python Fundamentals"] = "Jane Doe"

book_list.append("Data Science and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data Science and Algorithms"] = "Jane Doe"

book_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#search for a book
search_title = input("Enter the title of the book to search: ")
if search_title in book_list:
    print(f"Book found! The Author of the book {search_title}' is {books_dict[search_title]}")
else:
    print(f"Book not found.")


remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in book_list:
    remove_author = books_dict[remove_title]
    book_list.remove(remove_title)
    del books_dict[remove_title]

    if remove_author not in books_dict.values():
        authors_set.remove(remove_author)   

    print("Book removed successfully.")
    print("Book available along with their authors:", books_dict)
    print("Just available books:", book_list)
    print("Just the authors available:", authors_set)

else:
    print("Book not found.")
    