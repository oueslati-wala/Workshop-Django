from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

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

class ConferenceCreate(CreateView):
    model= Conference
    template_name ="conference/add.html"
    fields = "__all__"
    success_url = reverse_lazy("liste_conferences")

class ConferenceUpdate(UpdateView):
    model=Conference
    template_name="conference/update.html"
    fields="__all__"
    success_url=reverse_lazy("liste_conferences")

class ConferenceDelete(DeleteView):
    model=Conference
    template_name="conference/delete.html"
    success_url=reverse_lazy("liste_conferences")