# Email-spam-classifier

A NAÏVE BAYES EMAIL SPAM CLASSIFIER

Introduction:
The emergence of the electronic mail or e-mail facility has proven to be of immense help to organizations wanting to reach out to a large audience all over the internet, in attempts to increase their sales. However, many of these mails are in fact not genuine, and are called junk mail or spam mail. Spam mail causes a lot of trouble for the internet community: large amount of spam traffic between servers causes delays in transmission of legitimate email. Sorting out the spam email from the legitimate mail is a time consuming process and constantly involves the risk of deleting useful mail. The goal of this project is to implement a simple Naïve Bayes Email Spam Filter in Python.

Spam Filtering:
Spam 	Filtering is a binary classification task. Given an email, the goal is to classify an email into any one of the two categories: spam(junk) mail or ham(legitimate) mail. The textual content of the mail: words like “free”, “Viagra”, “lottery”, “Congratulations! You have won a 1,000,000 dollars! Click here to claim your price”: is crucial in spam detection and offers some of the strongest clues. 
We will be using a Naïve Bayes Classifier for the purpose. The machine learning classifier that we will implement will detect that an email is spam or not based on some features that it will extract from the email, given the fact that it has been trained on a significant amount of labelled, training data. The performance of the email spam classifier depends considerably on the type of the classifier used, the size of the training data, and the quality of the features learned by the classifier. Moreover, the user also has the option to feed an input mail to the classifier through the code, and the result of the classification can be viewed.
The sample dataset that we will be using is the Ernon Dataset, which contains about half a million labelled emails, separately categorized into ham and spam emails. The dataset can be obtained from here. 


The spam detection process involves five steps, which are as follows:

	•	Loading the data
  
	•	Pre-processing of the data
  
	•	Extraction of the features
  
	•	Training the Classifier
  
	•	Evaluating the Classifier




 





