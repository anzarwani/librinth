from unicodedata import name
from django.urls import path, include
#from . import views
from .views import HomeView, ArticleDetailView, MyPostView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView, PoemView, BookReviewView
urlpatterns = [
    #path('', views.home, name = 'home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('poems/', PoemView.as_view(), name='poems'),
    path('my_posts/', MyPostView.as_view(), name='my_posts'),
    path('book_reviews/', BookReviewView.as_view(), name='books'),
]