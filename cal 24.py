"""
算24点游戏
规则：4个数通过四则运算、括号得到24

cal程序功能：输入4个数于list，利用递归方法
得到算24点游戏的解

by dxh
date:20200303
lastchange:20200601
"""
#input 2number
#output possible soluion from cal ,and the operator

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
    

# +:0, -:1, *:2, /:3
#in:two number
#out:a tuple with result and its operator
def f(a,b):
    
    #让a>=b
    if(a<b):
        a,b=swap(a,b)
        
    res=[]
    res.append((a*b,'*'))
    res.append((a+b,'+'))
    res.append((a-b,'-'))
    if(b!=0):
        res.append((a/b,'/'))
        res.append((b/a,'/'))
    else:
        res.append((0,'/'))
    return res



#a:list,element is number
#temp:list,the solution,len=N+1
#N:dimension of initial problem
#n:len(a)
def cal(a,n,temp,N):
    if(n<=2):
        res=f(a[0],a[1])
        for i in res:#例(c,'+') i[0]对应c,i[1]对应'+'
            temp[N+1-n]=(a[0],i[1],a[1],'=',24)
            if(abs(i[0]-24)<=1E-7):
                temp[0]=True
                print(temp[1:])
                break
        return
            
    else:        
        for i in range(0,n):
            #若前面得到了结果则退出分支
            if(temp[0]==True):
                        break
            for j in range(i+1,n):
                    res=f(a[i],a[j])                    
                    for k in res:
                        temp[N+1-n]=(a[i],k[1],a[j],k[0])
                        #下一步要求解的新数组
                        new_a=[]            
                        for m in range(0,n):
                            if(m!=i and m!=j):
                                new_a.append(a[m])
                        new_a.append(k[0])
                        #print(new_a,n,temp[0])
                        #input()
                        cal(new_a,n-1,temp,N)
                        
                            
                        
#test
a=[1,5,5,5]
N=4
n=4
temp=N*[0]
temp[0]=False




#使用此函数时将 输出无解的组合 
def judge(a):
    temp=(n+1)*[0]
    temp[0]=False
    cal(a,n,temp,N)
    if(temp[0]==True):
        return True
    else:
        return False


def groupOfNoAnswer():
    s=0
    NoAnsGroup=[]
    for i in range(1,14):
        for j in range(i,14):
            for k in range(j,14):
                for l in range(k,14):
                    a=[i,j,k,l]
                    if(not judge(a)):
                        NoAnsGroup.append(tuple(a))
                        s+=1
    return s,NoAnsGroup
    
