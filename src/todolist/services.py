class TodoService:
    def __init__(self):
        self.todos = []
        self.counter = 1
        
    def create_todo(self, todo):
        new_todo = {
            "id" : self.counter,
            "title" : todo.title,
            "completed" : todo.completed
            }
        
        self.todos.append(new_todo)
        self.counter +=1
        return new_todo
    
    def get_todos(self):
        return self.todos
        
    def update_todo(self, todo_id: int, updated_todo):
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["title"] = updated_todo.title
                todo["completed"] = updated_todo.completed
                return todo
        return None
    
    def delete_todo(self, todo_id: int):
        for index, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                return self.todos.pop(index)
        return None

    
    

