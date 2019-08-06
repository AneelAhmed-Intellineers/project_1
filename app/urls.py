from django.urls import path


from .views import StudentRegisterationCreateView, StudentDetailView,thanks, ResultFormView,ResultDetailView,StudentListView,SearchResultView


app_name = 'app'
urlpatterns = [
    path('', StudentRegisterationCreateView.as_view(), name='student'),
    path('result/', ResultFormView.as_view(), name='result'),
    path('<int:pk>/',StudentDetailView.as_view(), name='student_detail'),
    path('thanks/', thanks, name='thanks'),
    path ('view_result/<str:enrollment>', ResultDetailView.as_view(), name='resultview'),
    path('student_list/', StudentListView.as_view(), name='studentlist'),
    path('test/<str:name>',SearchResultView.as_view(),name='search'),
    #path('<int:student_id>/', views.result, name='result'),
]
