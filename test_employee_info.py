import employee_info as empinfo

def test_age_range():
    expected=[{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    answer=empinfo.get_employees_by_age_range(39,41)
    assert(answer==expected)

def test_avg_salaries():
    expected=60166.67
    answer=round(empinfo.calculate_average_salary(),2)
    assert(expected==answer)

def test_get_depart():
    expected=[ {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
              {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    answer=empinfo.get_employees_by_dept("Engineering")
    assert(expected==answer)