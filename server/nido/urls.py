from django.urls import path

from . import views

urlpatterns = [
    path('tets1/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    
]
