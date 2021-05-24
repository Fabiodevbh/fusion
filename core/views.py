from django.views.generic import TemplateView

from .models import Servico, Funcionario


"""
Dentre as várias opções de view que temos, o instrutor optou por usar o TemplateView. Isso porque para usarmos o
TemplateView, precisamos somente informar o nome do template na classe que criamos abaixo (class IndexView)
"""


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        return context
