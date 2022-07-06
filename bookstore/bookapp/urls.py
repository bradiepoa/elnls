from django.urls import path
from .import views

app_name = 'bookapp'
urlpatterns = [
# admin dashboard
path('index/', views.Homeview, name="dashboardpage"),

path('addbookform/', views.AddBookFormView, name="addbookpage"),

path('updatebook/<str:upd_bk>/', views.UpdateBook, name="updatebook"),
path('delete_book/<str:del_bk>/', views.DeleteBook, name="delete_book"),

path('addbookcategory/',views.AddBookCategory, name="addcategory"),

path('bkcategory/', views.BkCategory, name="Bkcategorypage"),

path('updatebkcategory/<str:upd_bkc>/', views.UpdateBkCategory, name="updatebkcategory"),

path('chat/', views.ChatDetails, name="chatdetailpage"),

path('logout/', views.LogoutUser, name="logout"),




# librariandash==========================
path('indexlb/', views.Homelbview, name='dashlibrarian'),


# students books
path('indexst/',views.Homestview, name='studentbookpage'),



path('', views.Loginview,name='loginpage'),

path('logout/',views.LogoutUser, name="logout"),

path('register/', views.Registeriew,name='registerpage'),


]