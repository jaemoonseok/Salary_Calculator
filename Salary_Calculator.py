def main():
    salary_records = []
    salary_records = loadData(salary_records)
    command = input("Command:")

    while command != 'Quit':
        if command == 'Print':
            printSalaryRecords(salary_records)
        elif command == 'Total':
            totalSalaryPaid(salary_records)
        elif command == 'TotalEach':
            totalSalaryForEach(salary_records)
        elif command == 'WhoIsMax':
            maxTotalSalary(salary_records)
        elif command == 'MaxEach':
            maxTotalSalaryForEach(salary_records)
        elif command == 'Sort':
            sortRecords(salary_records)
        else:
            print("Please input a valid command!")
        command = input("Command:")
    print("BYE")

#Make first function loadData

def loadData():
    open('Salary_Records.txt')
    for i in loadData:
        salary_records.append(i)
    return salary_records

#Make second function printSalaryRecords

def printSalaryRecords():
    print("Name\tJan\tFeb\tMar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec")
    for i in salary_records:
        print(i, end= '\t')


#Make third function totalSalaryPaid


def totalSalaryPaid():
    sum1=0
    for i in salary_records:
        if type(i)==int:
            sum1=sum1 + i
    print(sum1)

#Make fourth function totalSalaryForEach
            
def totalSalaryForEach():
    sum2=0
    name=input()
    if name=='Billy':
        for i in salary_records(1,12):
            sum2= sum2+i
    elif name=='Betty':
        for i in salary_records(15,26):
            sum2= sum2+i
    elif name=='Apple':
        for i in salary_records(28,39):
            sum2=sum2+i
    elif name=='Kelly':
        for i in salary_records(41,52):
            sum2=sum2+i
    elif name=='Gigi':
        for i in salary_records(63,74):
            sum2=sum2+i
    else:
        print(name,'not found')
    print(sum2)


#Make fifth function maxTotalSalary

def maxTotalSalary():
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in salary_records(1,12):
            a=a+i
    for i in salary_records(15,26):
            b=b+i
    for i in salary_records(28,39):
            c=c+i
    for i in salary_records(41,52):
            d=d+i
    for i in salary_records(63,74):
            e=e+i
    if a>b>c>d>e:
        print('Billy earn the most')
    elif a>b>c>e>d:
        print('Billy earn the most')


#Make sisth function maxTotalSalaryForEach


def maxTotalSalaryForEach():
    sum2=0
    name=input()
    if name=='Billy':
        for i in salary_records(1,12):
            if i>sum2:
                sum2=i
        if sum2==salary_records(1):
            print('January')
        elif sum2==salary_records(2):
            print('Feburary')
        elif sum2==salary_records(3):
            print('March')
        elif sum2==salary_records(4):
            print('April')
        elif sum2==salary_records(5):
            print('May')
        elif sum2==salary_records(6):
            print('June')
        elif sum2==salary_records(7):
            print('July')
        elif sum2==salary_records(8):
            print('August')
        elif sum2==salary_records(9):
            print('September')
        elif sum2==salary_records(10):
            print('October')
        elif sum2==salary_records(11):
            print('November')
        elif sum2==salary_records(12):
            print('December')
    elif name=='Betty':
        for i in salary_records(15,26):
            if i>sum2:
                sum2=i
        print(sum2)
    elif name=='Apple':
        for i in salary_records(28,39):
            if i>sum2:
                sum2=i
        print(sum2)
    elif name=='Kelly':
        for i in salary_records(41,52):
            if i>sum2:
                sum2=i
        print(sum2)
    elif name=='Gigi':
        for i in salary_records(63,74):
            if i>sum2:
                sum2=i
        print(sum2)
    else:
        print(name,'not found')
        
main()
