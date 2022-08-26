from django.shortcuts import render
from .loan import prediction
# Create your views here.



def home(request):
    return render(request, 'home.html' )




def Index(request):
	return render(request,'index.html')


def prediction_view(request):
    if request.method == "POST":
        Gender = (request.POST['Gender'])
        Married = (request.POST['Married'])
        Dependents = request.POST['Dependents']
        Education = request.POST['Education']
        Self_Employed = request.POST['Self_Employed']
        ApplicantIncome = request.POST['ApplicantIncome']
        CoapplicantIncome = request.POST['CoapplicantIncome']
        LoanAmount = request.POST['LoanAmount']
        Loan_Amount_Term = request.POST['Loan_Amount_Term']
        Credit_History = request.POST['Credit_History']
        Property_Area = request.POST['Property_Area']

        print("gender", Gender)
        print("married", Married)
        print("dependents", Dependents)
        print("education", Education)
        print("self_employee" , Self_Employed)
        print("ApplicantIncome" , ApplicantIncome)
        print("CoapplicantIncome",CoapplicantIncome)
        print("loanamount" ,LoanAmount)
        print("Loan_Amount_Term", Loan_Amount_Term)
        print("Credit_History" , Credit_History)
        print("propertyArea", Property_Area)

        loan = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term, Credit_History, Property_Area)
        
        return render(request,'prediction.html',{'loan':loan})
    return render('request','prediction.html')







