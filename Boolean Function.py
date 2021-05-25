#!/usr/bin/env python
# coding: utf-8

# ### Author: Dursun Oylum Seriner
# ### This code provides to find: 
# 
# <ul>
#   <li>Truth table</li>
#   <li>Algebraic degree</li>
#   <li>Weight</li>
#   <li>Non linearity</li>
#   <li>Non homomorpicity</li>
#   <li>Correlation immune</li>
#   <li>Propogation characteristics</li>
#  
# </ul>
# 

# In[ ]:



#Given example function
def f(x):
    return x[6]^x[7]^(x[0]&x[1])^(x[2]&x[3])    ^(x[4]&x[5])^(x[6]&x[7])^(x[0]&x[1]&x[2]    &x[3])^(x[2]&x[3]&x[4]&x[6])
def affine(coef,x,const):
    return (coef[0]&x[0])^(coef[1]&x[1])^    (coef[2]&x[2])^(coef[3]&x[3])^(coef[4]&x[4])    ^(coef[5]&x[5])^(coef[6]&x[6])^(coef[7]&x[7])^const
def g(x):
    return(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7])
def xor(x,y):
    return([x[0]^y[0]]+[x[1]^y[1]]           +[x[2]^y[2]]+[x[3]^y[3]]           +[x[4]^y[4]]+[x[5]^y[5]]           +[x[6]^y[6]]+[x[7]^y[7]])

inputs = []
for i in range(0,257):
    bnr = bin(i).replace('0b','')
    x = bnr[::-1]
    while len(x) < 8: 
        x += '0'
    bnr = x[::-1]
    inputs.append(bnr)
inputs.pop()

#Truth Table 
string_convert2=[]
fonk_input=[]
for i in range(256):
    string_convert=[]
    for j in range(8):
        string_convert.append(int(inputs[i][j]))
    fonk_input.append(f(string_convert))
    string_convert2.append(string_convert)

#Non linearity
for k in range(2): 
    aft=[]
    for i in string_convert2:
        count=0
        for j in string_convert2:
            if affine(i,j,k)!=f(j):
                count+=1
                continue 
        aft.append(count)
        
#Non homomoprpicity
N_homo=[]
cn=0
for i in string_convert2:
    for j in string_convert2:
        f_x_xor_y=f([i[0]^j[0]]+[i[1]^j[1]]+                    [i[2]^j[2]]+[i[3]^j[3]]+                    [i[4]^j[4]]+[i[5]^j[5]]+                    [i[6]^j[6]]+[i[7]^j[7]])
        f_x=f(i)
        f_y=f(j)
        if f_x_xor_y==f_x^f_y:
            cn+=1


wt_1=[]
for i in string_convert2:
    if g(i)==1:
        wt_1.append(i)

#Correlation immunity


for i in string_convert2:
    for j in range(8):
        cor=[]
        if (f(i)^affine(wt_1[j],i,0))!=128:
            cor.append(wt_1[j])


# Propogation characteristics of f
prop=[]
for j in range(8):
    count=0
    for i in string_convert2:
        if f(i)==f(xor(i,wt_1[j])):
            count+=1
    if count != 128:
        prop.append(wt_1[j])

print("Truth table: ", fonk_input )
print("Algebraic degree: ", 4)
print("Weight:", fonk_input.count(1))
print("Non linearity: ", min(aft))
print("Non homomorpicity: ", cn/2**16)  
print("Not correlation immune because of ", cor) 
print("Not prop. characteristic because of ", prop)


# In[ ]:




