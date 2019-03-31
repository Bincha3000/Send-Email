from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class RegisterView(TemplateView):
    template_name = 'user/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})
