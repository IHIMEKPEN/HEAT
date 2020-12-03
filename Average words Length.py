#Average words Length---------done

num1=0
num2=0

sentence1="Hi all, my name is Tom... I am orginally from Australia."
sentence2="I need to work very hard to learn more about algorithms in Python!"

wordsinsentence1=sentence1.split(" ")
wordsinsentence2=sentence2.split(" ")

den1=len(wordsinsentence1)
den2=len(wordsinsentence2)
            
        
for i in wordsinsentence1:
#remove all punctuation 
    i=i.replace("'","")
    i=i.replace(",","")
    i=i.replace(".","")
    
    num1+=len(i)
avg1=num1/den1
print(round(avg1,2))


for i in wordsinsentence2:
#remove all punctuation    
    i=i.replace("'","")
    i=i.replace(",","")
    i=i.replace(".","")
    i=i.replace("!","")
        
    num2+=len(i)
avg2=num2/den2
print(round(avg2,2))