from django.urls import path
from . import views



urlpatterns = [
     path('', views.home, name = 'home'),
     path('add-tools/', views.addStuffsView, name = 'addStuffsViews'),
     path('import/', views.import_from_excel, name='import_from_excel'),
]
   
