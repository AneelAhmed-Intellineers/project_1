from django.urls import path


from .views import IndexCreateView, CreateDetailView,thanks, ResultCreateView,ResultDetailView


app_name = 'app'
urlpatterns = [
    path('student/', IndexCreateView.as_view(), name='index'),
    path('result/', ResultCreateView.as_view(), name='result'),
    path('<int:pk>/',CreateDetailView.as_view(), name='detail'),
    path('thanks/', thanks, name='thanks'),
    path ('view/<str:enrollment>', ResultDetailView.as_view(), name='resultview'),
    #path('<int:student_id>/', views.result, name='result'),
]
