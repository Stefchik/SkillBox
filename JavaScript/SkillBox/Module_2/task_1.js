function square(x1, y1, x2, y2){
    let side1 = Math.abs(x1 - x2)
    let side2 = Math.abs(y1 - y2)
    let S = side1 * side2
    console.log('Площадь равна:',S)
}
square(2, 3, 10, 5)
square(10, 5, 2, 3)
square(-5, 8, 10, 5)
square(5, 8, 5, 5)  
square(8, 1, 5, 1)
