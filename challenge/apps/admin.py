from django.contrib import admin
from .models import Company, users, DocumentUpload

admin.site.register(Company)

admin.site.register(users)

admin.site.register(DocumentUpload)
