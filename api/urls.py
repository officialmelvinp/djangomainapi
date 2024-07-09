from django.urls import path
from .views import StudentListEndpoint


urlpatterns=[
    path('students', StudentListEndpoint.as_view(), name="students"),
    path('students/<int:id>/', StudentListEndpoint.as_view(), name="studemts_with_params")
]