from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/register/', views.user_register, name='user-register'),
    path('company/register/', views.company_register, name='company-register'),
    path('user/signin/', views.user_signin, name='user-signin'),
    path('company/signin/', views.company_signin, name='company-signin'),
    path('upload-documents/', views.document_upload, name='document-upload'),
   path('', views.landing_page, name='landing_page'),
   
   
   
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)