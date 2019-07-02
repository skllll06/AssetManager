from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Assetlist
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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
    return render(request, 'signup.html')



def signinfunc(request):
    if request.method == 'POST':
        reqUsername = request.POST['username']
        reqPassword = request.POST['password']
        user = authenticate(request, username=reqUsername, password=reqPassword)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('assetlist')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'signin.html',{'error':'このユーザーは登録されていません'})
    return render(request, 'signin.html')

def logoutfunc(request):
    logout(request)
    return redirect('signin')


@login_required
def aseetlistfunc(request):
    object_list = Assetlist.objects.all()
    return render(request, 'AssetList.html',{'object_list':object_list})


class AssetCreate(CreateView):
        template_name='create.html'
        model = Assetlist
        object_list = Assetlist.objects.all()
        fields = ('assetname','controlno','modelno','boughtdate','stockplace')
        success_url =reverse_lazy('assetlist')
        

class AssetUpdate(UpdateView):
    model = Assetlist
    fields = '__all__'  # or ['colmunname', 'colmunname', 'colmunname']
    template_name = 'update.html'
    success_url =reverse_lazy('assetlist')
    
class AssetDelete(DeleteView):
    model = Assetlist
    success_url = reverse_lazy('assetlist')
    

    