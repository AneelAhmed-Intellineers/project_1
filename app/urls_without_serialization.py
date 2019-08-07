from django.urls import path


from .views import StudentRegisterationCreateView, StudentDetailView,thanks, ResultFormView,ResultDetailView,StudentListView,SearchResultView
from .views import StudentUpdateView, CreateStudentUpdate, CreateStudentDelete, StudentDeleteView

app_name = 'app'
urlpatterns = [
    path('', StudentRegisterationCreateView.as_view(), name='student_registeration'),
    path('search/', ResultFormView.as_view(), name='result_search'),
    path('<int:pk>/',StudentDetailView.as_view(), name='student_detail'),
    path('thanks/', thanks, name='thanks'),
    path ('view_result/<str:enrollment>', ResultDetailView.as_view(), name='resultview'),
    path('students/', StudentListView.as_view(), name='studentlist'),
    path('student_update/',CreateStudentUpdate.as_view(), name='Student_update_view'),
    path('student_update/<str:enrollment>',StudentUpdateView.as_view(), name='Student_updateview_detail'),
    path('student_delete/', CreateStudentDelete.as_view(), name='student_delete'),
    path('student_delete/<str:enrollment>', StudentDeleteView.as_view(), name='student_delete_view'),
    path('student_delete/deleted/', StudentDeleteView.deleted_data, name='deleted_data'),
    #path('<int:student_id>/', views.result, name='result'),
]
