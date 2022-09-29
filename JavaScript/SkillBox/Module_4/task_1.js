function array(n, m, count) {
    let arrayGenerator = []
    for (let i = 0; i < count; i++){
        arrayGenerator.push(Math.round(Math.random() * Math.abs(m - n) + Math.min(n, m)))
    }
    console.log(arrayGenerator)
}
array(0, 100, 100)
array(2, 5, 50)
array(100, -5, 70)
array(-3, -10, 42)
