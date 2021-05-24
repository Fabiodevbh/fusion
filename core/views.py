from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario
from .forms import ContatoForm

"""
Dentre as várias opções de view que temos, INICIALMENTE o instrutor optou por usar o TemplateView. Isso porque para usarmos o
TemplateView, precisamos somente informar o nome do template na classe que criamos abaixo (class IndexView)

No commit C031 o instrutor fez uma mudança, trocando o TemplateView por FormView...
"""


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)