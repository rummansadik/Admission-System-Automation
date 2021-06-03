from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import (ProfileUpdateForm, StudentRegisterForm, StudentUpdateForm,
                    TeacherRegisterForm, TeacherUpdateForm)


def home(request):
    return render(request, 'home.html')


def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home_page')
    else:
        form = StudentRegisterForm()
    return render(request, 'student/register.html', {'form': form})


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home_page')
    else:
        form = TeacherRegisterForm()
    return render(request, 'teacher/register.html', {'form': form})


@login_required
def student_profile(request):
    if request.method == 'POST':
        u_form = StudentUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('student_profile')

    else:
        u_form = StudentUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'student/profile.html', context)


@login_required
def teacher_profile(request):
    if request.method == 'POST':
        u_form = TeacherUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('teacher_profile')

    else:
        u_form = TeacherUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'teacher/profile.html', context)
