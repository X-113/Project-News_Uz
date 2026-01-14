from django.urls import path
from . import views, auth_views

urlpatterns = [
    path("", views.index, name="home"),
    path("ctg/<slug>/", views.category, name="ctg"),
    path("search/", views.search, name="search"),
    path("view/<int:pk>/", views.view, name="view"),
    path("contact/", views.contact, name="contact"),
    path("add/subs/",views.add_subs,name="subs_add"),

    #auth
    path("login/", auth_views.login, name='login'),
    path("regis/", auth_views.register, name='register'),


    # path("api/test/", views.api_test)
]




