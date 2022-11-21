import database




def writeWorker(name,position):
    database.writeNewWorker(name,position)


def writeBook(name,number_of_books,author,year):
    database.writeBooks(name_of_the_book=name,number_of_books=number_of_books,book_author=author, book_year_created=year)

def main():
    writeWorker(name="Иванов Иван",position="Библиотекарь")
    writeBook(name="Пугра над карточным домиком",number_of_books=100,author='Игорь Ефимов',year='2012')

if __name__ == '__main__':
    main()