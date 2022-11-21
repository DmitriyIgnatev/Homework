from django.shortcuts import render, redirect
from .forms import Form
from django.core.mail import send_mail
from .models import FeedbackModel
from django.contrib import messages


def feedback(request):
    '''is_send отвечает за то, отправлено сообщение или нет'''

    form = Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        email = form.cleaned_data['email']
        feedback = FeedbackModel.objects.create(
            text=text,
            email=email)
        feedback.text = text
        feedback.save()
        send_mail(
            f'Спасибо за ваше обращение! Ваше письмо: {feedback.created_on}',
            text,
            email,
            ['Duck123321@yandex.ru'],
            fail_silently=True)
        messages.success(request, "Ваше сообщение успешно отправлено")
        return redirect('feedback:feedback')
    context = {
        'form': form,
    }
    return render(request, 'feedback.html', context)
