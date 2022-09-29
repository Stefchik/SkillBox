function reverseStr(line) {
    let reverseLine = ''
    for (let i = 0; i < line.length; i++){
        reverseLine += line[(line.length - 1) - i]
    }
    console.log(reverseLine)
}    
reverseStr("'Привет мир!'")
reverseStr("'1'")
reverseStr("''")
