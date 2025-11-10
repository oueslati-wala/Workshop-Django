from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import ConferenceForm

def list_conferences(request):
    conferences_list=Conference.objects.all()
    return render(request,"conference\liste.html", {"liste":conferences_list})

class ConferenceList(ListView):
    model=Conference
    context_object_name="liste"
    template_name="conference/liste.html"

class ConferenceDetails(DetailView):
    model=Conference
    context_object_name="conference"
    template_name="conference/details.html"

class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles = {"organisateur ", "comite"}

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        user_role = getattr(request.user, 'role', None)
        if user_role not in self.allowed_roles:
            raise PermissionDenied("Accès réservé au comité d'organisation.")
        return super().dispatch(request, *args, **kwargs)


class ConferenceCreate(RoleRequiredMixin, CreateView):
    model= Conference
    template_name ="conference/add.html"
    #fields = "__all__"
    form_class=ConferenceForm
    success_url = reverse_lazy("liste_conferences")

class ConferenceUpdate(RoleRequiredMixin, UpdateView):
    model=Conference
    template_name="conference/update.html"
    #fields="__all__"
    form_class=ConferenceForm
    success_url=reverse_lazy("liste_conferences")

class ConferenceDelete(RoleRequiredMixin, DeleteView):
    model=Conference
    template_name="conference/delete.html"
    success_url=reverse_lazy("liste_conferences")