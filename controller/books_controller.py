from app import app 
from model.books_model import Books
 
books_instance = Books()

@app.route('/books/display')
def showbooks():
    return books_instance.display_books()

