#Reverse Integer or sentence-------------done

no=input()
def RI(no):
    if no[0]=='-':#checking for the negative sign 
        print('-', end='')
    ri=[]   #creating an empty list
    for i in no:#iterating through the list of stringed numbers
        if i=='-':#once it sees  the negative sign it goes to the next iteration
            continue
        else:
            ri.append(i)#update the list with the result of all iteration
    ri.reverse()#reverse the list
    for i in ri:
        ans=print(i, end='')
    return ans
RI(no)