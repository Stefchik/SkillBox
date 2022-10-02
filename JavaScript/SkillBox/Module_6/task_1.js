let objects = [
    { name: 'Василий', surname: 'Васильев'},
    { name: 'Иван', surname: 'Иванов'},
    { name: 'Пётр', surname: 'Петров'}
    ]
function filter (objects, key, value) {
    let newObjects = []
    for (let i = 0; i < objects.length; i++) {
        let obj = objects[i]
        if (obj[key] === value) newObjects.push(obj)
    }
    return newObjects
}
let result = filter(objects, 'name', 'Иван')
console.log(result)