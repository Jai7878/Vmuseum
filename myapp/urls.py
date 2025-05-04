"""
URL configuration for virtual_museum project.

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

from django.urls import path, include, re_path
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('gallerys/', views.gallerys, name='gallerys'),

    # path("dashboard/", views.admin_dashboard, name="admin-dashboard"),
    # path('about/problem-statement/', views.problem_statement, name="problem-statement"),
    # path('login/', views.login_page, name="login"),
    # path('services/details', views.service_details, name="service-details"),
    path('newsletter/subscribe', views.subscribe_newsletter, name="newsletter-subscribe"),
    path('newsletter/unsubscribe', views.unsubscribe_newsletter, name="newsletter-unsubscribe"),
    path('contact/form/submit', views.submit_contact_form, name="contact-form-submit"),
    # path("user/login/", views.user_login, name="user-login"),
    # path("user/logout/", views.user_logout, name="user-logout"),
    #re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
    
    #path('dashboard/', views.dashboard, name="dashboard"),
    #path('logout_user/', views.logout_user, name="logout-user"),
]



