from flask import Flask, request, jsonify

app = Flask(__name__)

books = []
next_id = 1  

@app.route('/')
def home():
    return "Book CRUD API is running!"

@app.route('/books', methods=['POST'])
def create_book():
    global next_id
    data = request.get_json()
    book = {
        "id": next_id,
        "book_name": data.get("book_name"),
        "author": data.get("author"),
        "publisher": data.get("publisher")
    }
    books.append(book)
    next_id += 1
    return jsonify({"message": "Book added successfully", "book": book}), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books[i]["book_name"] = data.get("book_name", book["book_name"])
            books[i]["author"] = data.get("author", book["author"])
            books[i]["publisher"] = data.get("publisher", book["publisher"])
            return jsonify({"message": "Book updated successfully", "book": books[i]})
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            deleted_book = books.pop(i)
            return jsonify({"message": "Book deleted successfully", "book": deleted_book})
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
