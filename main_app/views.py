from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from main_app.models import User, RPG, Stat, Classification, Entity
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rpgs"] = RPG.objects.all()
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

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
    template_name = "account/account_detail.html"

class AccountUpdate(UpdateView):
    model = User
    fields = ['username']
    template_name = "account/account_update.html"

    def get_success_url(self):
        return reverse("account_detail", kwargs={'pk': self.object.pk})

class RPGIndex(TemplateView):
    template_name = "rpg/rpg_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rpgs"] = RPG.objects.all()
        return context

class RPGDetail(DetailView):
    model = RPG
    template_name = "rpg/rpg_detail.html"

class RPGCreate(CreateView):
    model = RPG
    fields = ['title', 'genre', 'description']
    template_name = "rpg/rpg_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RPGCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('rpg_detail', kwargs={'pk': self.object.pk})

class RPGUpdate(UpdateView):
    model = RPG
    fields = ['title', 'genre', 'description']
    template_name = "rpg/rpg_update.html"

    def get_success_url(self):
        return reverse('rpg_detail', kwargs={'pk': self.object.pk})

class RPGDelete(DeleteView):
    model = RPG
    template_name = "rpg/rpg_delete_confirm.html"
    success_url = "/"

class StatCreate(CreateView):
    model = Stat
    fields = ['title', 'description', 'max_value']
    template_name = "stat/stat_create.html"

    def form_valid(self, form):
        form.instance.rpg = RPG.objects.get(pk=self.kwargs["pk"])
        return super(StatCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rpg"] = RPG.objects.get(pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse('stat_create', kwargs={'pk': self.object.rpg.pk})

class ClassificationCreate(CreateView):
    model = Classification
    fields = ['title', 'description']
    template_name = "classification/classification_create.html"

    def form_valid(self, form):
        form.instance.rpg = RPG.objects.get(pk=self.kwargs["pk"])
        return super(ClassificationCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rpg"] = RPG.objects.get(pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse('classification_create', kwargs={'pk': self.object.rpg.pk})

class PlayableEntityCreate(CreateView):
    model = Entity
    fields = ['title', 'description']
    template_name = "playable_entity/playable_entity_create.html"

    def form_valid(self, form):
        form.instance.rpg = RPG.objects.get(pk=self.kwargs["pk"])
        return super(PlayableEntityCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rpg"] = RPG.objects.get(pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse('playable_entity_create', kwargs={'pk': self.object.rpg.pk})