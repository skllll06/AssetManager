from django.urls import path
from .views import signupfunc,signinfunc,aseetlistfunc

urlpatterns = [
    path('signup/', signupfunc,name='signup'),
    path('signin/', signinfunc,name='signin'),
    path('AssetList/', aseetlistfunc,name='assetlist'),    
]


