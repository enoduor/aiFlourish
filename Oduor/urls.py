from django.urls import path
from . import views



urlpatterns = [
     path('', views.home, name = 'home'),
     path('add-tools/', views.addStuffsView, name = 'addStuffsViews'),
     path('import/', views.import_from_excel, name='import_from_excel'),
     path('tool/<int:stuff_id>/', views.ToolDetail, name='tool'),
     path('video/', views.VideoView, name = 'videos'),
     path('filtered-tools/', views.filtered_tools, name='filtered_tools'),
]
   
