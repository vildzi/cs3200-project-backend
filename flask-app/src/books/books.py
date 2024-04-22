from flask import Blueprint
from src import db, convert_db_to_json

books = Blueprint('books', __name__)

@books.route('/', methods=['GET'])
def get_books():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Books')
    return convert_db_to_json(cursor)

