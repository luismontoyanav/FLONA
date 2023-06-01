from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from api.v1.users.views import EmployeesView

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("employees/", EmployeesView.as_view(), name="employees")
]
