from django.urls import path
from . import views
from .views import IndexView, LikePostView, PostView, LikeCommentView, CreateCommentView, SearchView, CommentView, PostCreateView, PostDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('post/<int:id>/', PostView.as_view(), name='post-comment'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/likes/', LikePostView.as_view(), name='blog-post-likes'),
    path('comment/likes/', LikeCommentView.as_view(), name='blog-comment-likes'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-post-delete'),
    path('posts/comment/delete/', CommentView.as_view(), name='blog-post-comment-delete'),
    path('posts/comment/create/', CreateCommentView.as_view(), name='blog-post-comment-create'),
    path('post/search/', SearchView.as_view(), name='post-search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)