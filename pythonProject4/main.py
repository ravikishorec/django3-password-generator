import pandas as pd
import numpy as np
#
# labels=['a','b','c']
# # my_data=[10,20,30]
# # array=np.array(my_data)
# # d={'a':10,'b':20,'c':30}
# print("labels:",labels)
# # # print("my_data:",my_data)
# # # print("array:",array)
# # # print("dictinary:",d)
# # # #creating series
# # # print("\nholding array data\n",'-'*20)
# # # a=pd.Series(array,labels)
# # # print(a)
# # ser1=pd.Series([1,2,3,4],['sa','si','dh','ar'])
# # ser2=pd.Series([1,2,3,4],['sa','si','dh','ar'])
# #
# # print(ser1)
# # print(ser1[1])
#
#
# my_data=np.random.rand(5,4)
# row_labels=['A','B','C','D','E']
# column_headings=['w','x','y','z']
# df=pd.DataFrame(my_data,index=row_labels,columns=column_headings)
# print("\n the data frame look like\n",'-'*50)
# print(df)
# # print("\n the only of x columns\n",'-'*50)
# # print(df[['w','x','y','z']],type(df))
# # print("\n adding the column\n",'-'*50)
# # df['new']=df['x']+df['y']
# # print(df)
# # #df=df.drop('new',axis=1)
# # #print(df)
t# # df=df.drop('A')
# # print(df)df
# #print(df.loc[['B','C']])
# # print(df.loc[['A','B']])
# # print(df.loc[['A','B'],['w','z']])
# print(df>0.6)
# booldf=df>0.6
# #print(df[booldf])
# # print(df.dropna(axis=0))
# data={'company':['f','f','e','l','m'],
#       'person':['sas','dar','var','sam','lon'],
#       'sales':[200,120,340,124,243]}
# df=pd.DataFrame(data)
# print(df)
# byComp=df.groupby('sales')print(byComp.mean())
# print(byComp.sum())
#












#
df=pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10],
                  'col2':[444,555,666,444,333,222,666,777,666,555],
                  'col3':'aaa bb c dd eeee fff gg h iii j'.split()})
print(df)
#print(df.head())
#print(df.tail())
#print(df['col2'].nunique())


#a=df['col2'].value_counts()
#print(a)
def testfunc(x):
    if (x>500):
        return(10*np.log10(x))
    else:
        return(x/10)
df['funcApplied']=df['col2'].apply(testfunc)
print(df)
k=df['col3length']=df['col3'].apply(len)
print(k)
l=df['funcApplied'].apply(lambda x:np.sqrt(x))
print(l)
print(df['funcApplied'].sum())
print(df['funcApplied'].max())
print(df['funcApplied'].std())

print(df['funcApplied'].mean())



