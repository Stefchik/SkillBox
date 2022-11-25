(function () {
    function createAppTitle(title) {
        let appTitle = document.createElement('h2');
        appTitle.innerHTML = title;
        return appTitle;
    }

    function createTodoItemForm() {
        let form = document.createElement('form');
        let input = document.createElement('input');
        let buttonWrapper = document.createElement('div');
        let button = document.createElement('button');

        form.classList.add('input-group', 'mb-3');
        input.classList.add('form-control');
        input.placeholder = 'Введите название нового дела';
        buttonWrapper.classList.add('input-group-append');
        button.classList.add('btn', 'btn-primary');
        button.textContent = 'Добавить дело';

        buttonWrapper.append(button);
        form.append(input);
        form.append(buttonWrapper);

        return {
            form,
            input,
            button,
        };
    }

    function createTodoList() {
        let list = document.createElement('ul');
        list.classList.add('list-group');
        return list;
    }

    function createTodoItem(name) {
        let item = document.createElement('li');
        let buttonGroup = document.createElement('div');
        let doneButton = document.createElement('button');
        let deleteButton = document.createElement('button');

        item.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        item.textContent = name;

        buttonGroup.classList.add('btn-group', 'btn-group-sm');
        doneButton.classList.add('btn', 'btn-success');
        doneButton.textContent = 'Готово';
        deleteButton.classList.add('btn', 'btn-danger');
        deleteButton.textContent = 'Удалить';

        buttonGroup.append(doneButton);
        buttonGroup.append(deleteButton);
        item.append(buttonGroup);

        return {
            item,
            doneButton,
            deleteButton,
        };
    }

    function addEventOnButton(todoItem, keyPage, arrayTodoItems) {

        todoItem.doneButton.addEventListener('click', function () {
            todoItem.item.classList.toggle('list-group-item-success');
            let doneValue = todoItem.item.childNodes[0].nodeValue;
            arrayTodoItems.map(object => {
               if ( object['name'] === doneValue) object['done'] = todoItem.item.classList.contains('list-group-item-success');
            });
            localStorage.removeItem(keyPage);
            localStorage.setItem(keyPage, JSON.stringify(arrayTodoItems));
        });
        todoItem.deleteButton.addEventListener('click', function () {
            if (confirm('Вы уверены?')) {
                let removedValue = todoItem.item.childNodes[0].nodeValue;
                arrayTodoItems = arrayTodoItems.filter(object => object['name'] !== removedValue);
                todoItem.item.remove();
                localStorage.removeItem(keyPage);
                localStorage.setItem(keyPage, JSON.stringify(arrayTodoItems));
            }
        });
        return todoItem;
    }


    function createTodoApp(container, keyPage, title = 'Список дел', taskArray) {
        let arrayTodoItems = [];
        let todoAppTitle = createAppTitle(title);
        let todoItemForm = createTodoItemForm();
        let todoList = createTodoList();

        container.append(todoAppTitle);
        container.append(todoItemForm.form);
        container.append(todoList);

        if (taskArray) {
            for (let task in taskArray) {
                let todoItem = createTodoItem(taskArray[task]['name']);
                todoItem = addEventOnButton(todoItem, keyPage, arrayTodoItems);
                if (taskArray[task]['done'])
                    todoItem.item.classList.toggle('list-group-item-success');
                todoList.append(todoItem.item);
            }
        }

        if (localStorage.getItem(keyPage)) {
            let parsItems = JSON.parse(localStorage.getItem(keyPage));
            for (let task in parsItems) {
                arrayTodoItems.push(parsItems[task]);
                let todoItem = createTodoItem(parsItems[task]['name']);
                todoItem = addEventOnButton(todoItem, keyPage, arrayTodoItems);
                if (parsItems[task]['done'])
                    todoItem.item.classList.toggle('list-group-item-success');
                todoList.append(todoItem.item);
            }
        }

        todoItemForm.button.disabled = true;

        todoItemForm.form.addEventListener('input', function () {
            todoItemForm.button.disabled = !todoItemForm.input.value;
        })

        todoItemForm.form.addEventListener('submit', function (e) {
            e.preventDefault();

            let inputValue = todoItemForm.input.value;
            if (!inputValue) {
                return;
            }

            todoItemForm.button.disabled = true;
            let todoItem = createTodoItem(inputValue);
            todoItem = addEventOnButton(todoItem, keyPage, arrayTodoItems);

            todoList.append(todoItem.item);
            arrayTodoItems.push({name: inputValue, done: false})
            localStorage.setItem(keyPage, JSON.stringify(arrayTodoItems));
            todoItemForm.input.value = '';
        });
    }

    window.createTodoApp = createTodoApp;
})();