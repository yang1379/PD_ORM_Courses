from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_course$', views.add_course),
    url(r'^(?P<course_id>\d+)/destroy_course$', views.destroy_course),
    url(r'^(?P<course_id>\d+)/destroy_course_confirmed$', views.destroy_course_confirmed),
    url(r'^$', views.index)
]