
from django.contrib import admin
from django.urls import path
from samis import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('dashboard/', views.dashboard, name="dash"),
    path('engine_record/', views.engine, name="eng_rec"),
    path('run-command/', views.run_command, name='run_command'),
   # path('samis_drone_stream/', views.samis_drone_frame, name='samis_drone_stream'),
    
]




