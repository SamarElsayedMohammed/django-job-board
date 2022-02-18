from django.urls import path,include
from . import views
from . import api 


urlpatterns = [
    path('', views.jop_list,name ='job_list'),
    path('add', views.add_job ,name = 'add_job'),

    path('<str:slug>', views.jop_details ,name = 'job_detail'),

    #api your
    path('api/jobs', api.job_list_api ,name = 'job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api ,name = 'job_detail_api'),




]