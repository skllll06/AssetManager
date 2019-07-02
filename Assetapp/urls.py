from django.urls import path
from .views import signupfunc,signinfunc,aseetlistfunc, logoutfunc,AssetCreate,AssetUpdate

urlpatterns = [
    path('signup/', signupfunc,name='signup'),
    path('', signinfunc,name='signin'),
    path('assetlist/', aseetlistfunc,name='assetlist'),    
    path('logout/', logoutfunc,name='logout'),
    path('assetcreate/',AssetCreate.as_view(),name='create'),
    path('update/<int:pk>/',AssetUpdate.as_view(),name='update'),
]



