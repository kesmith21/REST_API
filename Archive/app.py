from flask import Flask, request, jsonify
import pymssql

# import PyMySQL
# from flask_mysqldb import MySQL
# import mysql.connector


app = Flask(__name__)
app.secret_key = 'many random bytes'

books_list = [{
    "id": 1,
    "author": "Michael Lewis",
    "title": "Moneyball"
},
    {
        "id": 2,
        "author": "Ben Mezrich",
        "title": "Bitcoin Billionaires"
    }]


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_title = request.form['title']
        iD = books_list[-1]['id'] + 1

        new_obj = {
            "id": iD,
            "author": new_author,
            "title": new_title
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'title': book['title']
                }
                return jsonify(updated_book)

    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book('id') == id:
                books_list.pop(index)
                return jsonify(books_list)


if __name__ == "__main__":
    app.run(debug=True)
