function WordCorrection(userName, userSurname) {    
    let firstLetterName = userName.substring(0, 1)
    let firstLetterSurname = userSurname.substring(0, 1)
    let restWordName =  userName.substring(1)
    let restWordSurname =  userSurname.substring(1)
    let correctFirstLetterName = firstLetterName.toUpperCase()
    let correctFirstLetterSurname = firstLetterSurname.toUpperCase()
    let correctRestWordName = restWordName.toLowerCase()
    let correctRestWordSurname = restWordSurname.toLowerCase()
    console.log('Правильное имя:', correctFirstLetterName + correctRestWordName) 
    console.log('Правильная фамилия:', correctFirstLetterSurname + correctRestWordSurname)
    let name = correctFirstLetterName + correctRestWordName !== userName ? console.log('Имя было преобразовано') : console.log('Имя осталось без изменений')
    let Surname = correctFirstLetterSurname + correctRestWordSurname !== userName ? console.log('Фамилия была преобразована') : console.log('Фамилия осталась без изменений')
}
WordCorrection('СтеПАН', 'РЯСин')
WordCorrection('никита', 'Колчин')