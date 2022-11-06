#Name :Sahil Mahendra Mody
#Cwid:20007262




import math
def mean(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
        mean_number=sum/len(data)
    return mean_number

def median(data):
    data.sort()
    n = len(data)
    if n % 2 == 1:
        median_number= data[len(data)//2]
        return median_number
    else:
        temp = n // 2
        res = data[temp-1] + data[temp]
        res1=res/2
        return res1

def mode(data):
    dict = {}
    max_number = 0
    n=len(data)
    for i in range(n):
        if data[i] in dict:
            dict[data[i]] += 1
        else:
            dict[data[i]] = 1
        max_number = max(max_number,dict[data[i]])
    answer = []
    if max_number==1:
        return None
    for j in dict:
        if dict[j] == max_number:
            answer.append(j)
    return answer

def standardDeviation(data):
    sum = 0
    n=len(data)
    if n == 0 or n == 1:
        return 0
    for i in range(n):
        sum += data[i]
    mean1 = sum / len(data)
    sum1 = 0
    for i in range(n):
        sum1 += ((mean1 - data[i])**2)
    
    sd = math.sqrt(sum1/(n-1))
    return sd

 
data=[]
print("Enter the real numbers -1 to stop.")
while(True):
    num = int(input())
    if num == -1:
        break
    data.append(num)

print("Data is: ",data)
print("Mean is: %.2f"%mean(data))
print("Median is: ",median(data))
print("Mode is: ",mode(data))
print("Standard Deviation is: %.2f "%standardDeviation(data))
