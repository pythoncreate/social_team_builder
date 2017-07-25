"""team_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^$", views.ProjectListView.as_view(), name="home"),
    url(r"^admin/", admin.site.urls),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^projects/", include("projects.urls", namespace="projects")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    # url(r"^posts/", include("posts.urls", namespace="posts")),
    # url(r"^communities/",
    #     include("communities.urls", namespace="communities")),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)