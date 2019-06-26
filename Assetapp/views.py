from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        reqUsername = request.POST['username']
        reqPassword = request.POST['password']
        try:
            User.objects.get(username=reqUsername)
            return render(request, 'signup.html',{'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(reqUsername, '', reqPassword)
            return redirect('signin')
    return render(request, 'signup.html',{'some':100})



def signinfunc(request):
    if request.method == 'POST':
        reqUsername = request.POST['username']
        reqPassword = request.POST['password']
        user = authenticate(request, username=reqUsername, password=reqPassword)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('signup')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'signin.html',{'error':'このユーザーは登録されていません'})
    return render(request, 'signin.html',{'some':100})

def aseetlistfunc(request):
    return render(request, 'AssetList.html')