x=10
print("X= %d" % x)

def gcf(m,n) :
    if m<n :
        (m,n) = (n,m)
    if (m%n) == 0 :
        return(n)
    else :
        return(gcf(n,m%n))
    
 
