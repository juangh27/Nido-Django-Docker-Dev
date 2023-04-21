from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'nido'

urlpatterns = [
    path('tets1/', views.test, name='index'),
    path('test2/', views.test2, name='test2'),
    path('apadrinamiento/', views.apadrinamiento, name='apadrinamiento'),
    path('donativos/', views.apadrinamiento, name='donativos'),
    path('sesion/', views.apadrinamiento, name='sesion'),
    path('button', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('', TemplateView.as_view(template_name='nido/aves.html'), name='index'),
]
