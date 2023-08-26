from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("publish/", views.publish, name="publish-form"),
    path("search/", views.search, name="search-page"),
    path("filtered-rides/", views.filter_rides, name="filter-page"),
    path("published-rides/", views.published_rides, name="published-rides-page"),
    path("published-rides/<ride_id>", views.delete_ride, name="delete-ride"),
    path("join/<int:ride_id>", views.join_ride, name="join-ride"),
    path("about/", views.about, name="about-page")
]
