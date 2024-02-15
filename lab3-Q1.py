employee_data = {} 

while True:
    name = input("Enter the employee name (or 'no' to exit): ")
    
    if name.lower() == 'no':
        break

    salary = float(input("Enter the employee salary: "))
    
    employee_data[name] = salary

print("Employee data stored successfully!")
print("Employee data:", employee_data)