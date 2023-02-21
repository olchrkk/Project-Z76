from django.urls import path
from . import views
from .views import IndexView, LikePostView, PostView, LikeCommentView

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('post/<int:id>/', PostView.as_view(), name='post-comment'),
    path('post/likes/', LikePostView.as_view(), name='blog-post-likes'),
    path('comment/likes/', LikeCommentView.as_view(), name='blog-comment-likes')
]