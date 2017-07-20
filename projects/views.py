from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from braces.views import LoginRequiredMixin, PrefetchRelatedMixin
from django.http import Http404

from . import models


class ProjectDetailView(generic.TemplateView):
    model = models.Project
    template_name = "projects/project.html"
