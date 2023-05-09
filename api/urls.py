from django.urls import path
from api.views import CompanyList, CompanyDetail, RoleList, RoleDetail, SidebarItemList, SidebarItemDetail

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company_list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('roles/', RoleList.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetail.as_view(), name='role_detail'),
    path('sidebar_items/', SidebarItemList.as_view(), name='sidebar_item_list'),
    path('sidebar_items/<int:pk>/', SidebarItemDetail.as_view(), name='sidebar_item_detail'),
]
