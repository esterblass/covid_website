from . import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    id_number = db.Column(db.String(10), nullable=False)
    address_city = db.Column(db.String(150), nullable=False)
    address_street = db.Column(db.String(150), nullable=False)
    address_number = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)


class Vaccine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    vaccine_date = db.Column(db.Date, nullable=True)
    vaccine_manufacturer = db.Column(db.String(50), nullable=True)


class Covid_cases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    positive_result_date = db.Column(db.Date, nullable=True)
    recovery_date = db.Column(db.Date, nullable=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    img_data = db.Column(db.LargeBinary)
