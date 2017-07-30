def gcf(m,n) :
    if m<n :
        (m,n) = (n,m)
    if (m%n) == 0 :
        return(n)
    else :
        return(gcf(n,m%n))
   
   
def f(m,n):
    ans = 1
    while (m - n >= 0) :
        (ans,m) = (ans*2,m-n)
    return(ans)    
 
