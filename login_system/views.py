from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import StudentRegisterForm, TeacherRegisterForm
from django.contrib.auth.decorators import login_required


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
def profile(request):
    return render(request, 'profile.html')
