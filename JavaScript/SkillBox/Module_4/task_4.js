let array = []
let days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье',]
for (let i = 1; i <= 31; i++) {
    array.push(`${i} января, ${days[i % 7]}`)
}
console.log(array)