from . import views
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')
# from rest_framework.documentation import include_docs_urls

# app_name = 'accounts'
urlpatterns = [
    path('', views.reg, name='reg'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('activate/<token>/', views.activate, name='activate'),
    path('delete', views.delete, name='delete'),
    path('forget', views.forget, name='forget'),
    path('reset/<token>/', views.reset, name='reset'),
    # path('swagger_docs/', schema_view),
    # path('docs/', include_docs_urls(title='django API')),

]