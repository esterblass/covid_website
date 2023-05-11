from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Employee, Vaccine, Covid_cases
from . import db
from flask_login import current_user

add_employee = Blueprint('add_employee', __name__)


def is_valid_id(id_number):
    id_number = str(id_number).strip()
    if len(id_number) != 9:
        return False
    if not id_number.isdigit():
        return False
    id_sum = 0
    for i, digit in enumerate(id_number[:-1]):
        weight = (i % 2) + 1  # משקל הספרה תלוי במיקום שלה במספר
        digit_sum = sum(int(d) for d in str(int(digit) * weight))
        id_sum += digit_sum
    check_digit = (10 - (id_sum % 10)) % 10
    return check_digit == int(id_number[-1])


@add_employee.route('/create-employee', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        id_number = request.form.get('idNumber')
        address_city = request.form.get('addressCity')
        address_street = request.form.get('addressStreet')
        address_number = request.form.get('addressNumber')
        birth_date = None
        date_str = request.form.get('birthDate')
        # birth_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        if date_str:
            birth_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        phone_number = request.form.get('phoneNumber')
        mobile_number = request.form.get('mobileNumber')
        date_str = request.form.get('vaccine1Date')
        vaccine1_date = None
        if date_str:
            vaccine1_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        vaccine1_manufacturer = request.form.get('vaccine1Manufacturer')
        date_str = request.form.get('vaccine2Date')
        vaccine2_date = None
        if date_str:
            vaccine2_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        vaccine2_manufacturer = request.form.get('vaccine2Manufacturer')
        date_str = request.form.get('vaccine3Date')
        vaccine3_date = None
        if date_str:
            vaccine3_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        vaccine3_manufacturer = request.form.get('vaccine3Manufacturer')
        date_str = request.form.get('vaccine4Date')
        vaccine4_date = None
        if date_str:
            vaccine4_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        vaccine4_manufacturer = request.form.get('vaccine4Manufacturer')
        date_str = request.form.get("positiveResultDate")
        positive_result_date = None
        if date_str:
            positive_result_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        date_str = request.form.get("recoveryDate")
        recovery_date = None
        if date_str:
            recovery_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        employee = Employee.query.filter_by(id_number=id_number).first()
        if employee:
            flash('מספר זהות כבר קיים במערכת', category='error')
        elif not is_valid_id(id_number):
            flash('מספר זהות לא תקין', category='error')
        elif len(phone_number) < 9:
            flash('מספר טלפון חייב להכיל יותר מ-8 תווים', category='error')
        elif len(mobile_number) < 10:
            flash('מספר נייד חייב להכיל יותר מ-8 תווים', category='error')
        elif len(first_name) < 2:
            flash('שם פרטי חייב להכיל יותר מתו אחד', category='error')
        elif len(last_name) < 2:
            flash('שם משפחה חייב להכיל יותר מתו אחד', category='error')
        elif len(address_city) < 2:
            flash('שם העיר חייב להכיל יותר מתו אחד', category='error')
        elif len(address_street) < 2:
            flash('שם רחוב חייב להכיל יותר מתו אחד', category='error')
        elif len(address_number) < 1:
            flash('חובה להכניס מספר בית', category='error')
        elif birth_date is None:
            flash('חובה להכניס תאריך לידה', category='error')
        elif positive_result_date is not None and positive_result_date > recovery_date:
            flash('תאריך תוצאה חיובית חייב להיות לפני תאריך החלמה', category='error')
        else:
            new_employee = Employee(first_name=first_name, last_name=last_name, id_number=id_number,
                                    address_city=address_city, address_street=address_street,
                                    address_number=address_number, birth_date=birth_date, phone_number=phone_number,
                                    mobile_number=mobile_number)
            db.session.add(new_employee)
            db.session.commit()
            last_employee = db.session.query(Employee).order_by(Employee.id.desc()).first()
            last_employee_id = last_employee.id

            vaccine1 = Vaccine(employee_id=last_employee_id, vaccine_date=vaccine1_date,
                               vaccine_manufacturer=vaccine1_manufacturer)
            vaccine2 = Vaccine(employee_id=last_employee_id, vaccine_date=vaccine2_date,
                               vaccine_manufacturer=vaccine2_manufacturer)
            vaccine3 = Vaccine(employee_id=last_employee_id, vaccine_date=vaccine3_date,
                               vaccine_manufacturer=vaccine3_manufacturer)
            vaccine4 = Vaccine(employee_id=last_employee_id, vaccine_date=vaccine4_date,
                               vaccine_manufacturer=vaccine4_manufacturer)

            covid_case = Covid_cases(employee_id=last_employee_id, positive_result_date=positive_result_date,
                                     recovery_date=recovery_date)

            if vaccine1:
                db.session.add(vaccine1)
                db.session.commit()
            if vaccine2:
                db.session.add(vaccine2)
                db.session.commit()
            if vaccine3:
                db.session.add(vaccine3)
                db.session.commit()
            if vaccine4:
                db.session.add(vaccine4)
                db.session.commit()
            if covid_case:
                db.session.add(covid_case)
                db.session.commit()
            #
            # file = request.files['fileInput']
            # file.save(file.filename)

            flash('העובד נוסף בהצלחה!', category='success')
            return redirect(url_for('add_employee.create_employee'))

    return render_template("add_employee.html", user=current_user)



