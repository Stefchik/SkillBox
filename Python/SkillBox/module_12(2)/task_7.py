from dataclasses import dataclass, field

@dataclass(order=True)
class TaskData:
    sort_index: int = field(init=False, repr=False)

    name: str
    index: int

    def __post_init__(self):
        self.sort_index = self.index

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: TaskData):
        self.items.append(item)

    def pop(self, index: int = -1):
        if len(self.items) == 0:
            return None
        return self.items.pop(index)

    def peek(self) -> TaskData:
        return self.items[-1]

    def is_empty(self) -> bool:
        return self.items == []

    def size(self) -> int:
        return len(self.items)

class TaskManager:
    stack = Stack()

    def __str__(self):
        result = ''
        old_index: int = 0
        if self.stack.size() == 0:
            result = 'empty stack'
        else:
            self.stack.items.sort()
            result += 'Результат:'
            for task in self.stack.items:
                if old_index == task.index:
                    result += f'; {task.name}'
                else:
                    result += f'\n{task.index} {task.name}'
                    old_index = task.index
        return result

    def new_task(self, name: str, index: int):
        self.stack.push(TaskData(name, index))

    def delete_task(self, name: str, index: int):
        index_element = 0
        for item in self.stack.items:
            if item.name == name and item.index == index:
                self.stack.pop(index_element)
                break
            index_element += 1

manager = TaskManager()
manager.new_task('Сделать уборку', 4)
manager.new_task('Помыть посуду', 4)
manager.new_task('Отдохнуть', 1)
manager.new_task('Поесть', 2)
manager.new_task('Сдать домашнее задание', 2)
print(manager)
manager.delete_task('Поесть', 2)
print(manager)
manager.delete_task('Отдохнуть', 1)
print(manager)
