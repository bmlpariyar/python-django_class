#Book platform console app
books = []
print("Welcome to book review System: ")
while True:
    print("\n1)Add books\n2)Display Books\n3)Delete Books\n4)Exit\n")
    choice = int(input("Enter your choice(1,2,3,4): "))
    match choice:
        case 1:
            book_name = input("Enter the name of the book: ")
            author = input("Enter the name of the author: ")
            book = {"book_name": book_name, "author": author}
            books.append(book)
            print("\n=================================\nBook added successfully")
        case 2:
            for book in books:
                print(book)
        case 3:
            book_name = input("Enter the name of the book: ")
            for book in books:
                if book["book_name"] == book_name:
                    books.remove(book)
        case 4: 
            print("Thank you\nVisit Again!!!")
            break
        case _:
            print("\nInvalid Choice!!!")
            break