from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Submission


class SubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    context_object_name = 'submissions'
    template_name = 'submission/list.html'

    def get_queryset(self):
        return Submission.objects.select_related('conference', 'user').filter(user=self.request.user)


class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = Submission
    context_object_name = 'submission'
    template_name = 'submission/detail.html'

    def get_queryset(self):
        return Submission.objects.select_related('conference', 'user').filter(user=self.request.user)


class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    template_name = 'submission/add.html'
    fields = ['title', 'abstract', 'keywords', 'paper', 'conference']
    success_url = reverse_lazy('submission_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if not form.instance.status:
            form.instance.status = 'submitted'
        return super().form_valid(form)


class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Submission
    template_name = 'submission/update.html'
    fields = ['title', 'abstract', 'keywords', 'paper']
    success_url = reverse_lazy('submission_list')

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user, status__in=['submitted', 'under review'])

    def dispatch(self, request, *args, **kwargs):
        submission = None
        try:
            submission = Submission.objects.get(pk=kwargs.get('pk'))
        except Submission.DoesNotExist:
            pass
        if submission and submission.status in ['accepted', 'rejected']:
            raise PermissionDenied("Une soumission acceptée ou rejetée ne peut pas être modifiée.")
        return super().dispatch(request, *args, **kwargs)
