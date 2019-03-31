from django.shortcuts import render
from django.utils import timezone
from django.core.mail import mail_admins
from django.views.generic import TemplateView
from .forms import PostForm


class PaperView(TemplateView):
    template_name = 'send_post/post.html'

    def dispatch(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                theme = form.cleaned_data['title']
                message = ("Сообщение для Администратора от: " +
                           request.user.email +
                           '\n Текст сообщения: ' +
                           form.cleaned_data['text']
                           )
                post = form.save(commit=False)
                post.status = True
                post.author = request.user
                post.published_date = timezone.now()
                mail_admins(subject=theme, message=message)
                post.save()
            else:
                return render(request, 'home.html', {'form': form})
        else:
            form = PostForm()
        return render(request, self.template_name, {'form': form})
