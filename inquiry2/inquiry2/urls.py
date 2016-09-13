"""inquiry2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from base.views import *

urlpatterns = [
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^submitted/$', SubmittedView.as_view(), name='submitted'),
    url(r'^data/$', DataView.as_view(), name='data'),

    #### DEBUGGING: TAKE OUT LATER ####
    url(r'^(?P<version>\d)/$', MainView.as_view()),
    ###################################
]
