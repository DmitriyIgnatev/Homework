from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import CustomUser
from .forms import RegistrationForm, ProfileForm


def registrations(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Вы успешно зарегестрировались')
    context = {
        'form': form,
    }
    return render(request, 'user/reg.html', context)


def profile(request):
    if request.user.is_authenticated:
        form = ProfileForm(request.POST or None, instance=request.user)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, "Сохранено")
        context = {
            'form': form,
        }
        return render(request, 'user/profile.html', context)
    return render(request, 'user/profile.html')


def users_list(request):
    users = CustomUser.objects.active()
    context = {
        'users': users
    }
    return render(request, 'user/user_list.html', context)


def user_detail(request, pk):
    user_object = get_object_or_404(CustomUser.objects.active(), pk=pk)
    context = {
        'user_object': user_object
    }
    return render(request, 'user/user_detail.html', context)
