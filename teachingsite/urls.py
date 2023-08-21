"""teachingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 包含siteindex的url在项目url中
urlpatterns += [
    path('siteindex/', include('siteindex.urls')),
]

# 包含quiz的url在项目url中
urlpatterns += [
    path('quiz/', include('quiz.urls')),
]

# 包含discussboard的url在项目url中
urlpatterns += [
    path('discussboard/', include('discussboard.urls')),
]


# 将根目录重定向至siteindex
urlpatterns += [
    path('', RedirectView.as_view(url='/siteindex/')),
]


# 静态文件支持
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 用户认证
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
