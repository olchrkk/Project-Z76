from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class AccountView(TemplateView):
    template_name = 'userAccount.html'

    @method_decorator(login_required)
    def get(self, request, id):
        user_profile = UserProfile.objects.get(id=id)

        params = {
            'otherUser': user_profile
        }
        return render(request, self.template_name, params)

    def post(self, request):
        followed_users = [user.id for user in request.user.profile.first().follows.all()]
        user = User.objects.get(id=request.POST['user_id'])
        profile = UserProfile.objects.get(id=request.user.id)
        profile.follows.add(user)
        if user in followed_users:
            request.user.profile.follows.remove()
        else:
            request.user.profile.follows.add(user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FollowersView(TemplateView):
    template_name = "follows.html"

    @method_decorator(login_required)
    def get(self, request, id):
        user = User.objects.get(id=id)
        followers = user.followers.all().exclude(id=user.id)
        user_follows = request.user.follows.all()

        params = {
            'last_users': followers,
            'user_follows': user_follows,
            'title': f"{user.username}'s followers"
        }
        return render(request, self.template_name, params)


class FollowingView(TemplateView):
    template_name = "follows.html"

    @method_decorator(login_required)
    def get(self, request, id):
        user = User.objects.get(id=id)
        follows = user.follows.all().exclude(id=user.id)
        user_follows = request.user.follows.all()

        params = {
            'last_users': follows,
            'user_follows': user_follows,
            'title': f"{user.username}'s follows"
        }
        return render(request, self.template_name, params)
