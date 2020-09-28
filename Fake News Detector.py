import pandas as pd 

df=pd.read_csv('/home/andre/Documents/Datasets/train.csv',nrows=50)
df=df.dropna()
# df.head()
# 1 unreliable, 0 reliable
df['label']=df['label'].map({0:'Real',1:'Fake'})

from sklearn.model_selection import train_test_split as tts

x=df.text
y=df.label
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.3,shuffle=True)

from sklearn.feature_extraction.text import CountVectorizer as cvr
from sklearn.naive_bayes import MultinomialNB as mnb

vectorizer=cvr()
counts=vectorizer.fit_transform(x_train.values)

targets=y_train.values
classifier=mnb()
classifier.fit(counts,targets)

x_test=vectorizer.transform(x_test)
pred=classifier.predict(x_test)
print(pred[:10])

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,pred)#calculate accuracy

# print(cm)

tp=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tn=cm[1][1]

accuracy=(tp+tn)/(tp+tn+fp+fn)
precision=tp/(tp+fp)
recall=tp/(tp+fn)
print("accuracy=", round(accuracy*100,2),'%')
print("precision=", round(precision*100,2),'%')
print("recall=", round(recall*100,2),'%')

