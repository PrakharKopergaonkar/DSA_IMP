# Find a digit which is first faulty i.e number is small than its previous
# In a loop continue replacing number after that index by 9 and decrement previous by 1 if found faulty
# Continue that untill index is > 0 .
N = input()


i = 1
flag = False
while(i<len(N)):
    if(N[i]<N[i-1]):
        flag=True
        break
    i+=1
if(flag):
    while(i>0):
        if(N[i]<N[i-1]):
            N = N[0:i-1] + str(int(N[i-1])-1) + '9'*((len(N)-i))
        i-=1
print(int(N))
        