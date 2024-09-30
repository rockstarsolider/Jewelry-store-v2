"""
URL configuration for project project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import products
import products.urls
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    
    path('',include(products.urls)),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(  
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
)  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)