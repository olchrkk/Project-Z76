from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from users.models import UserProfile


class SignUpView(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            new_user = authenticate(
                username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password2']
            )
            login(request, new_user)
            return redirect('index')
        return render(request, self.template_name, {'user_form': user_form})


