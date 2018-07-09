from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('policy/<str:policy_code>/<int:naic_code>/details', views.policy_details, name='policy_details'),
  path('policy/description', views.policy_description, name='policy_description'),
  path('create', views.create_policy, name='create_policy')
];