from django.urls import path
from .views import AccountView


urlpatterns = [
    path('user/<int:id>/', AccountView.as_view(), name='user_account'),
    path('follow/', AccountView.as_view(), name='user-follows')

]




