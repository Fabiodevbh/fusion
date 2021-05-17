from django.urls import path

from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # definindo a rota. repare q executaremos IndexView como uma função
]