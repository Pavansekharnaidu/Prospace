# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAuthenticationView.as_view(), name='user-authentication'),
    path('assignments/', views.AssignmentListCreateView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('questions/', views.QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('classes/', views.ClassListCreateView.as_view(), name='class-list-create'),
    path('classes/<int:pk>/', views.ClassDetailView.as_view(), name='class-detail'),
]
