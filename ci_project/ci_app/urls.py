from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_job, name='create_job'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('run/<int:job_id>/', views.run_job, name='run_job'),
    path('logs/<int:job_id>/', views.view_logs, name='view_logs'),  # Nowa ścieżka
]