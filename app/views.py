from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . models import BankData
from . forms import BankDataForm


def dashboard(request):
    return render(request, 'app/dashboard.html')


class UserListView(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BankData
    context_object_name = "users"
    template_name = "app/home.html"
    paginate_by = 5
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

class UserCreate(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BankData
    template_name = "app/user-form.html"
    fields = ("first_name", "last_name", "iban")
    success_url = reverse_lazy("user-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(UserCreate, self).form_valid(form)

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BankData
    template_name = "app/user-update.html"
    form_class = BankDataForm
    success_url = reverse_lazy("user-list")

    def get_object(self, *args, **kwargs):
        user = super(UserUpdate, self).get_object(*args, **kwargs)
        
        if not user.owner == self.request.user:
            raise Http404()

        return user

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(UserUpdate, self).form_valid(form)

class UserDelete(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BankData
    template_name = "app/delete-form.html"
    success_url = reverse_lazy("user-list")

    def get_object(self, *args, **kwargs):
        user = super(UserDelete, self).get_object(*args, **kwargs)
        if not user.owner == self.request.user:
            raise Http404()

        return user