from django.contrib import admin
from django.urls import path
from .views import *


# urlpatterns = {
#     path('blog/', ShowPostView.as_view(), name='blog'),
#     path('user/<str:username>', UserAllPostView.as_view(), name='user-post'),
#     # path('blog/<int:pk>', PostDetailView.as_view(), name='blog_post'),
#     path('blog/<int:pk>/update', UpdatePostView.as_view(), name='post-update'),
# #     path('blog/<int:pk>/delete', DeletePostView.as_view(), name='post-delete'),
# #     path('blog/add', CreatePostView.as_view(), name='post-add'),
# }