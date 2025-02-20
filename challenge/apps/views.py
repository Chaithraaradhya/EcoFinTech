from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, CompanyRegistrationForm, DocumentUploadForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import users, Company, DocumentUpload
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully!')
            return redirect('user-register')  
    else:
        form = UserRegistrationForm()
    return render(request, 'app/user_register.html', {'form': form})


def company_register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company registered successfully!')
            return redirect('company-register')  
    else:
        form = CompanyRegistrationForm()
    return render(request, 'app/company_register.html', {'form': form})


def user_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = users.objects.get(name=username, password=password)
            messages.success(request, 'Logged in successfully!')  
            return redirect('document-upload')  
        except users.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('user-signin')  

    return render(request, 'app/user_signin.html')

def company_signin(request):
    if request.method == 'POST':
        
        company_name = request.POST.get('company_name')
        password = request.POST.get('password')

        try:
        
            company = Company.objects.get(name=company_name, password=password)
            messages.success(request, 'Logged in successfully!')
            return redirect('company-dashboard')  
        except Company.DoesNotExist:
            
            messages.error(request, 'Invalid company credentials. Please try again.')
            return redirect('company-signin') 

    return render(request, 'app/company_signin.html')

def document_upload(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data (uploads and text fields) to the database
            messages.success(request, 'Documents uploaded and information saved successfully!')
            return redirect('document-upload')  # Redirect to the same page or another page
        else:
            messages.error(request, 'There was an error with the form submission.')

    else:
        form = DocumentUploadForm()

    return render(request, 'app/document_upload.html', {'form': form})

encoder = OneHotEncoder(drop='first', sparse_output=False)
model = RandomForestClassifier(random_state=42)

def train_model():
    data = {
        'Water Resources': ['High', 'Low', 'Medium', 'High', 'Low'],
        'Soil Type': ['Black Soil', 'Sandy Soil', 'Black Soil', 'Black Soil', 'Red Soil'],
        'Location': ['Urban', 'Rural', 'Urban', 'Urban', 'Rural'],
        'Eligible': [1, 0, 1, 1, 0]
    }
    df = pd.DataFrame(data)
    encoder.fit(df[['Soil Type', 'Location']])
    encoded_features = encoder.transform(df[['Soil Type', 'Location']])
    df_encoded = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['Soil Type', 'Location']))
    df = pd.concat([df, df_encoded], axis=1)
    water_map = {'High': 3, 'Medium': 2, 'Low': 1}
    df['Water Resources'] = df['Water Resources'].map(water_map)
    X = df[['Water Resources'] + list(df_encoded.columns)]
    y = df['Eligible']
    model.fit(X, y)

train_model()

def landing_page(request):
    return render(request, 'app/homepage.html')


