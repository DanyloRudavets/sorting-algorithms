def bublesort(f):
    for i in range(len(f)):
        for j in range(len(f)-1):
            if f[i]<f[j]: #if you want to change the order from ascending to discending just change the sign lower than to greater than
                f[i],f[j]= f[j],f[i]
    print(f)
bublesort([2,3,4,6,7,1,9])