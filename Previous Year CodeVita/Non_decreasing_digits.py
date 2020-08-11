#start from last -> find digits that are fault, replace all after it (incl itselft) by 9 and decrease previous by 1
N = input()


i = len(N)-1


while(i>0):
    if(N[i]<N[i-1]):
        N = N[0:i-1] + str(int(N[i-1])-1) + '9'*((len(N)-i))
    i-=1
print(int(N))
        