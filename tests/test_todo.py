from lib.todo   import *
from lib.todo_list import *

"""
1. 
Create a task and instance of todo in todo_list
Check adds to list
"""
def test_todo_and_todo_list_instantiates():
    lst = TodoList()
    assert lst.todo_list == []

"""
2. 
Add a task to the todo_list
Check adds to list works
"""
def test_todo_adds_to_list():
    lst = TodoList()
    task_1 = Todo('Do shopping')
    lst.add(task_1)
    assert lst.todo_list == [task_1]
"""
3. 
Checks which tasks are incomplete
"""
def test_incomplete():
    lst = TodoList()
    task_1 = Todo('Do shopping')
    task_2 = Todo('Go dancing')
    lst.add(task_1)
    lst.add(task_2)
    expected_result = [task_1, task_2]
    actual_result = lst.incomplete()
    assert expected_result == actual_result

"""
4.
Marks tasks as complete and returns list
"""
def test_complete():
    lst = TodoList()
    task_1 = Todo('Do shopping')
    task_2 = Todo('Go dancing')
    lst.add(task_1)
    lst.add(task_2)
    task_2.mark_complete()
    expected = [task_2]
    actual = lst.complete()
    assert expected == actual

"""
5.
Marks all tasks as complete
"""
def test_give_up():
    lst = TodoList()
    task_1 = Todo('Do shopping')
    task_2 = Todo('Go dancing')
    lst.add(task_1)
    lst.add(task_2)
    lst.give_up()
    expected = [task_1, task_2]
    actual = lst.complete()
    assert expected == actual