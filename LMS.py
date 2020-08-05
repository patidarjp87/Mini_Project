import time
class Library:
    def __init__(self,list_of_books,library_name):
        self.lend_books={}
        self.list_of_books=list_of_books
        self.library_name=library_name
        #adding books to dictionary
        for books in self.list_of_books:
            self.lend_books[books]="Not issued to anyone"
    def display_books(self):
        print('please wait....')
        time.sleep(4)
        if self.list_of_books==[]:
            print("There is no book in your library")
        else:
            print('List of books is :')
        for i,b in enumerate(self.list_of_books):
            print(f"{i+1}.   {b}")
    def lend_book(self,book,taker_name):
        if book in self.list_of_books:
            if self.lend_books[book] =="Not issued to anyone":
                self.lend_books[book]=taker_name
                print('please wait....')
                time.sleep(3)
                print("Data Updated succesfully")
            else:
                print(f"sorry,this book is already lend by {self.lend_books[book]}")
        else:
            print("sorry, you have entered wrong book name...Entered book is not available in our library")
    def return_book(self,book,returner_name):
        if book in self.list_of_books:
            if self.lend_books[book]==returner_name:
                self.lend_books[book]="Not issued to anyone"
                print('please wait....')
                time.sleep(3)
                print("Data Updated succesfully")
            else:
                print("sorry but this book is not lend to you")
        else:
            print("sorry ,this book doesn't belongs to this library")
    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_books[book_name]="Not issued to anyone"
        print('please wait....')
        time.sleep(4)
        print("Book added succesfully")
    def delete_book(self,book_name):
        for x in self.list_of_books:
            if x==book_name:
                self.list_of_books.remove(book_name)
                del self.lend_books[book_name]
                print('please wait....')
                time.sleep(4)
                print("Book deleted succesfully")
                break
        else:
            print(f"sorry, There is no book named {book_name}")
def main():
    print('~~~~~WELCOME TO THE LIBRARY MANAGEMENT SYSTEM~~~~~')
    l=[str(x) for x in input("Enter books name by separator space").split()]
    n=input('Enter your library name')
    u=input('Username :')
    secret=input('password')
    jp=Library(l,n)
    print(f"~~~~~ WELCOME TO {n}'s LIBRARY ~~~~~\n")
    Exit=True
    while Exit !=False:
        print("\npress 'q' for exit \nDisplay Book Using 'd'\nAdd lend book using 'l'\nReturn a Book using 'r' \nAdd Book Using 'a'\nDelete Book using 'del' \n ")
        i=input()
        print()
        if i=='q':
            Exit=False
        elif i=="d":
            jp.display_books()
        elif i=='l':
            taker=input('What is your name ..?')
            book=input('Which book do you want to lend ')
            print("\nBook Lend \n")
            jp.lend_book(book,taker)
        elif i=='a':
            book=input("Book Name ")
            jp.add_book(book)
        elif i=='del':
            user=input('user name:')
            password=input('passward')
            if password==secret:
                book=input('Which book do you want to delete')
                jp.delete_book(book)
            else:
                print('sorry, Wrong passward')
        elif i=='r':
            name=input('What is your name ')
            book=input("which book do you want to return ")
            jp.return_book(book,name)
if __name__=='__main__':
  main()