from lib.todo import *

class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [item for item in self.todo_list if item.complete == False]
        # return filter(lambda item: item.complete == False, self.todo_list)

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [item for item in self.todo_list if item.complete == True]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for item in self.todo_list:
            item.mark_complete()
        