from django.urls import path

from blog.api_views import post_detail, post_list

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>", post_detail, name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)