from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register("student", views.StudentAPI)
router.register("marks", views.MarksAPI)
print(views.MarksAPI)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/student/<int:roll_no>/', views.StudentAPI,name='stu_api'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]