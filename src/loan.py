# First Import Relevant Libraries..
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import warnings                           # This is used for removing upcoming warnings
warnings.filterwarnings('ignore')
import os
#Now we have to import LabelEncoder library  to do label encoding
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler  # Now import StandardScaler  for scalling the data
                                                     # but First import the library of StandardScalling

def stringToInt(string):
    integer = 0
    #try seeing if string value given is already a number if so the output would be
    try:
        #means string value given is already a int
        integer = int(string)
    except:
        string = string.lower()
        for i in string:
            integer += ord(i)
    return integer


def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
                 Loan_Amount_Term, Credit_History, Property_Area):


	#import dataset
	get_file = os.path.join("clustering.csv")
	df = pd.read_csv(get_file)

	df1 = df.drop("Loan_ID", axis =1)

	df1.Gender = df1.Gender.fillna("Male")

	df1.Dependents = df1.Dependents.fillna("0")

	df1.Self_Employed=df1.Self_Employed.fillna(method="ffill")

	df1.Loan_Amount_Term = df1.Loan_Amount_Term.fillna(df1.Loan_Amount_Term.median())

	df1.Credit_History.fillna(method="ffill")

	df1.Credit_History = df1.Credit_History.fillna(method="ffill")


	label = LabelEncoder()                    # these all are in string format so thats why we are applying Label encoding.. 

	df1.Gender = label.fit_transform(df1.Gender)

	df1.Married = label.fit_transform(df1.Married)

	df1.Dependents = label.fit_transform(df1.Dependents)

	df1.Education = label.fit_transform(df1.Education)

	df1.Self_Employed= label.fit_transform(df1.Gender)

	df1.Property_Area = label.fit_transform(df1.Property_Area)

	X = df1.drop('Loan_Status',axis = 1) # X is independent variable therefore, here y is dropped...

	y =  df1.Loan_Status   # This Dependent Variable


	sc = StandardScaler()
	scaled = sc.fit_transform(X)

	# After, Scalling all these we need to train and test data.. with the help of train _test_library

	from sklearn.model_selection import train_test_split

	x_train,x_test,y_train,y_test = train_test_split(scaled,y, test_size = 0.2)

	# import KNneighbour library

	from sklearn.neighbors import KNeighborsClassifier

	from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

	Accuracy =  []

	for i in range(1,20):
		knn = KNeighborsClassifier(n_neighbors=i)
		knn.fit(x_train,y_train)
		yp = knn.predict(x_test)
		Accuracy.append(accuracy_score(y_test,yp))


	knn = KNeighborsClassifier(n_neighbors=6)
	knn.fit(x_train,y_train)

	yp_knn = knn.predict(x_train)


	cm = confusion_matrix(y_test,yp)

	print(accuracy_score(y_test,yp))
	print(classification_report(y_test,yp))

	Gender = Gender.lower()
	Gender = stringToInt(Gender)

	Married = Married.lower()
	Married = stringToInt(Married)

	Dependents = Dependents.lower()
	Dependents = stringToInt(Dependents)

	Education = Education.lower()
	Education = stringToInt(Education)

	Self_Employed = Self_Employed.lower()
	Self_Employed = stringToInt(Self_Employed)

	Property_Area = Property_Area.lower()
	Property_Area = stringToInt(Property_Area)

	ApplicantIncome = int(ApplicantIncome)

    
	return knn.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
















































































































































