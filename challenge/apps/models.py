from django.db import models

class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DocumentUpload(models.Model):
    name = models.CharField(max_length=100)
    adhar_card = models.FileField(upload_to='documents/adhar_card/')
    land_documents = models.FileField(upload_to='documents/land_documents/')
    soil_type = models.CharField(max_length=255)
    water_availability = models.CharField(max_length=255) 
    location = models.TextField()
    land_area = models.DecimalField(max_digits=10, decimal_places=2)  # New field for land area
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DocumentUpload {self.id} - {self.soil_type}, {self.location}, {self.land_area} hectares"