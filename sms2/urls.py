from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from _school.views import CustomTokenObtainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_token/', CustomTokenObtainView.as_view(), name='get_token'),
    # path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    # path('api/verify_token/', TokenVerifyView.as_view(), name='verify_token'),
    path('api/school/', include('_school.urls')),
    path('api/stuffs/', include('_stuff.urls')),
    path('api/teachers/', include('_teacher.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
