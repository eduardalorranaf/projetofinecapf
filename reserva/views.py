from django.shortcuts import render
from .models import Reserva, Stand
from .form import ReservaForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages import views
from users.permissions import GerentePermission


class Index(LoginRequiredMixin,generic.TemplateView):
    template_name = "reserva/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context
    
class Add(GerentePermission,generic.TemplateView):
    template_name = "reserva/add.html"

class Perfil(generic.TemplateView):
    template_name = "account/profile.html"
    
class Detalhar(GerentePermission,LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "reserva/detalhar.html"  
    context_object_name = 'reserva'

class Listar(GerentePermission,generic.ListView):
    template_name = "reserva/reservas.html"
    model = Reserva
    context_object_name = 'reserva'
    paginate_by = 3


class Cadastrar(LoginRequiredMixin,views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reserva/forms.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class Deletar(GerentePermission,LoginRequiredMixin,views.SuccessMessageMixin, generic.DeleteView):
  model = Reserva
  template_name = "reserva/deletar.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva removida com sucesso!"
  
class Editar(GerentePermission,LoginRequiredMixin,views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reserva/forms.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva atualizada com sucesso! " 


 