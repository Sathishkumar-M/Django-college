from django.conf.urls import url
from .views import StudentAPIView, StudentRudView,CourseAPIView

urlpatterns = [
    url(r'^$',StudentAPIView.as_view(),name='post-create'),
    url(r'^(?P<pk>\d+)/$',StudentRudView.as_view(),name='post-rud'),
    url(r'^course/$',CourseAPIView.as_view(),name='course-list'),
]
