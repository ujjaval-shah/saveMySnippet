"""saveMySnippet URL Configuration

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
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/language/all/', get_languages),
    path('api/language/create/all/', create_languages),
    path('api/tag/<int:id>/', get_tag),
    path('api/tag/<int:id>/delete/', delete_tag),
    path('api/tag/all/', get_tags),
    path('api/tag/create/', create_tag),
    path('api/tag/update/', update_tag),
    path('api/snip/<int:id>/', get_snip),
    path('api/snip/all/', get_snips),
    path('api/snip/create/', create_snip),
    path('api/snip/<int:id>/delete/', delete_snip),
    path('api/snip/<int:id>/pin/', pin_snip),
    path('api/snip/<int:id>/unpin/', unpin_snip),
    path('api/snip/update/', update_snip),
    path('api/snip/all/whose_tag/<int:id>/', get_snips_by_tag),
]
