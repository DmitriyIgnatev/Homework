from .models import CustomUser
from .forms import RegistrationForm, ProfileForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


def registrations(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        CustomUser.objects.create(**form.cleaned_data).save()
        messages.success(request, "Вы успешно зарегестрировались")
    context = {
        'form': form,
    }
    return render(request, 'user/reg.html', context)


def profile(request):
    if request.user.is_authenticated:
        form = ProfileForm(
            request.POST or None,
            initial={
                'username': request.user.username,
                'email': request.user,
                'first_name': request.user.first_name,
                'second_name': request.user.second_name,
                'birthday': request.user.birthday})
        if request.method == 'POST' and form.is_valid():
            user = CustomUser.objects.get(pk=request.user.pk)
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.second_name = form.cleaned_data.get('second_name')
            user.birthday = form.cleaned_data.get('birthday')
            user.save()
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
