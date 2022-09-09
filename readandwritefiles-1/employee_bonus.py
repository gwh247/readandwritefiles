import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile)

next(csvfile)

#float is a decimal

for record in csvfile:
    full_name = record[1] + ' ' + record[2]
    salary = float(str(record[3]))
    bonus = float(str(record[4]))
    total_pay = ((salary * bonus) + bonus)
    print(type(total_pay))
    total_pay = format(total_pay, 'f')
    print(type(total_pay), total_pay)
    print('Full Name: ' + full_name + '\n')
    print('Total Pay: ' + total_pay + '\n')
    
