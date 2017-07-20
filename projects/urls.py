from django.conf.urls import url

from . import views

app_name = "projects"

urlpatterns = [
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
]