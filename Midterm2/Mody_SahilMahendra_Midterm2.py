#!/usr/bin/env python
# coding: utf-8

# In[95]:


import pandas as pd


# In[96]:


#Q1: READING DATA 
headers=["Employee","Salary","Year","Gender"]
data=pd.read_csv("salary-2.txt",sep=" ",names=headers)
data


# In[97]:


grouped=data.groupby("Gender")
grouped


# In[98]:


#Q2: MAXIMUM, STANDARD DEVIATION AND MEAN OF SALARIES BASED ON MALE AND FEMALES
maximum_salary=grouped["Salary"].max()
print("Maximum Salary based on gender: ",maximum_salary)
sd_salary=grouped["Salary"].std()
print("Standard Deviation based on gender: ",sd_salary)
mean_salary=grouped["Salary"].mean()
print("Mean Salary based on gender: ",mean_salary)


# In[99]:


#Interpreting the results
"""Maximum Salary of Male is 45 whereas of Female is 29
Standard Deviation of Male Salary is 7.42 whereas of Female is 4.321
Mean of Male Salary is 32.67 whereas of Female is 23.3"""


# In[100]:


#Q3: BOXPLOT
import matplotlib.pyplot as plt
data_salary=data.drop("Employee",axis=1)
data_salary1=data.drop("Year",axis=1)
grouped1=data_salary1.groupby("Gender")
grouped1.boxplot("Salary")
plt.show()


# In[101]:


sum_salary=grouped.agg({"Salary":"sum"})
per_salary=sum_salary.apply(lambda x: 100 *x/float(x.sum()))
per_salary


# In[102]:


#Q4: PIECHART
plt.pie(per_salary["Salary"], labels=["Female","Male"],autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()


# In[103]:


#Q5: Scatter plot
plt.scatter(data[data['Gender']=='M']['Year'],data[data['Gender']=='M']['Salary'])
plt.scatter(data[data['Gender']=='F']['Year'],data[data['Gender']=='F']['Salary'])
plt.xlabel("Years")
plt.ylabel("Salary")
plt.show()


# In[104]:


#Q6: Histogram
import seaborn as sns
sns.histplot(data=data, x="Salary",bins=5)
plt.show()
"""Yes it follows a normal distribution"""


# In[105]:


#Q7: Regression Plot
df = pd.DataFrame({'x_data':data["Salary"], 'y_data':data["Year"]})
sns.regplot('x_data', 'y_data', data=df)
plt.show()


# In[107]:


#Q8
""""
If I was the judge, I would rule in favour of the plaintiffs(females) and not the defendant(companies) as we can see the mean salary of females is 23.3 which is 
too less as compared to males which is 32.67. Also, the count of males employees is greater comparing with females
"""

