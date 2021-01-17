from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import signupForm
def home_view(request):
    return render(request,'authapp/home.html')
@login_required
def python_view(request):
    return render(request,'authapp/python.html')
@login_required
def java_view(request):
    return render(request,'authapp/java.html')
@login_required
def aptitude_view(request):
    return render(request,'authapp/aptitude.html')
def logout_view(request):
    return render(request,'authapp/logout.html')
def signupView(request):
    f=signupForm()
    if request.method=='POST':
        f=signupForm(request.POST)
        if f.is_valid():
            user=f.save()
            user.set_password(user.password)
            user.save()
            return redirect("/accounts/login")
    d={"form":f}
    return render(request,'authapp/signup.html',d)
