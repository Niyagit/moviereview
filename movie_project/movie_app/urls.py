
from django.urls import include, path
from .import views

from django.contrib.auth import views as userViews
urlpatterns = [
    path('home/', views.index, name='home'),
    path('login/', views.user_login, name='login'),

      

    path('', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_profile/',views.UpdateUserView.as_view(),name='edit_user'),
    path('movie/<int:Movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addreview/<int:id>', views.add_review, name='add_review'),
    path('editreview/<int:movie_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:movie_id>/<int:review_id>/', views.delete_review, name="delete_review"),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
     path("search/", views.SearchResultsView.as_view(), name="search_results"),

]