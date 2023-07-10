#To find the closest pair of values in a given array here we will create an arrray dynamically
shorted_array=[]
for i in range(2,100,3): #for creating an array of 100 indexes
    shorted_array.append(i)
n=len(shorted_array)#for findind the length of array
def givennumber(x,shorted_array,n):#creating a function to perform action
    l,r,diff=0,n-1,1000
    res_l,res_r=0,0
    while l < r:  # greaterthen is stopping the loop cause both are becomeing same so do noy use '=' sign in conditions
        if abs(shorted_array[l]+shorted_array[r]-x)<diff:
            res_l=l
            res_r=r
            diff=abs(shorted_array[l]+shorted_array[r]-x)
        elif shorted_array[l]+shorted_array[r]>x:
            r-=1
        else:
            l+=1
    print('The closest pair is {} and {}'.format(shorted_array[res_l],shorted_array[res_r]))
print("Program 1 : Finding the closest pair to a value given in sorted array")
x=int(input("Enter any number between 0-193 :"))
givennumber(x,shorted_array,n)#calling the function

