#Name :Sahil Mahendra Mody
#Cwid:20007262




num=int(input("Enter a number: "))

def ascending(num):
    temp = []
    while num > 0:
        digit = num % 10
        temp.append((digit))
        num = num // 10
    temp.sort()
    result=0
    for i in range(len(temp)):
        result = result*10 + temp[i]
    return result
    
print(ascending(num))