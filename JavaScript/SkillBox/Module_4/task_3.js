let roodMines = [true, true, true, true, true, true, true, true, true, true] 
let lives = 2
for (let position = 0; position < roodMines.length; ++position) {
    console.log(`танк переместился на ${position + 1}`)
    if (roodMines[position] === true && lives > 1) {
        lives -= 1
        console.log(`танк повреждён`)
    } else if (roodMines[position] === true && lives > 0) {
        lives -= 1
        console.log(`танк уничтожен`)
        break
    }
}    
