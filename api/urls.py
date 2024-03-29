from django.urls import path
from api.views import CompanyList, CompanyDetail, RoleList, RoleDetail, SidebarItemList, SidebarItemDetail, SidebarList, SidebarDetail, RegisterView, ChangePasswordView, UpdateProfileView, CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenBlacklistView

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company_list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('roles/', RoleList.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetail.as_view(), name='role_detail'),
    path('sidebar_items/', SidebarItemList.as_view(), name='sidebar_item_list'),
    path('sidebar_items/<int:pk>/', SidebarItemDetail.as_view(), name='sidebar_item_detail'),
    path('companies/<int:company>/roles/<int:role>/sidebar/', SidebarList.as_view(), name='sidebar_list'),
    path('companies/<int:company>/roles/<int:role>/sidebars/<int:pk>/', SidebarDetail.as_view(), name='sidebar_detail'),
    path('sidebars/<int:pk>/', SidebarDetail.as_view(), name='sidebar_detail'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='token_blacklist'),
]
