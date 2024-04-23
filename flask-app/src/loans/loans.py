from flask import Blueprint, request, jsonify
from src import db, convert_db_to_json

loans = Blueprint('loans', __name__)

@loans.route('/', methods=['GET'])
def get_loans():
    cursor = db.get_db().cursor()
    cursor.execute('select * from BookLoans where return_date is null')
    return convert_db_to_json(cursor)

@loans.route('/', methods=['POST'])
def create_loan():
    end_date = request.form.get('end_date')
    book_id = request.form.get('book_id')
    user_id = request.form.get('user_id')
    cursor = db.get_db().cursor()
    cursor.execute('insert into BookLoans (book_id, user_id, loan_start, loan_end) values (%s, %s, now(), %s)', (book_id, user_id, end_date))
    db.get_db().commit()
    return jsonify({"success": True})

@loans.route('/overdue', methods=['GET'])
def get_overdue_loans():
    cursor = db.get_db().cursor()
    cursor.execute('select * from BookLoans where now() > loan_end and return_date is null')
    return convert_db_to_json(cursor)

@loans.route('/<loan_id>', methods=['GET'])
def get_loan(loan_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from BookLoans where loan_id = %s', loan_id)
    return convert_db_to_json(cursor)

@loans.route('/<loan_id>', methods=['DELETE'])
def end_loan(loan_id):
    cursor = db.get_db().cursor()
    cursor.execute('update BookLoans set return_date = now() where loan_id = %s;', loan_id)
    db.get_db().commit()
    return jsonify({"success": True})
