function calculate(cartTotal, numberItemsCart, promoCode = null) {
    if (promoCode === 'ДАРИМ300') {
        if (cartTotal < 300) {
            cartTotal = 0
        } else
            cartTotal -= 300
    }
    if (numberItemsCart >= 10) {
        cartTotal -= (cartTotal / 100) * 5
    }
    if (cartTotal > 50000) {
        cartTotal -= ((cartTotal - 50000) / 100) * 20
    }
    if (promoCode === 'СКИДКА15' && cartTotal >= 20000) {
        cartTotal -= (cartTotal / 100) * 15
    }
    return cartTotal
}
console.log(calculate(250, 20,'ДАРИМ300'))