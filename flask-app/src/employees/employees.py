from flask import Blueprint, jsonify
from src import db, convert_db_to_json

employees = Blueprint('employees', __name__)

@employees.route('/', methods=['GET'])
def get_employees():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Employees')
    return convert_db_to_json(cursor)

@employees.route('/<employee_id>', methods=['DELETE'])
def fire_employee(employee_id):
    cursor = db.get_db().cursor()
    cursor.execute('delete from Employees where employee_id = %s;', employee_id)
    db.get_db().commit()
    return jsonify({"success": True})