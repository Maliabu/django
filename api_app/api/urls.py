# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path
# from rest_framework.authtoken import views
# # from .v1.users.UsersView import CreateAuthUser, CreateUserAuthToken
# import importlib

# DEFAULT_API_VERSION="v1"
# ####################
# user_view = importlib.import_module(f"api.{DEFAULT_API_VERSION}.users.UsersView")
# ##################
# urlpatterns = [
# #  path('', views.index.as_view(), name="index"),
#  path('auth', views.obtain_auth_token),
#  path('<str:lang>/auth/token/', user_view.CreateUserAuthToken.as_view(), name="create-user-token"),
#  path('<str:lang>/auth/user/', user_view.GetAuthUser.as_view(), name="get-auth-user"),
#  path('<str:lang>/auth/user/<int:userid>/', user_view.GetAuthUserById.as_view(), name="get-auth-user-by-id"),
#  path('<str:lang>/auth/users/all', user_view.GetAllUsers.as_view(), name="get-all-users"),
# ]
# urlpatterns = urlpatterns + \
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
import importlib

DEFAULT_API_VERSION="v1"
####################
user_view = importlib.import_module(f"api.{DEFAULT_API_VERSION}.users.UsersView")
##################
urlpatterns = [
 path('', views.index.as_view(), name="index"),
 path('<str:lang>/auth/token/', views.CreateUserAuthToken.as_view(), name="create-user-token"),
 path('<str:lang>/auth/user/', user_view.GetAuthUser.as_view(), name="get-auth-user"),
 path('<str:lang>/auth/user/<int:userid>/', user_view.GetAuthUserById.as_view(), name="get-auth-user-by-id"),
 path('<str:lang>/auth/users/all/', user_view.GetAllUsers.as_view(), name="get-all-users"),
]
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)