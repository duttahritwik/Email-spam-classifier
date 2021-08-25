import os
import random
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import tkinter
import tkinter.messagebox

#The main directory where the dataset is present.
rootdir="C:\\Users\\DuttaHritwik\\Desktop\\Applied Data Science\\Email Spam Classifier\\Enron Dataset"

#Create two lists which will store words from the ham and spam emails
ham_list=[]
spam_list=[]
 
def create_word_features(words):
    my_dict=dict([(word,True) for word in words])
    return my_dict
 
for directories,subdirs,files in os.walk(rootdir):
    if (os.path.split(directories)[1]=='ham'):
        for filename in files:      
            with open(os.path.join(directories,filename),encoding="latin-1") as f:
                data=f.read()
                # The data we read is one big string. We need to break it into words.
                words=word_tokenize(data)
                ham_list.append((create_word_features(words),"ham"))
    
    if (os.path.split(directories)[1]=='spam'):
        for filename in files:
            with open(os.path.join(directories,filename),encoding="latin-1") as f:
                data=f.read()
                words=word_tokenize(data)
                spam_list.append((create_word_features(words),"spam"))

combined_list=ham_list+spam_list
print("Total number of ham and spam emails is "+ str(len(combined_list)))

#randomly shuffle the ham and spam emails
random.shuffle(combined_list)

training_part=int(len(combined_list)*0.8)
training_set=combined_list[:training_part]
test_set=combined_list[training_part:]

print("Number of emails in training set is "+ str(len(training_set)))
print("Number of emails in test set is "+ str(len(test_set)))

#Training the Naive Bayes Classifier
classifier=NaiveBayesClassifier.train(training_set)

# Finding the accuracy, using the test data
accuracy=nltk.classify.util.accuracy(classifier,test_set)
print("Accuracy is: ", accuracy * 100," %")
#Printing the most distinctive features
print(classifier.show_most_informative_features(20))

#Testing if a given message is ham or spam
root=tkinter.Tk()
def test_Spam():
    email=textInput.get(1.0,tkinter.END)
    words=word_tokenize(email)
    features=create_word_features(words)
    tkinter.messagebox.showinfo("Result","Given email is "+classifier.classify(features))

label=tkinter.Label(root,text="Enter sample email to test for spam")
label.grid(row=0,columnspan=4)
textInput=tkinter.Text(root,bg="white",height=20,width=50)
textInput.grid(row=1)
button=tkinter.Button(root,text="Check",command=test_Spam)
button.grid(row=2,column=0)
root.mainloop()