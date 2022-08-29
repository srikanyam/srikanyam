items={
    'sugar':30, 
    'chocolate':50, 
    'bread':40, 
    'cake':25, 
    'dhal':80, 
    'oil':200, 
    'poha':60
    }
oritem=[]
item={
1:'sugar', 
2:'chocolate', 
3:'bread', 
4:'cake', 
5:'dhal', 
6:'oil', 
6:'poha',
}
i=0
print("                     Welcome to SR store            ")
print('List of Items')
print('1.sugar-Rs.30\n2.chocolate-Rs.50\n3.bread-Rs.40\n4.cake-Rs.25\n5.dhal-Rs.80\n6.oil-Rs.200\n7.poha-Rs.60')
print('Enter your choice 1 to 7 for buy 8 for exit')
j=int(input())
while((j>=1)and (j<=7)):
    i=i+1
    print('Quantity you want')
    n=int(input())
    j1=item[j]
    j2=items[j1]
    k=n*j2
    oritem=oritem+[item[j], items[j1],n,k]
    print('List of items')
    print('1.sugar-Rs.30\n2.chocolate-Rs.50\n3.bread-Rs.40\n4.cake-Rs.25\n5.dhal-Rs.80\n6.oil-Rs.200\n7.poha-Rs.60')
    print('Enter your choice 1 to 7 for buy 8 for exit')
    j=int(input())
print(25*" ","TAX INVOICE",25*" ")
print(70* "*")
print('Item        Price        Quantity        Total')
print(70* "*")
b=0
ind=0
for x in range(i):
    print("%s\t    %0.2f\t\t%d\t\t%0.2f" %(oritem[ind],oritem[ind+1],oritem[ind+2],oritem[ind+3]))
    b=b+oritem[ind+3]
    ind=ind+4
    print(70* "*")
    print('Total Amount        %0.2f'%b)