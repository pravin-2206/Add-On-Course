# Even index value sum


arr=[10,20,30,40,50]
sum=0
for i in range(0,len(arr),2):
        # if arr.index(i)%2==0:
        if i%2==0:
                
                sum=sum+arr[i]
print(sum)