import Employee
import pickle
import os

def buildEmpDict(employees):
    dict = {}
    for x in employees:
        dict[x.getID()] = x
    return dict

def printDict(dict):
    for x in dict:
        print(x,'-', dict[x])

def initDataFile(filename):
    print('  -> Data file: ', filename,' not found.',sep='')
    print('  -> Generating data...',sep='')
    employee1 = Employee.Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    employee2 = Employee.Employee('Mark Jones', 39119, 'IT', 'Programmer')
    employee3 = Employee.Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
    employees = [employee1, employee2, employee3]
    newDict = buildEmpDict(employees)
    save(newDict, filename)

def save(dict, filename):
    #filename = 'employees.dat'
    print('  -> Saving data to: ', filename,'...',sep='')
    binarywritefile = open(filename,'wb') #wb for writing binary
    pickle.dump(dict,binarywritefile)
    binarywritefile.close()
    print('  -> Data saved.')

def load(filename):
    #filename = 'employees.dat'
    print('  -> Loading data from: ', filename,'...',sep='')
    binaryreadfile = open(filename,'rb') #rb for reading binary
    #Using pickle to load objects from dat file
    dict = pickle.load(binaryreadfile)
    print('  -> Data loaded.')
    return dict

def getOption():
    print('Please enter the number of the action you wish to perform:\n' +
        '  1. Look up an employee in the dictionary\n' +
        '  2. Add a new employee to the dictionary\n' +
        '  3. Edit an existing employees information in the dictionary\n' +
        '  4. Delete an employee in the dictionary\n' +
        '  5. Quit the program')
    option = input()
    try:
        option = int(option)
    except:
        print('Input must be a number between 1 and 5.\n')
        option = -1
    return int(option)

def lookUpUser(dict):
    inputNum = int(input('Please enter employee ID to look up: '))
    try:
        print(dict[inputNum])
    except:
        print('Invalid employee ID number.')

def addEmployee(dict):
    print('Adding new employee:')
    name = input('  Please input new employee name: ')
    id = int(input('  Please input new employee ID number (as integer): '))
    dept = input('  Please input new employee department: ')
    job = input('  Please input new employee job: ')
    newEmp = Employee.Employee(name, id, dept, job)
    dict[id] = newEmp
    return dict

def editEmployee(dict):
    print('Editing employee:')
    id = int(input('  Please input employee ID number (as integer): '))
    name = input('  Please input employee name (leave blank to keep existing): ')
    dept = input('  Please input employee department (leave blank to keep existing): ')
    job = input('  Please input employee job (leave blank to keep existing): ')
    if len(name) == 0:
        name = dict[id].getName()
    if len(dept) == 0:
        dept = dict[id].getDept()
    if len(job) == 0:
        job = dict[id].getJob()
    edited = Employee.Employee(name, id, dept, job)
    dict[id] = edited
    print('Edited employee: ', edited)
    return dict

def deleteEmployee(dict):
    print('Deleting employee:')
    id = input('  Please input employee ID number to remove (or enter c to cancel): ')
    if id == 'c':
        return dict
    else:
        try:
            id = int(id)
            name = dict[id].getName()
            print('  -> Deleting record for employee: ',name, '...',sep='')
            del dict[id]
            print('  -> Deleted.')
        except:
            print('Invalid ID number.')
    return dict


def main():
    quit = False
    filename = 'employees.dat'
    if not os.path.exists(filename):
        initDataFile(filename)
    empDict = load(filename)
    printDict(empDict)
    print()
    option = -1
    while not quit:
        while option == -1:
            option = getOption()
        if option < 1 or option > 5:
            print('Invalid menu option. Please enter a number between 1 and 5.\n')
            option = -1
        if option == 1:
            lookUpUser(empDict)
            print()
        if option == 2:
            empDict = addEmployee(empDict)
            print()
        if option == 3:
            empDict = editEmployee(empDict)
            print()
        if option == 4:
            empDict = deleteEmployee(empDict)
            print()
        if option == 5:
            quit = True
        option = -1

    save(empDict,filename)
    print('  -> Quitting program...')


main()
