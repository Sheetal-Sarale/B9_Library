from django.urls import path
from cbv_app.views import NewView,EmployeeCreate,EmployeeList, EmployeeDetail
urlpatterns = [
    path('new-cview/', NewView.as_view()),
    path('emp-create/', EmployeeCreate.as_view()),
    path('emp-list/',EmployeeList.as_view()),
    path('emp-view/<pk>/', EmployeeDetail.as_view()),
]