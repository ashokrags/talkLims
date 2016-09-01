"""talkLims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from talkLims import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.navpage, name='startup'),
    url('^initiateproject/', include('talkLims.initiateproject.urls')),
    url('^samplemanifest/', include('talkLims.samplemanifest.urls')),
    url('^procedurerequest/procedurerequest_download/',
        include('talkLims.procedurerequest.procedurerequest_download.urls')),
    url('^procedurerequest/procedurerequest_upload/',
        include('talkLims.procedurerequest.procedurerequest_upload.urls')),
    url('^pullrequest/pullrequest_download/', include('talkLims.pullrequest.pullrequest_download.urls')),
    url('^pullrequest/pullrequest_upload/', include('talkLims.pullrequest.pullrequest_upload.urls')),
    url('^platesetup/platesetup_download/', include('talkLims.platesetup.platesetup_download.urls')),
    url('^platesetup/platesetup_upload/', include('talkLims.platesetup.platesetup_upload.urls')),
    url('^librarymaking/librarymaking_download/', include('talkLims.librarymaking.librarymaking_download.urls')),
    url('^librarymaking/librarymaking_upload/', include('talkLims.librarymaking.librarymaking_upload.urls')),
    url('^librarypooling/librarypooling_download/', include('talkLims.librarypooling.librarypooling_download.urls')),
    url('^librarypooling/librarypooling_upload/', include('talkLims.librarypooling.librarypooling_upload.urls')),
    # url('^rnaseqsubmission/', include('talkLims.pullrequest.urls')),
    # url(r'^samplemanifest/$', sampleviews.initiate_manifest, name='manifest-initiate-form'),
    # url(r'^samplemanifest/', sampleviews.manifest_verify, name='manifest-verify-form'),
    # url(r'^samplemanifest/', sampleviews.manifest_submit_complete, name='manifest-submit'),
]
