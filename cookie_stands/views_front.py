from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "CookieStands/cookieStands_list.html"
    model = CookieStand
    context_object_name = "CookieStands"



class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "CookieStands/cookieStands_detail.html"
    model = CookieStand
    success_url = reverse_lazy('CookieStand_list')



class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "CookieStands/cookieStands_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CookieStands/cookieStands_create.html'
    model = CookieStand
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them
    success_url = reverse_lazy('CookieStand_list')


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "CookieStands/cookieStands_delete.html"
    model = CookieStand
    success_url = reverse_lazy("CookieStand_list")
