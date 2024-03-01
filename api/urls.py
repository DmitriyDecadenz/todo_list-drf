from django.urls import path
from api.views import ApiOverview, TaskCreate, TaskDelete, TaskDetail,TaskList, TaskUpdate


urlpatterns = [
    path('', ApiOverview, name="api-overview"),
    path('task-list/', TaskList, name="task-list"),
    path('task-detail/<str:pk>/', TaskDetail, name="task-detail"),
    path('task-create/', TaskCreate, name='task-create'),

    path('task-update/<str:pk>/', TaskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', TaskDelete, name='task-delete'),  
]