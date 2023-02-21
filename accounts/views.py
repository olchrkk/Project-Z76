from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegistrationForm


class SignUpView(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        return render(request. self.template_name, {'user_form': user_form})

