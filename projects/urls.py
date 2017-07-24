from django.conf.urls import url

from . import views


app_name = "projects"

urlpatterns = [
    url(r'^project/$', views.ProjectListView.as_view(), name='projects'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^project/(?P<pk>\d+)/delete/$', views.ProjectDeleteView.as_view(), name='project_delete'),
    url(r'^project/(?P<pk>\d+)/edit/$', views.ProjectEditView.as_view(), name='project_edit'),
    url(r'^project/add/$', views.ProjectCreateView.as_view(), name='add_project'),
]