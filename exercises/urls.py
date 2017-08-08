"""URL configuration for exercises app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^new$', views.ExerciseCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[-\w]+)/edit$', views.ExerciseUpdateView.as_view(), name='update'),
]
