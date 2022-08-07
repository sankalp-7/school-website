
#function to get remainder dictionary

def give_remainder_dict(a,b,c):
    x=a/b
    f=round(x,c)    #rounding off numbers up to c deacimals
    f=str(f)
    s=f.split(".") # if f=1.234 then s=[1,234]
    num=str(s[1])
    d={str(k):0 for k in range(10)} #intitalizing dict keys from range 0-9
    for n in num:
        d[n]+=1 #increasing dict key value for every digit in num
    return d



if __name__=='__main__':
    dividend,divisor,n=map(int,input().split())
    print(give_remainder_dict(dividend,divisor,n))
