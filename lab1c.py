def search_employee(emp_list, id, index):
    if index == len(emp_list):
        return False

    if emp_list[index] == id:
        return True

    return search_employee(emp_list, id, index + 1)


employees = [101, 102, 103, 104, 105]

id = int(input("Enter employee ID to search: "))

if search_employee(employees, id, 0):
    print("Employee ID found")
else:
    print("Employee ID not found")
