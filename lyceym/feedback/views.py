from django.shortcuts import render, redirect, reverse
from .forms import Form
from django.core.mail import send_mail
from .models import Feedback


def feedback(request):
    form = Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        feedback = Feedback.objects.create()
        text = form.cleaned_data['text']
        date = feedback.created_on
        feedback.text = text
        feedback.save()
        send_mail(
            date,
            text,
            'example@yandex.ru',
            ['Duck123321@yandex.ru'],
            fail_silently=True)
        return redirect(reverse('feedback:feedback'))
    context = {
        'form': form
    }
    return render(request, 'feedback.html', context)
