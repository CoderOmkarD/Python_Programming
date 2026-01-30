class BookStore:

    NoOfBooks = 0

    def __init__(self, BookName, AuthorName):

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

        self.Name = BookName
        self.Author = AuthorName

    def Display(self):
        print(self.Name, "by ", self.Author, ". No.of Books :", BookStore.NoOfBooks)


def main():

    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()
