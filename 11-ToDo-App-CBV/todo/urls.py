from django.urls import path
from .views import TodoCreate, TodoList, home, todo_create, todo_update, todo_delete
from .models import Todo
from django.views.generic import ListView

urlpatterns = [
    path("", home, name="home"),
    path("add/", todo_create, name="add"),
    path("adds/", TodoCreate.as_view()),
    path('list/',TodoList.as_view(),name="list"),
    path('lists/', ListView.as_view(model = Todo,context_object_name = 'todos')),
    path("update/<int:id>", todo_update, name="update"),
    path("delete/<int:id>", todo_delete, name="delete"),
]
