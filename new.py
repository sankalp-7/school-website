


def give_remainder_dict(a,b,c):
    x=a/b
    f=round(x,c)
    f=str(f)
    s=f.split(".")
    num=str(s[1])
    d={str(k):0 for k in range(10)}
    for n in num:
        d[n]+=1
    return d



if __name__=='__main__':
    dividend,divisor,n=map(int,input().split())
    print(give_remainder_dict(dividend,divisor,n))