# Coleman Petras
# SDEV 220
# Create a CRUD API for a Book. The model should have the following parameters:
    # id, book_name, author, publisher

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.author} - {self.publisher}"

@app.route('/book', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'}), 201

@app.route('/book', methods=['GET'])
def get_book():
    book = Book.query.first()
    if not book:
        return jsonify({'message': 'No book available'}), 404
    return jsonify({'book': {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}})

@app.route('/book', methods=['PUT'])
def update_book():
    data = request.get_json()
    book = Book.query.first()
    if not book:
        return jsonify({'message': 'No book available'}), 404
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@app.route('/book', methods=['DELETE'])
def delete_book():
    book = Book.query.first()
    if not book:
        return jsonify({'message': 'No book available'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)