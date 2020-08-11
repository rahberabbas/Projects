from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('my_admin_ncs/', admin.site.urls),
    path('',include('cont.urls'))
]