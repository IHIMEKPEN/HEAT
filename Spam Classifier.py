import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer as cvr
from sklearn.naive_bayes import MultinomialNB as mnb
from sklearn.model_selection import train_test_split as tts

#loadind the dataset using panadas
data=pd.read_csv('/home/andre/Documents/Datasets/spam_or_not_spam.csv')


# data cleaning -knowing if spam 1 if not 0
data['label']=data['label'].map({0:'ham',1:'spam'})
data=data.dropna()
# data.email.fillna('')
# data[data['email'].notnull()]
data.isnull().sum()



x=data.email
y=data.label

x_train,x_test,y_train,y_test=tts(x,y,test_size=0.33, shuffle=True)

vectorizer=cvr()
counts=vectorizer.fit_transform(x_train.values)

targets=y_train.values
classifier=mnb()
classifier.fit(counts,targets)

example=pd.read_csv(r'/home/andre/Documents/Datasets/mails.csv')
example=example['message']
example.head(10)

example_count=vectorizer.transform(example.values)
predictions=classifier.predict(example_count)
predictions[:10]

x_test=vectorizer.transform(x_test)
pred=classifier.predict(x_test)
pred[:10]

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,pred)#calculate accuracy

print(cm)

tp=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tn=cm[1][1]

accuracy=(tp+tn)/(tp+tn+fp+fn)
precision=tp/(tp+fp)
recall=tp/(tp+fn)
print("accuracy=", accuracy)
print("precision=", precision)
print("recall=", recall)