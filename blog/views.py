from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Post, Comment
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request):
        posts = Post.objects.all()
        # post = Post.objects.get(id=id)
        # last_two_comments = Comment.objects.filter(post__id=id)[:2]
        params = {
            'posts': posts,
            # 'last_two_comments': last_two_comments,
        }
        return render(request, self.template_name, params)


class PostView(TemplateView):
    template_name = 'post-comment.html'

    @method_decorator(login_required)
    def get(self, request, id):
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post__id=id)
        params = {
            'post': post,
            'comments': comments,
        }
        return render(request, self.template_name, params)


class CommentView(TemplateView):

    def post(self, request):
        comment = Comment.objects.get(id=request.POST["comment_id"])
        comment.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class LikePostView(TemplateView):
    def post(self, request):
        post_id = request.POST['user_id']
        current_post = Post.objects.get(id=post_id)
        likes = [user for user in current_post.likes.all()]
        if request.user in likes:
            current_post.likes.remove(request.user)
        else:
            current_post.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class LikeCommentView(TemplateView):
    def post(self, request):
        comment_id = request.POST['comment_id']
        current_comment = Comment.objects.get(id=comment_id)
        likes = [user for user in current_comment.likes.all()]
        if request.user in likes:
            current_comment.likes.remove(request.user)
        else:
            current_comment.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
