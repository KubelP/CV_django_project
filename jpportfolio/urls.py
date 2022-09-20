from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path
from jpportfolio import views

app_name = 'jpportfolio'

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('cv/', TemplateView.as_view(template_name = 'my_cv.html'), name ='cv'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'), 
    path('contact/', views.my_contact, name='contact'), 
    path('success/', TemplateView.as_view(template_name = 'success.html'), name = 'success')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)