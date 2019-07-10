from django.urls import path
from .views import signupfunc, signinfunc, AssetList, logoutfunc, AssetCreate, AssetUpdate, AssetDelete

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('', signinfunc, name='signin'),
    path('assetlist/', AssetList.as_view(), name='assetlist'),
    path('logout/', logoutfunc, name='logout'),
    path('assetcreate/', AssetCreate.as_view(), name='create'),
    path('update/<int:pk>/', AssetUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', AssetDelete, name='delete'),
]
