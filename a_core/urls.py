from django.contrib import admin
from django.urls import path, include
from a_posts.views import *
from a_users.views import *

# for media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # for theboss
    # path('admin/', admin.site.urls),    
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('theboss/', admin.site.urls),
    path('accounts/', include('allauth.urls')),   # for django-allauth
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),      
    path('post/create/', post_create_view, name='post-create'),
    path('post/delete/<pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<pk>/', post_edit_view, name='post-edit'),
    path('post/<pk>/', post_page_view, name='post'),
    path('post/like/<pk>/', like_post, name='like-post'),
    path('comment/like/<pk>/', like_comment, name='like-comment'),
    path('reply/like/<pk>/', like_reply, name='like-reply'),
    path('profile/', profile_view, name='profile'),
    path('<username>/', profile_view, name='userprofile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/delete/', profile_delete_view, name='profile-delete'),
    path('profile/onboarding/', profile_edit_view, name="profile-onboarding"),
    path('profile/verify-email/', profile_verify_email, name="profile-verify-email"),
    path('commentsent/<pk>/', comment_sent, name="comment-sent"),
    path('comment/delete/<pk>/', comment_delete_view, name='comment-delete'),
    path('replysent/<pk>/', reply_sent, name='reply-sent'), 
    path('reply/delete/<pk>/', reply_delete_view, name='reply-delete'),
    # path('_/', include('a_landingpages.urls')),      
]

# for media
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)