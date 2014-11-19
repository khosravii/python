__author__ = 'esy'
def enheraf(f):
    n=0

    for i in  range(0,len (f)):
        n+=f[i]
    y= n/len(f)
    e=(n-y)/len(f)
    if len(f)%2!=0:
       m=len(f)/2
       a=f[m]
    else:
        m=len(f)/2
        a=(f[m]+f[m-1])/2


    return (y,e,a)




if __name__ == '__main__':
    f=[3,2,6,4,5,1]
    print enheraf(f)