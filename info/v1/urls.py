from django.urls import path

from info.v1.services.comment import CommentView
from info.v1.services.core import TestView
from info.v1.services.category import CategoryView
from info.v1.services.contact import ContactView
from info.v1.services.auth import LoginView, RegisterView, LogoutView
from info.v1.services.new import NewView
from info.v1.services.subscription import SubscriptionView


urlpatterns = [
    path('test/', TestView.as_view()),
    path("test/<int:pk>/", TestView.as_view()),

    path('ctg/', CategoryView.as_view()),
    path('ctg/<int:pk>/', CategoryView.as_view()),

    path('contact/', ContactView.as_view()),
    path('contact/<int:pk>/', ContactView.as_view()),

    path('comment/', CommentView.as_view()),
    path('comment/<int:pk>/', CommentView.as_view()),

    path('new/', NewView.as_view()),
    path('new/<int:pk>/', NewView.as_view()),

    path('subs/', SubscriptionView.as_view()),
    path('subs/<int:pk>/', SubscriptionView.as_view()),

    # auth: login va register
    path('login/', LoginView.as_view()),
    path('regis/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view())


]





