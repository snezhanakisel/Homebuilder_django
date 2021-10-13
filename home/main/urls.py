from django.urls import path
from .views import *
from blog.views import *


urlpatterns = [
    path('', index, name='index'),
    path('project/', project, name='project'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('contact/', contact_us, name='contact_us'),
    path('blog/', ShowPostView.as_view(), name='blog'),
    path('user/<str:username>', UserAllPostView.as_view(), name='user_post'),
    path('blog/<int:pk>', PostDetailView.as_view(), name='blog_post'),
    path('blog/<int:pk>/comment/', PostCommentCreate.as_view(), name='post_comment'),
    path('blog/<int:pk>/update', UpdatePostView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='post-delete'),
    path('blog/add', CreatePostView.as_view(), name='post-add'),
    path('', index, name='mail')

]