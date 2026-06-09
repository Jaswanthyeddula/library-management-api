from app import db
from app.models import Book
def get_all_books():
    books = Book.query.all()
    return {"books":[b.to_dict() for b in books]}
def create_new_book(data):
    book = Book(
        title = data['title'],
        author = data['author'],
        price  = data['price']
    )
    db.session.add(book)
    db.session.commit()
    return book.to_dict()
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return {"not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message":"book deleted"}
def get_one_book(id):
    book = Book.query.get(id)
    if not book:
        return {"not found"}
    db.session.commit()
    return book.to_dict()
def update_book(id, data):
    book = Book.query.get(id)
    if not book:
        return None
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.price = data.get('price', book.price)
    db.session.commit()
    return book.to_dict()

