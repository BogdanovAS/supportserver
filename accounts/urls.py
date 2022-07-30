from django.urls import path, re_path, include
 
from .views import SignUpView
 
urlpatterns = [
    re_path(r'^signup', SignUpView.as_view(), name='signup'),
]