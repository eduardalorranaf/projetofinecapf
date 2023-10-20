from django.shortcuts import render
from reserva.models import Stand
from stand.form import StandForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages import views


class Listar_S(ListView):
    template_name = "stand/stands.html"
    model = Stand
    context_object_name = 'stand'
    paginate_by = 3

class Detalhar_S(DetailView):
    model = Stand
    template_name = "stand/detalhar.html"  
    context_object_name = 'stand'

class Cadastrar_S(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  template_name = "stand/forms.html"
  success_url = reverse_lazy("listar")
  success_message = "Stand cadastrado com sucesso!"
  
class Deletar_S(views.SuccessMessageMixin, generic.DeleteView):
  model = Stand
  template_name = "stand/deletar.html"
  success_url = reverse_lazy("listar")
  success_message = "Stand removido com sucesso!"
  
class Editar_S(views.SuccessMessageMixin, generic.UpdateView):
  model = Stand
  form_class = StandForm
  template_name = "stand/forms.html"
  success_url = reverse_lazy("listar")
  success_message = "Stand atualizado com sucesso! " 
