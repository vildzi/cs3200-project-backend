from flask import Blueprint, jsonify
from src import db, convert_db_to_json

books = Blueprint('books', __name__)

@books.route('/', methods=['GET'])
def get_books():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Books b join BookLocations bl on b.book_id = bl.book_id join BookGenres bg on bg.book_id = b.book_id join Genres g on g.genre_id = bg.genre_id')

    books_dict = {}
    for book in cursor:
        if book[1] not in books_dict:
            books_dict[book[1]] = {
                'book_id': book[0],
                'title': book[1],
                'isbn': book[2],
                'description': book[3],
                'author': book[4],
                'physical_condition': book[5],
                'total_stock_count': book[6],
                'rating': book[7],
                'row_num': book[9],
                'shelf_num': book[10],
                'genres': [book[14]]
            } 
        else:
            books_dict[book[1]]['genres'].append(book[14])
    return jsonify(list(books_dict.values()))

@books.route('/<bookid>')
def get_book(bookid):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Books b join BookLocations bl on b.book_id = bl.book_id where b.book_id = %s', bookid)
    return convert_db_to_json(cursor)