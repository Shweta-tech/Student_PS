from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'student', views.StudentAPI)
router.register(r'marks', views.MarkAPI)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api', views.UserViewSet.as_view()),
    path('api/<int:roll_no>/', views.UserViewSet.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]