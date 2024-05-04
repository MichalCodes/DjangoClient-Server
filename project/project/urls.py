"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SKJproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('person/<int:person_id>/', views.person, name = 'person'),
    path('addperson/', views.addperson, name='addperson'),
    path('cases/', views.cases, name='cases'),
    path('addcase/', views.addcase, name='addcase'),
    path('case/<int:case_id>/', views.showCase, name='show_case'),
    path('case/<int:case_id>/evidence/', views.showEvidence, name='show_evidence'),
    path('showwitness/<int:case_id>/', views.show_witness, name='show_witness'),
    path('add_criminal_record/<int:case_id>/', views.addCriminalRecord, name='add_criminal_record'),
    path('add_witness/<int:case_id>/', views.addWitness, name='add_witness'),
    path('add_defendant/<int:case_id>/', views.addDefendant, name='add_defendant'),
    path('add_evidence/<int:case_id>/', views.addEvidence, name='add_evidence'),
]
