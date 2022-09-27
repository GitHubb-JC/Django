from django.test import TestCase
from models import Todo

# Create your tests here.

### 1번 #################
### 1번 #################
### 1번 #################

import datetime
todo = Todo()
todo.content = "실습 제출"
todo.priority = 5
todo.deadline = datetime.date(2022, 9, 27)
todo.save()

### 2번 #################
### 2번 #################
### 2번 #################

todo = Todo.objects.order_by('id')
for todo in todo:
    print(todo.id)

### 3번 #################
### 3번 #################
### 3번 #################

todo = Todo.objects.order_by('-deadline')
for todo in todo:
    print(todo.deadline)

### 4번 #################
### 4번 #################
### 4번 #################

todo = Todo.objects.order_by('-priority')
for todo in todo:
    print(todo.priority)

### 5번 #################
### 5번 #################
### 5번 #################

todo = Todo.objects.filter(priority = 5)
todo = todo.order_by("id")
for todo in todo:
    print(todo.id, end=" ")
    print(todo.priority)

### 6번 #################
### 6번 #################
### 6번 #################

todo = Todo.objects.filter(completed = True)
todo = todo.order_by("id")
for todo in todo:
    print(todo.id, end=" ")
    print(todo.completed)

### 7번 #################
### 7번 #################
### 7번 #################

todo = Todo.objects.filter(priority = 5)
todo.count()

### 8번 #################
### 8번 #################
### 8번 #################

todo = Todo.objects.filter(id = 1)
print(todo)

### 9번 #################
### 9번 #################
### 9번 #################

todo = Todo.objects.get(id = 1)
todo.delete()

### 10번 #################
### 10번 #################
### 10번 #################

todo = Todo.objects.get(id = 10)
todo.priority = 5
todo.save()