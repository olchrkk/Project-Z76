from django.urls import path
from .views import AccountView, FollowersView, FollowingView, EditUserProfile


urlpatterns = [
    path('user/<int:id>/', AccountView.as_view(), name='user_account'),
    path('follow/', AccountView.as_view(), name='user-follows'),
    path('user/<int:id>/followers/', FollowersView.as_view(),
         name='user-followers'),
    path('user/<int:id>/following/', FollowingView.as_view(),
         name='user-following'),
    path('user/edit/', EditUserProfile.as_view(), name='user-edit'),

]




