from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from seven.views import ClienteViewSet
from corsheaders.defaults import default_headers


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'my-custom-header',
]