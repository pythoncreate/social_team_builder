from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from braces.views import LoginRequiredMixin, PrefetchRelatedMixin
from django.http import Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy


from accounts.models import *
from .models import *
from .forms import *


class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'project_list'
    queryset = Project.objects.all()
    template_name = 'index.html'


class ProjectDetailView(generic.DetailView):
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['positions'] = Position.objects.filter(project=context['project'])
        return context


class ProjectEditView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['p_formset'] = PositionInlineFormSet(
            queryset=Position.objects.filter(project=context['project']),
            prefix='p_formset'
        )
        return context


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    form_class = ProjectCreateForm
    context_object_name = 'project'
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:projects')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project_new.html'
    success_url = reverse_lazy('projects:projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['p_formset'] = PositionInlineFormSet(
            queryset=Position.objects.none(),
            prefix='p_formset'
        )
        return context

    def post(self, request, *args, **kwargs):
        form = ProjectCreateForm(self.request.POST)
        p_formset = PositionInlineFormSet(
            self.request.POST,
            queryset=models.Position.objects.none(),
            prefix='p_formset'
        )

        if form.is_valid():
            project = form.save(commit=False)
            project.creator = self.request.user
            project.save()
            if p_formset.is_valid():
                positions = p_formset.save(commit=False)
                for position in positions:
                    position.project = project
                    position.save()
                p_formset.save_m2m()
        return HttpResponseRedirect(reverse('projects:projects'))

class PositionApplyView(LoginRequiredMixin,generic.CreateView):
    pass