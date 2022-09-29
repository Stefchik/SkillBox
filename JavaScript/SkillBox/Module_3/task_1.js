function CheckPassword(password){
    if (password.length >= 4 && (password.includes('_') || password.includes('-'))) {
        console.log('Пароль надежный')
    } else {
        console.log('Пароль недостаточно надежный')
    }
}
CheckPassword('1234-')
CheckPassword('4321_')
CheckPassword('qaz-xsw')
CheckPassword('_zxd')
CheckPassword('_-a')
CheckPassword('qaz')
CheckPassword('_-3')
CheckPassword('123456789')
