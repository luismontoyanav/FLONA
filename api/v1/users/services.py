from typing import List
from users.models import Employee
from api.v1.users.lib.dataclasses import EmployeeData


def get_all_employees() -> List[EmployeeData]:
    employees = Employee.objects.all()
    return [
        EmployeeData(
            uuid=employee.uuid,
            id=employee.id,
            birth_date=employee.birth_date,
            photo=employee.photo,
            date_joined=employee.date_joined,
            last_modified=employee.last_modified,
            phone=employee.phone,
            street=employee.street,
            state=employee.state,
            city=employee.city,
            neighborhood=employee.neighborhood,
            zip_code=employee.zip_code,
            salary=employee.salary,
        )
        for employee in employees
    ]
