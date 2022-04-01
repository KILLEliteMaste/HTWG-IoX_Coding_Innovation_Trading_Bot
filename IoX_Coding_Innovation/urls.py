"""IoX_Coding_Innovation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers
from IoX_Coding_Innovation.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'binance', views.snippet_detail)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('binance/tickers/', views.get_all_tickers),
    path('binance/ticker/', views.get_symbol_ticker),
    path('binance/symbol/', views.get_symbol_info),
    path('binance/account/', views.get_account_info),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#    path('admin/', admin.site.urls),
# ]
