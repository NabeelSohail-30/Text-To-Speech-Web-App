"""
URL configuration for bolta_risala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from speech_generation.views import converter_view, generate_speech, display_speeches, serve_audio_file, generate_speech_eleven
from user_auth.views import custom_logout_view, custom_logout_page
from data_dictionary.views import data_dictionary
from merge_audios.views import upload_audio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('custom-logout/', custom_logout_view, name='custom_logout_view'),
    path('logout_page/', custom_logout_page, name='custom_logout_page'),
    path('converter/', converter_view, name='converter'),
    path('generate_speech', generate_speech, name='generate_speech'),
    path('generate_speech_eleven', generate_speech_eleven,
         name='generate_speech_eleven'),
    path('speeches', display_speeches, name='display_speeches'),
    path('data_dictionary', data_dictionary, name='data_dictionary'),
    path('upload_audio', upload_audio, name='upload_audio'),
    path('<path:path>', serve_audio_file, name='speech_file'),
]
