from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('create_account/', views.CreateAccount.as_view(), name='create_account'),

    # path('json', views.cur_update, name='cur_update'),
    # path('currencies', views.Currencies.as_view(), name='currencies'),

]