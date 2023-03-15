from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Post, Comment, UserProfile
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request):
        followed_users = [user.id for user in request.user.profile.first().follows.all()]
        followed_users_posts = Post.objects.filter(
            user__id__in=followed_users).order_by('-id')
        posts_recent_all = Post.objects.all().order_by(
            '-id').exclude(id__in=followed_users_posts)
        posts = (list(followed_users_posts) + list(posts_recent_all))

        accounts = UserProfile.objects.all().order_by('-id').exclude(id__in=followed_users).exclude(id=request.user.id)[:6]
        params = {
            'posts_recent': posts,
            'accounts': accounts
        }
        return render(request, self.template_name, params)


class PostView(TemplateView):
    template_name = 'post-comment.html'

    @method_decorator(login_required)
    def get(self, request, id):
        post = Post.objects.get(id=id)
        account = UserProfile.objects.get(id=id)
        comments = Comment.objects.filter(post__id=id)
        params = {
            'account': account,
            'post': post,
            'comments': comments,
        }
        return render(request, self.template_name, params)

    def post(self, request):
        post = Comment.objects.get(id=request.POST["post_id"])
        post.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostCreateView(TemplateView):
    template_name = 'new_post.html'

    def post(self, request):
        content = request.POST["new_post"]
        cover = request.POST["new_cover"]
        Post.objects.create(user=request.user, content=content, cover=cover)

        return redirect('index')


class CommentView(TemplateView):

    def post(self, request):
        comment = Comment.objects.get(id=request.POST["comment_id"])
        comment.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CreateCommentView(TemplateView):

    def post(self, request):
        new_comment = request.POST["new_comment"]
        post_num = Post.objects.get(id=request.POST["post_id"])
        Comment.objects.create(content=new_comment, user=request.user, post=post_num)

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


class SearchView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        content = request.POST['content']
        # posts_by_author = Post.objects.filter(author__icontains=content)
        posts_by_content = Post.objects.filter(content__icontains=content)
        posts = posts_by_content
        # posts = posts_by_author.union(posts_by_content, all=False)
        params = {
            'posts': posts
        }

        return render(request, self.template_name, params)



