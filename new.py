
from decimal import Decimal

def give_remainder_dict(a,b,c):
    x=Decimal(a)/Decimal(b)  #we use decimal model in order to get upto 28 places after decimal. In default float python can only accomodate upto 18 places
    f=str(x)                 #converting x to string in order to perform string operations
    s=f.split(".")           #if f="1.234" then s=['1','234']
    num=str(s[1])             
    if c<=28:
        num=num[:c]          #req number of decimal places is less then 28 then we slice our string to the req number of digits
    if num.count(num[0])==len(num):  #special case for divisions where all the decimal places are equal (eg:-1/3) and the req number of digits is > 28
        req=num[0]
        if c>28:
            diff=c-28
            for i in range(diff):
                num=num+req    #add that number to num diff number of times
    d={str(k):0 for k in range(10)}
    for n in num:
        d[n]+=1    #increment value in dict for every key found in num
    return d



if __name__=='__main__':
    dividend,divisor,n=map(int,input().split())
    print(give_remainder_dict(dividend,divisor,n))
