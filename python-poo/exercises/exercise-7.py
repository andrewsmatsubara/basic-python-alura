class Book:
  def __init__(self, title, author, release_date):
    self._title = title
    self._author = author
    self._release_date = release_date
    self._available = True

  def __str__(self):
    return f'Title: {self._title.ljust(10)} | Author: {self._author.ljust(10)} | Release Date: {self._release_date}'
  
  def borrow(self):
    self._available = not self._available

  def verify_availability(self, year):
    available_books = [book for book in Book.books if book.release_year == year and book.available]

    return available_books
  
book_1 = Book('Book 1', 'Andrews', '1995')
book_2 = Book('Book 2', 'Laura', '2001')

print(book_1)
print(book_2)

book_1.borrow()

print(book_1._available)
