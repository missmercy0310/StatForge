from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from main_app.models import User, RPG
from django.views.generic.edit import UpdateView
from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class AccountDetail(DetailView):
    model = User
    template_name = "account_detail.html"

class AccountUpdate(UpdateView):
    model = User
    fields = ['username']
    template_name = "account_update.html"
    def get_success_url(self):
        return reverse("account_detail", kwargs={'pk': self.object.pk})

class RPGIndex(TemplateView):
    template_name = "rpg_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rpgs"] = RPG.objects.all()
        return context

class RPGDetail(DetailView):
    model = RPG
    template_name = "rpg_detail.html"