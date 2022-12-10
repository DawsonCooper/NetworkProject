
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.profile, name="profile"),

    # API routes
    path('like/<int:postId>', views.interaction_API, name="like"),
    path("get_user_interactions", views.get_user_interactions,
         name="get_user_interactions"),
    path('create_realationship', views.create_realationship,
         name="create_realationship"),
    path('get_post_data/<int:postId>', views.get_post_data, name="get_post_data"),
    path('update_post/<int:postId>', views.update_post, name="update_post"),
    path('update_interaction_count', views.update_interaction_count,
         name="update_interaction_count"),
    #path('edit_post', views.edit_post, name="edit_post"),
    path('get_posts/<int:postId>', views.get_posts, name="get_posts"),
]
# MEDIA routes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
