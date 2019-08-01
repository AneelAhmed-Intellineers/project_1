from django.urls import path


from .views import IndexCreateView,ResultcreateView


app_name = 'app'
urlpatterns = [
    path('student/', IndexCreateView.as_view(), name='index'),
    path('result/', ResultcreateView.as_view(), name='detail'),
    path('thanks/', IndexCreateView.thanks),
    #path('<int:student_id>/', views.result, name='result'),
]
