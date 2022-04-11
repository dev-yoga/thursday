class Book:
  def __init__(self, input_title, input_author, input_pages, input_read = True):
      self.title = input_title
      self.author = input_author
      self.pages = input_pages
      self.read = input_read
  def __str__(self):
      return '{} {} {} {}'.format(self.title, self.author, self.pages, self.read)

book_one = Book("Simulacra and Simulation", "Baudrillard", 164)

print(book_one)
print(book_one.title)