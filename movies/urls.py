from django.urls import path
from . import views
 
app_name = "movies"

urlpatterns = [
   path('', views.movies, name="movies"),
   path('logout', views.logout_user, name="logout"),
   path('login', views.loginPage, name="login"),
   path('register', views.register_user, name="register"),
   path('search', views.find_movie,name="search"),
   path('show/<pk>/', views.movie_details, name="single"),
   # path('cart', views.add_to_cart,name="cart"),
   path('add_movie/',views.add_movie,name="addmovie"),
   path('add_movie_action/',views.add_movie_action,name="add_movie_action"),
   path('add_screening/',views.add_screening,name="addscreening"),
   path('add_movie_action/',views.add_screening_action,name="add_screening_action"),
   path('add_hall/',views.add_hall,name="addhall"),
   path('add_movie_action/',views.add_hall_action,name="add_hall_action"),
   path('delete_movie/',views.delete_movie,name="delete_movie"),




]
