from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был умпешно создан!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html',
                  {
        'title': 'Страница регистрации',
        'form': form
                  }
                  )


@login_required()
def profile(request):
    if request.method == "POST":
        profileform = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateuserform = UserUpdateForm(request.POST, instance=request.user)

        if profileform.is_valid() and updateuserform.is_valid():
            updateuserform.save()
            profileform.save()
            messages.success(request, f'Ваш аккаунт был успешно обнавлен!')
            return redirect('profile', {'title': 'Кабинет пользователя'})
    else:
        profileform = ProfileImageForm(instance=request.user.profile)
        updateuserform = UserUpdateForm(instance=request.user)

    data = {
        'profileform': profileform,
        'updateuserform': updateuserform
    }
    return render(request, 'users/profile.html', data)