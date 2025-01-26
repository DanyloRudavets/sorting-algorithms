def insersort(f):
    for i in range(1,len(f)):
        while i>0 and f[i]<f[i-1]:
            f[i-1],f[i]=f[i],f[i-1]
            i-=1
    print(f)
insersort([1,2,4,5,3,9,8,6])
        