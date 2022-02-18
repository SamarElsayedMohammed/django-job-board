from django.shortcuts import render ,redirect
from . forms import SignupForm ,ProfileForm ,UserForm
from django.contrib.auth import authenticate ,login
from . models import Profile
from django.urls import reverse


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username ,password =password)
            login(request, user)
            return redirect('/accounts/profile')

    else:
        form = SignupForm()
    context={'form':form}
    return render(request, 'registration/signup.html',context)


def profile(request):
    # user that log in 
    profile = Profile.objects.get(user=request.user)
    context ={'profile':profile}
    return render(request, 'accounts/profile.html',context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        userform = UserForm(request.POST,instance=request.user)
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user =request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        profileform = ProfileForm(instance=profile)
        userform = UserForm(instance=request.user)
    context ={'profileform':profileform,'userform':userform}
    return render(request, 'accounts/profile_edit.html',context)
