#This algo is nothing but the differene of larger number and smaller number in random array  which we are calling stock price
# Finding the difference between the smallest and the greatest value
price=[7,5,20,200,100,250,90,100,23,1]
n=len(price)
def findingval(price,n):
    buy=price[0]
    profit=0
    for i in range(0,n):
        if (buy>price[i]):
            buy=price[i]
        elif (price[i]-buy>profit):
            profit=price[i]-buy
    print(profit)
findingval(price,n)