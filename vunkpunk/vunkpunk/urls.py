"""
URL configuration for vunkpunk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from vp_comments.views import CommentsListView
from vp_forum import views
from vp_forum.views import CategoryView
from vp_users import views as v

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/sales/", views.SaleCardsListCreateView.as_view(), name="salecards_list"),
    path(r"api/sales/<int:pk>/", views.SaleCardRetrieveUpdateDestroy.as_view()),
    path(r"api/user/<int:pk>/", v.UserRetrieveUpdateDestroyView.as_view(), name="user"),
    path(r"api/comments/<int:post_id>/", CommentsListView.as_view(), name="comments_list"),
    path(r"api/categories/", CategoryView.as_view(), name="categories"),
    path(r"api/image/", include("images_manager.urls")),
    path(r"api/auth/token/login/", v.CustomTokenCreateView.as_view()),
    re_path(r"api/auth/", include("djoser.urls")),
    re_path(r"api/auth/", include("djoser.urls.authtoken")),
    path(r"api/auth/activate/", v.ActivateAccountView.as_view(), name="activate"),
]
