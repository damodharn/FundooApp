from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Django Api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Fundooapi.urls')),
    path('schema_view/', schema_view)
]