from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.core.mail import send_mail
from .models import FeedbackModel
from django.contrib import messages


def feedback(request):
    '''is_send отвечает за то, отправлено сообщение или нет'''

    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        feedback = FeedbackModel.objects.create(**form.cleaned_data)
        feedback.save()
        send_mail(
            f'Спасибо за ваше обращение! Ваше письмо: {feedback.created_on}',
            feedback.text,
            'Duck1233212@yandex.ru',
            [feedback.email],
            fail_silently=True)
        messages.success(request, "Ваше сообщение успешно отправлено")
        return redirect('feedback:feedback')
    context = {
        'form': form,
    }
    return render(request, 'feedback.html', context)
