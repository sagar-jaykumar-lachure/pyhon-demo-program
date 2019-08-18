#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:56:28 2019

@author: vnit-stu
"""
import pandas as pd
import csv

data = pd.read_csv("/home/vnit-stu/Desktop/car.data")
data.head()
data.shape
buying = {'vhigh' :4, 'high' :3, 'med' :2, 'low' :1}
maint = {'vhigh' :4, 'high' :3, 'med' :2, 'low' :1}
lug_boot ={'small' :1, 'med' :2, 'big' :3}
safety = {'low' :1, 'med' :2, 'high' :3}
doors = {'2' :2, '3' :3,  '4' :4, '5more' :5}
persons ={'2' :2, '4' :4, 'more' :5}
#class_val = {'unacc' :1 , 'acc' :2, 'good' :3, 'vgood' :4}
data.lug_boot = [lug_boot[item] for item in data.lug_boot]
data.buying = [buying[item] for item in data.buying] 
data.maint = [maint[item] for item in data.maint]
data.safety = [safety[item] for item in data.safety]
data.doors = [doors[item] for item in data.doors]
data.persons = [persons[item] for item in data.persons]
#data.class_val = [class_val[item] for item in data.class_val]
print(data) 
data.sort_values(by="class_val")
print(data)

print(data.groupby("class_val").size())
data.to_csv('/home/vnit-stu/Desktop/car1.data')

df = pd.read_csv('/home/vnit-stu/Desktop/car1.data') 
df_unacc = df[df['class_val'] == 'unacc'] 
#df_unacc = df_unacc(columns="Unnamed: 0" )
df_unacc.to_csv('/home/vnit-stu/Desktop/car_unacc.csv') 
df_acc = df[df['class_val'] == 'acc']
df_acc.to_csv('/home/vnit-stu/Desktop/car_acc.csv') 
df_good = df[df['class_val'] == 'good'] 
df_good.to_csv('/home/vnit-stu/Desktop/car_good.csv')
df_vgood = df[df['class_val'] == 'vgood']
df_vgood.to_csv('/home/vnit-stu/Desktop/car_vgood.csv') 



a=df_unacc.mean()
print(df_unacc.mean())
b=df_unacc.median()
print(df_unacc.median())
c=df_unacc.std()
print(df_unacc.std())
d=df_unacc.var()
print(df_unacc.var())
e=df_unacc.skew()
print(df_unacc.skew())
f=df_unacc.kurtosis()
print(df_unacc.kurtosis())

unacc=[[df_unacc.buying.mean(),df_unacc.buying.median(),df_unacc.buying.min(),df_unacc.buying.max(),df_unacc.buying.std(),df_unacc.buying.var(),df_unacc.buying.skew(),df_unacc.buying.kurtosis()],
       [df_unacc.maint.mean(),df_unacc.maint.median(),df_unacc.maint.min(),df_unacc.maint.max(),df_unacc.maint.std(),df_unacc.maint.var(),df_unacc.maint.skew(),df_unacc.maint.kurtosis()],
       [df_unacc.safety.mean(),df_unacc.safety.median(),df_unacc.safety.min(),df_unacc.safety.max(),df_unacc.safety.std(),df_unacc.safety.var(),df_unacc.safety.skew(),df_unacc.safety.kurtosis()],
       [df_unacc.doors.mean(),df_unacc.doors.median(),df_unacc.doors.min(),df_unacc.doors.max(),df_unacc.doors.std(),df_unacc.doors.var(),df_unacc.doors.skew(),df_unacc.doors.kurtosis()],
       [df_unacc.persons.mean(),df_unacc.persons.median(),df_unacc.persons.min(),df_unacc.persons.max(),df_unacc.persons.std(),df_unacc.persons.var(),df_unacc.persons.skew(),df_unacc.persons.kurtosis()],
       [df_unacc.lug_boot.mean(),df_unacc.lug_boot.median(),df_unacc.lug_boot.min(),df_unacc.lug_boot.max(),df_unacc.lug_boot.std(),df_unacc.lug_boot.var(),df_unacc.lug_boot.skew(),df_unacc.lug_boot.kurtosis()],
       ] 

with open('/home/vnit-stu/Desktop/unacc_class.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Mean ','Median','MIN','MAX','Std Deviation','Var','Skewness','Kurtosis'])
    w.writerows(unacc)
with open('/home/vnit-stu/Desktop/unacc_class.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]



acc=[[df_acc.buying.mean(),df_acc.buying.median(),df_acc.buying.min(),df_acc.buying.max(),df_acc.buying.std(),df_acc.buying.var(),df_acc.buying.skew(),df_acc.buying.kurtosis()],
       [df_acc.maint.mean(),df_acc.maint.median(),df_acc.maint.min(),df_acc.maint.max(),df_acc.maint.std(),df_acc.maint.var(),df_acc.maint.skew(),df_acc.maint.kurtosis()],
       [df_acc.safety.mean(),df_acc.safety.median(),df_acc.safety.min(),df_acc.safety.max(),df_acc.safety.std(),df_acc.safety.var(),df_acc.safety.skew(),df_acc.safety.kurtosis()],
       [df_acc.doors.mean(),df_acc.doors.median(),df_acc.doors.min(),df_acc.doors.max(),df_acc.doors.std(),df_acc.doors.var(),df_acc.doors.skew(),df_acc.doors.kurtosis()],
       [df_acc.persons.mean(),df_acc.persons.median(),df_acc.persons.min(),df_acc.persons.max(),df_acc.persons.std(),df_acc.persons.var(),df_acc.persons.skew(),df_acc.persons.kurtosis()],
       [df_acc.lug_boot.mean(),df_acc.lug_boot.median(),df_acc.lug_boot.min(),df_acc.lug_boot.max(),df_acc.lug_boot.std(),df_acc.lug_boot.var(),df_acc.lug_boot.skew(),df_acc.lug_boot.kurtosis()],
       ] 

with open('/home/vnit-stu/Desktop/acc_class.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Mean ','Median','MIN','MAX','Std Deviation','Var','Skewness','Kurtosis'])
    w.writerows(acc)
with open('/home/vnit-stu/Desktop/acc_class.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
    
    
good=[[df_good.buying.mean(),df_good.buying.median(),df_good.buying.min(),df_good.buying.max(),df_good.buying.std(),df_good.buying.var(),df_good.buying.skew(),df_good.buying.kurtosis()],
       [df_good.maint.mean(),df_good.maint.median(),df_good.maint.min(),df_good.maint.max(),df_good.maint.std(),df_good.maint.var(),df_good.maint.skew(),df_good.maint.kurtosis()],
       [df_good.safety.mean(),df_good.safety.median(),df_good.safety.min(),df_good.safety.max(),df_good.safety.std(),df_good.safety.var(),df_good.safety.skew(),df_good.safety.kurtosis()],
       [df_good.doors.mean(),df_good.doors.median(),df_good.doors.min(),df_good.doors.max(),df_good.doors.std(),df_good.doors.var(),df_good.doors.skew(),df_good.doors.kurtosis()],
       [df_good.persons.mean(),df_good.persons.median(),df_good.persons.min(),df_good.persons.max(),df_good.persons.std(),df_good.persons.var(),df_good.persons.skew(),df_good.persons.kurtosis()],
       [df_good.lug_boot.mean(),df_good.lug_boot.median(),df_good.lug_boot.min(),df_good.lug_boot.max(),df_good.lug_boot.std(),df_good.lug_boot.var(),df_good.lug_boot.skew(),df_good.lug_boot.kurtosis()],
       ] 

with open('/home/vnit-stu/Desktop/good_class.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Mean ','Median','MIN','MAX','Std Deviation','Var','Skewness','Kurtosis'])
    w.writerows(good)
with open('/home/vnit-stu/Desktop/good_class.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]

vgood=[[df_vgood.buying.mean(),df_vgood.buying.median(),df_vgood.buying.min(),df_vgood.buying.max(),df_vgood.buying.std(),df_vgood.buying.var(),df_vgood.buying.skew(),df_vgood.buying.kurtosis()],
       [df_vgood.maint.mean(),df_vgood.maint.median(),df_vgood.maint.min(),df_vgood.maint.max(),df_vgood.maint.std(),df_vgood.maint.var(),df_vgood.maint.skew(),df_vgood.maint.kurtosis()],
       [df_vgood.safety.mean(),df_vgood.safety.median(),df_vgood.safety.min(),df_vgood.safety.max(),df_vgood.safety.std(),df_vgood.safety.var(),df_vgood.safety.skew(),df_vgood.safety.kurtosis()],
       [df_vgood.doors.mean(),df_vgood.doors.median(),df_vgood.doors.min(),df_vgood.doors.max(),df_vgood.doors.std(),df_vgood.doors.var(),df_vgood.doors.skew(),df_vgood.doors.kurtosis()],
       [df_vgood.persons.mean(),df_vgood.persons.median(),df_vgood.persons.min(),df_vgood.persons.max(),df_vgood.persons.std(),df_vgood.persons.var(),df_vgood.persons.skew(),df_vgood.persons.kurtosis()],
       [df_vgood.lug_boot.mean(),df_vgood.lug_boot.median(),df_vgood.lug_boot.min(),df_vgood.lug_boot.max(),df_vgood.lug_boot.std(),df_vgood.lug_boot.var(),df_vgood.lug_boot.skew(),df_vgood.lug_boot.kurtosis()],
       ] 

with open('/home/vnit-stu/Desktop/vgood_class.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Mean ','Median','MIN','MAX','Std Deviation','Var','Skewness','Kurtosis'])
    w.writerows(vgood)
with open('/home/vnit-stu/Desktop/vgood_class.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
    
    

print(df.corr())
print(df.cov())
# Print the new dataframe 
#print(df_filtered.head(100)) 
  
# Print the shape of the dataframe 
#print(df_filtered.shape) 

# =============================================================================
# data = pd.DataFrame({'class':['unacc']})
# print(data)
# =============================================================================
# =============================================================================
# data = csv.reader(open('/home/vnit-stu/Desktop/car1.data'),delimiter=',')
# sortedlist = sorted(data, key=operator.itemgetter(7))    # 0 specifies according to first column we want to sort
#       #now write the sorte result into new CSV file
# with open("/home/vnit-stu/Desktop/car1.data", "wb") as f:
#     fileWriter = csv.writer(f, delimiter=',')
#     for row in sortedlist:
#         fileWriter.writerow(row)
# =============================================================================

# =============================================================================
# data.mean()
# data.corr()
# =============================================================================
# =============================================================================
# print(data.head())
# print(data.shape)
# # =============================================================================
# # print(data.mean())
# # print(data.corr())
# # =============================================================================
# print(data.buying.mean())
# print(data.corr())
# =============================================================================
