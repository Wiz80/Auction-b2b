"""auctionb2b URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from auction_views import views as ab2b_views
from usuarios import views as user_views
from Payments import views as pay_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ab2b_views.index, name = "index"),
    path('login/', user_views.login_view, name = "login"),
    path('logout/', user_views.logout_view, name = "logout"),
    path('signup/', user_views.signup, name = "signup"),
    path('subastar_step_1/', user_views.subastar_step_1, name = "subastar_1"),
    path('subastar_step_2/<int:id>/', user_views.subastar_step_2, name = "subastar_2"),
    path('subastar_step_3/<int:id>/', user_views.subastar_step_3, name = "subastar_3"),
    path('subastar_step_4/<int:id>/', user_views.subastar_step_4, name = "subastar_4"),
    path('subastar_step_5/<int:id>/', user_views.subastar_step_5, name = "subastar_5"),
    path('subastar_step_6/<int:id>/', user_views.subastar_step_6, name = "subastar_6"),
    path('subastar_step_7/<int:id>/', user_views.subastar_step_7, name = "subastar_7"),
    path('vehiculo/<int:pk_vehiculo>/', ab2b_views.vehiculo, name = "vehiculo"),
    path('creditos/', pay_views.comprar_creditos, name = "creditos"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
