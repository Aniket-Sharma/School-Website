"""review_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from review.views import ReviewPageView, HomePageView, AboutPageView, AdmissionPageView, GalleryPageView, ContactPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReviewPageView.as_view(), name='review'),

    path('accounts/', include('accounts.urls'), name='accounts'),

    path('submit-review/', ReviewPageView.post, name='submit-review'),

    path('home/', HomePageView.as_view(), name='home'),
    # path('home/<str:email>' HomePageView.as_view() , name='subsribe'),

    path('about/', AboutPageView.as_view(), name='about'),
    path('admissions/', AdmissionPageView.as_view(), name='admissions'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    # path('contact/send/', send_message , name='send-message'),

]
