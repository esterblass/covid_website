from .models import db, Employee, Vaccine, Covid_cases
from flask import Blueprint, render_template, request

show_employee = Blueprint('show_employee', __name__)


@show_employee.route('/', methods=['GET', 'POST'])
def show_all_employees():
    if request.method == 'GET':
        employees = db.session.query(Employee, Covid_cases).join(Covid_cases).all()
        vaccines = db.session.query(Vaccine).all()

        dic_count_vaccine = {}
        for vaccine in vaccines:
            if vaccine.vaccine_date is None:
                if vaccine.employee_id not in dic_count_vaccine:
                    dic_count_vaccine[vaccine.employee_id] = 0
            else:
                dic_count_vaccine[vaccine.employee_id] = 1
        count = list(dic_count_vaccine.values()).count(0)

        return render_template('show_employee.html', employees=employees, vaccines=vaccines, count_not_vaccine=count)
    return render_template("show_employee.html")
