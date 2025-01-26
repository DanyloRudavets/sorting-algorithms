def mergesort(f):
    if len(f)>1:
        left_array=f[:len(f)//2]
        right_array=f[len(f)//2:]

        mergesort(left_array)
        mergesort(right_array)
        l=0 #left side index
        r=0 # right side index
        k=0 # merging array index
        while l<len(left_array) and r<len(right_array):
            if left_array[l]<right_array[r]:
                f[k]=left_array[l]
                l+=1
            else:
                f[k]=right_array[r]
                r+=1
            k+=1
        while l<len(left_array):
            f[k]=left_array[l]
            l+=1
            k+=1
        while r<len(right_array):
            f[k]=right_array[r]
            r+=1
            k+=1
        return f
print(mergesort([1,2,4,5,3,9,8,6]))
