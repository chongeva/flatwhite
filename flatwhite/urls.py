"""flatwhite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^admin/', admin.site.urls),
]

from fluent_pages.sitemaps import PageSitemap
from fluent_pages.views import RobotsTxtView
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'pages': PageSitemap,
}

urlpatterns += [
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', RobotsTxtView.as_view()),
]

if settings.DEBUG:
    # Adds the media URL to be used in development
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.SMEDIA_URL,
        document_root=settings.SMEDIA_ROOT
    )
    
urlpatterns += [
    url(r'', include('fluent_pages.urls')),
]