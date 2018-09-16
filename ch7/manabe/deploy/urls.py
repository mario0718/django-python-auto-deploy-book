from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import DeployCreateView, DeployUpdateView, DeployDetailView, DeployListView, jenkins_build, jenkins_status

app_name = 'deploy'

urlpatterns = [
    path('create/', login_required(DeployCreateView.as_view()),
         name='create'),
    path('list/', login_required(DeployListView.as_view()),
         name='list'),
    path('edit/<slug:pk>/', login_required(DeployUpdateView.as_view()),
         name='edit'),
    path('view/<slug:pk>/', login_required(DeployDetailView.as_view()),
         name='detail'),
    path('jenkins_build/', jenkins_build, name='jenkins_build'),
    path('jenkins_status/', jenkins_status, name='jenkins_status'),
]