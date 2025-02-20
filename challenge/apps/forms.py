from django import forms
from .models import users, Company, DocumentUpload

# Form for User Registration
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['name', 'email', 'password']

    # Optional: Clean password field to ensure it meets requirements
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('Password must be at least 6 characters long.')
        return password


# Form for Company Registration
class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'password']

    # Optional: Clean password field to ensure it meets requirements
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('Password must be at least 6 characters long.')
        return password

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = ['name','adhar_card','land_area', 'land_documents', 'soil_type', 'water_availability', 'location']
