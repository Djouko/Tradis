
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("n/login", views.login_view, name="login"),
    path("n/logout", views.logout_view, name="logout"),
    path("n/register", views.register, name="register"),
    path("<str:username>", views.profile, name='profile'),
    path("n/following", views.following, name='following'),
    path("n/saved", views.saved, name="saved"),
    path("n/createpost", views.create_post, name="createpost"),
    path("n/post/<int:id>/like", views.like_post, name="likepost"),
    path("n/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("n/post/<int:id>/save", views.save_post, name="savepost"),
    path("n/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("n/post/<int:post_id>/comments", views.comment, name="comments"),
    path("n/post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path("n/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("n/post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path("a/home/<int:id>/", views.home, name="home"),
    path("a/about/<int:id>/", views.about, name="about"),
    path("a/booking/<int:id>/", views.booking, name="booking"),
    path("a/contact/<int:id>/", views.contact, name="contact"),
    path("a/destination/<int:id>/", views.destination, name="destination"),
    path("a/package/<int:id>/", views.package, name="package"),
    path("a/service/<int:id>/", views.service, name="service"),
    path("a/team/<int:id>/", views.team, name="team"),
    path("a/testimonial/<int:id>/", views.testimonial, name="testimonial"),
    path("a/404", views.l404, name="404")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

