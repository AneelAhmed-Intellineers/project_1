from django.urls import path


from . import views 


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.detail, name='detail'),
    path('thanks/', views.thanks),
    #path('<int:student_id>/', views.result, name='result'),
]
