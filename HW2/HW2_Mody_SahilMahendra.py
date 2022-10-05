# Name: Sahil Mahendra Mody
#CWID : 20007262
# Assignment 2

#q1
print("------------------------Q1------------------------------------")
input2=int(input("Q1: Enter number: "))
a=0
b=1
count=0
if input2 < 0:
    print("Please enter a positive number")
elif input2 == 0:
    print(a)
elif input2 == 1:
    print(b) 
else:
    print("Fibonacci Sequence: ")
    while count<input2:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1


#q2
import fileinput
print("------------------------Q2------------------------------------")
input1=input("Enter file name: ")
if input1=='payroll.txt':
    file=open("payroll.txt","r")
    print('%-15s%-15s%-10s' % ('Name', 'Hours Worked', 'Total Pay'))
    for line in file:
        data=line.split()
        name=str(data[0])
        hours_worked=float(data[1])
        payment=hours_worked * float(data[2])
        print('%-15s%-15s%-10s' % (name,hours_worked,payment))
else:
    print("Invalid Output")

#q3
print("------------------------Q3------------------------------------")
file1=input("Enter file1 name: ")
file2=input("Enter file2 name: ")

if file1=='myfile1.txt' and file2=='myfile2.txt':
    f=open("./myfile1.txt",'r+')
    data=f.read()
    f.close()

    fl=open("./myfile2.txt",'w')
    fl.write(data)
    fl.close()
else:
    print("Invalid file1 or file2 name")


#q4
print("------------------------Q4------------------------------------")
myDict={}
n=int(input("Enter the size of dict: "))
for i in range(n):
    keys=input("enter key: ")
    value=int(input("Enter value: "))

    myDict[keys]=value
print(myDict)
for j in myDict:
    if myDict[j]>1:
        for k in range(2,myDict[j]):
            if myDict[j]%k==0:
                break
        else:
            print(j,"is a prime number")


#q5
print("------------------------Q5------------------------------------")
number=int(input("Enter a number: "))
exponential=int(input('Enter exponential digit: '))

def expo(number, exponential):  
    result=1
    if exponential<0:
        return ("Invalid input")
    while exponential>0:
        result = result * number
        exponential-=1
    return result
print(expo(number,exponential))
