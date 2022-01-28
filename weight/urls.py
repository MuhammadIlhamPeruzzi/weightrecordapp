from django.contrib import admin  
from django.urls import path  
from weight import views

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('list', views.list),  
    path('create',views.create),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),  
]  