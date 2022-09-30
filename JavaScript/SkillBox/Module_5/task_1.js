function filter(emails = [], blackListEmails = []) {
    let trueEmails = [];
    for (let item of emails) {
      if (!blackListEmails.includes(item)) {
          trueEmails.push(item);
      }
    }
    return trueEmails;
}
console.log(filter(["ryasin2002@gmail.com", "ryasin2015@yandex.ru", "Stepan.Riasin@urfu.me"],
["Ryasin2002@gmail.com", "ryasin2015@yandex.ru", "StepanRiasin@urfu.me"]));

