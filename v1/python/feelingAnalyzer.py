from nltk.grammar import dg_demo
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class FeelingAnalyzer:
        
    def trainAndReturnRandomForestClassifierModel(verbose) :
        # Importing and reading the Dataset
        dataset_feeling_file = 'dataset_feeling.csv'
        feelings_messages = pd.read_csv(dataset_feeling_file)

        x_features_mailText = feelings_messages.iloc[:, 2].values
        y_labels_feelings = feelings_messages.iloc[:, 1].values

        # Representing Text in Numeric Form with TF-IDF
        vectorizer = TfidfVectorizer (
            max_features=2500, 
            # min_df=7, 
            # max_df=0.8,
            #stop_words=stopwords.words('french')
        )
        x_features_mailText = vectorizer.fit_transform(x_features_mailText)

        # Dividing Data into Training and Test Sets
        X_train, X_test, y_train, y_test = train_test_split(
            x_features_mailText, 
            y_labels_feelings, 
            test_size=0.2, 
            random_state=0
        )

        # Training the Model
        # 1
        text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        text_classifier.fit(X_train, y_train)

        # Making Predictions and Evaluating the Model
        y_feeeling_predictions = text_classifier.predict(X_test)
        if (verbose):
            print('\n*************************** Confusion matrix ****************************\n\n', confusion_matrix(y_test,y_feeeling_predictions))
            print('\n**************************** Classification report **********************\n\n', classification_report(y_test,y_feeeling_predictions))
        
        print("\nModel accuracy =", accuracy_score(y_test, y_feeeling_predictions)*100, "%\n\n")

        return text_classifier
    
    def trainAndReturnLinearSVCModel(verbose) :
        # Importing and reading the Dataset
        dataset_feeling_file = 'dataset_feeling.csv'
        feelings_messages = pd.read_csv(dataset_feeling_file)

        x_features_mailText = feelings_messages.iloc[:, 2].values
        y_labels_feelings = feelings_messages.iloc[:, 1].values

        # Representing Text in Numeric Form with TF-IDF
        vectorizer = TfidfVectorizer (
            max_features=2500, 
            # min_df=7, 
            # max_df=0.8,
            #stop_words=stopwords.words('french')
        )
        x_features_mailText = vectorizer.fit_transform(x_features_mailText)

        # Dividing Data into Training and Test Sets
        X_train, X_test, y_train, y_test = train_test_split(
            x_features_mailText, 
            y_labels_feelings, 
            test_size=0.2, 
            random_state=0
        )

        # Training the Model
        # 2
        clf = LinearSVC()
        clf.fit(X_train, y_train)

        # Making Predictions and Evaluating the Model
        y_feeeling_predictions = clf.predict(X_test)

        if (verbose):
            print('\n*************************** Confusion matrix ****************************\n\n', confusion_matrix(y_test,y_feeeling_predictions))
            print('\n**************************** Classification report **********************\n\n', classification_report(y_test,y_feeeling_predictions))
        
        print("\nModel accuracy =", accuracy_score(y_test, y_feeeling_predictions)*100, "%\n\n")

        return clf

    def predictMailFeeling_Positivity(verbose, mailToAnalyse):
        
        # Importing and reading the Dataset
        dataset_feeling_file = 'dataset_feeling.csv'
        feelings_messages = pd.read_csv(dataset_feeling_file)

        x_features_mailText = feelings_messages.iloc[:, 2].values
        y_labels_feelings = feelings_messages.iloc[:, 1].values

        # Representing Text in Numeric Form with TF-IDF
        vectorizer = TfidfVectorizer (
            max_features=2500, 
            # min_df=7, 
            # max_df=0.8,
            #stop_words=stopwords.words('french')
        )
        x_features_mailText = vectorizer.fit_transform(x_features_mailText)

        # Dividing Data into Training and Test Sets
        X_train, X_test, y_train, y_test = train_test_split(
            x_features_mailText, 
            y_labels_feelings, 
            test_size=0.2, 
            random_state=0
        )

        # Training the Model
        # 1
        text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        text_classifier.fit(X_train, y_train)
        # 2
        clf = LinearSVC()
        clf.fit(X_train, y_train)

        # Making Predictions and Evaluating the Model
        y_feeeling_predictions = clf.predict(X_test)

        if (verbose):
            print('\n*************************** Confusion matrix (positivity) ****************************\n\n', confusion_matrix(y_test,y_feeeling_predictions))
            print('\n**************************** Classification report (positivity) **********************\n\n', classification_report(y_test,y_feeeling_predictions))
            print("\nModel accuracy =", accuracy_score(y_test, y_feeeling_predictions)*100, "%\n\n")

        
        # After training the model, run it on a text (mail) to have the predictions  
        x_mail_text_to_predict = mailToAnalyse
        x_mail_text_to_predict_list = [x_mail_text_to_predict]
        x_mail_text_to_predict_vector = vectorizer.transform(x_mail_text_to_predict_list)
        
        predictionWithClf = clf.predict(x_mail_text_to_predict_vector)[0]
        predictionWithRandomForest = text_classifier.predict(x_mail_text_to_predict_vector)[0]

        
        print("Prediction positivity avec clf :", predictionWithClf)
        print("Prediction positivity avec text_classifier : ", predictionWithRandomForest)
        
        listResultats = [predictionWithClf, predictionWithRandomForest]
        return listResultats

    def predictMailFeeling_Alarming(verbose, mailToAnalyse):
        
        # Importing and reading the Dataset
        dataset_feeling_file = 'dataset_feeling_alarming.csv'
        feelings_messages = pd.read_csv(dataset_feeling_file)

        x_features_mailText = feelings_messages.iloc[:, 2].values
        y_labels_feelings = feelings_messages.iloc[:, 1].values

        # Representing Text in Numeric Form with TF-IDF
        vectorizer = TfidfVectorizer (
            max_features=2500, 
            # min_df=7, 
            # max_df=0.8,
            #stop_words=stopwords.words('french')
        )
        x_features_mailText = vectorizer.fit_transform(x_features_mailText)

        # Dividing Data into Training and Test Sets
        X_train, X_test, y_train, y_test = train_test_split(
            x_features_mailText, 
            y_labels_feelings, 
            test_size=0.2, 
            random_state=0
        )

        # Training the Model
        # 1
        text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        text_classifier.fit(X_train, y_train)
        # 2
        clf = LinearSVC()
        clf.fit(X_train, y_train)

        # Making Predictions and Evaluating the Model
        y_feeeling_predictions = clf.predict(X_test)

        if (verbose):
            print('\n*************************** Confusion matrix (alarming) ****************************\n\n', confusion_matrix(y_test,y_feeeling_predictions))
            print('\n**************************** Classification report (alarming) **********************\n\n', classification_report(y_test,y_feeeling_predictions))
            print("\nModel accuracy =", accuracy_score(y_test, y_feeeling_predictions)*100, "%\n\n")

        
        # After training the model, run it on a text (mail) to have the predictions  
        x_mail_text_to_predict = mailToAnalyse
        x_mail_text_to_predict_list = [x_mail_text_to_predict]
        x_mail_text_to_predict_vector = vectorizer.transform(x_mail_text_to_predict_list)
        
        predictionWithClf = clf.predict(x_mail_text_to_predict_vector)[0]
        predictionWithRandomForest = text_classifier.predict(x_mail_text_to_predict_vector)[0]

        
        print("Prediction positivity avec clf :", predictionWithClf)
        print("Prediction positivity avec text_classifier : ", predictionWithRandomForest)
        
        listResultats = [predictionWithClf, predictionWithRandomForest]
        return listResultats
        

    def predictMailFeeling_Engaging(verbose, mailToAnalyse):
        
        # Importing and reading the Dataset
        dataset_feeling_file = 'dataset_feeling_engaging.csv'
        feelings_messages = pd.read_csv(dataset_feeling_file)

        x_features_mailText = feelings_messages.iloc[:, 2].values
        y_labels_feelings = feelings_messages.iloc[:, 1].values

        # Representing Text in Numeric Form with TF-IDF
        vectorizer = TfidfVectorizer (
            max_features=2500, 
            # min_df=7, 
            # max_df=0.8,
            #stop_words=stopwords.words('french')
        )
        x_features_mailText = vectorizer.fit_transform(x_features_mailText)

        # Dividing Data into Training and Test Sets
        X_train, X_test, y_train, y_test = train_test_split(
            x_features_mailText, 
            y_labels_feelings, 
            test_size=0.2, 
            random_state=0
        )

        # Training the Model
        # 1
        text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        text_classifier.fit(X_train, y_train)
        # 2
        clf = LinearSVC()
        clf.fit(X_train, y_train)

        # Making Predictions and Evaluating the Model
        y_feeeling_predictions = clf.predict(X_test)

        if (verbose):
            print('\n*************************** Confusion matrix (engaging) ****************************\n\n', confusion_matrix(y_test,y_feeeling_predictions))
            print('\n**************************** Classification report (engaging) **********************\n\n', classification_report(y_test,y_feeeling_predictions))
            print("\nModel accuracy =", accuracy_score(y_test, y_feeeling_predictions)*100, "%\n\n")

        
        # After training the model, run it on a text (mail) to have the predictions  
        x_mail_text_to_predict = mailToAnalyse
        x_mail_text_to_predict_list = [x_mail_text_to_predict]
        x_mail_text_to_predict_vector = vectorizer.transform(x_mail_text_to_predict_list)
        
        predictionWithClf = clf.predict(x_mail_text_to_predict_vector)[0]
        predictionWithRandomForest = text_classifier.predict(x_mail_text_to_predict_vector)[0]

        
        print("Prediction positivity avec clf :", predictionWithClf)
        print("Prediction positivity avec text_classifier : ", predictionWithRandomForest)
        
        listResultats = [predictionWithClf, predictionWithRandomForest]
        return listResultats