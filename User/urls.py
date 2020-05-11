from django.contrib import admin
from django.urls import path,include
from UserDetail.views import Register,Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',Register),
    path('login/',Login),

]
