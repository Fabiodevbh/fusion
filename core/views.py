from django.views.generic import TemplateView


"""
Dentre as várias opções de view que temos, o instrutor optou por usar o TemplateView. Isso porque para usarmos o
TemplateView, precisamos somente informar o nome do template na classe que criamos abaixo (class IndexView)
"""


class IndexView(TemplateView):
    template_name = 'index.html'

