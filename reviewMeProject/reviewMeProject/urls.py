from django.urls import path, re_path
from reviewMe import views

urlpatterns = [
    path('', views.NameView.as_view(), name='username'),
    path(r'review/$', views.reviewView.as_view(), name='review'),
]
