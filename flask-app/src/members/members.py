from flask import Blueprint
from src import db, convert_db_to_json

members = Blueprint('members', __name__)

@members.route('/', methods=['GET'])
def get_members():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Users')
    return convert_db_to_json(cursor)

@members.route('/<member_id>/loans')
def get_member_loans(member_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from BookLoans bl join Books b on b.book_id = bl.book_id where user_id = %s and bl.return_date is null', member_id)
    return convert_db_to_json(cursor)