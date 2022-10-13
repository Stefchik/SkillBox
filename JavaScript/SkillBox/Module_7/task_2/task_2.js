document.addEventListener("DOMContentLoaded", function () {
  let input = document.createElement("input");
  document.body.append(input);
  let h2 = document.createElement("h2");
  document.body.append(h2);
  let timeout;
  
  function enteringText() {
    let text = input.value;
    if (timeout) {
      clearTimeout(timeout);
    }
    timeout = setTimeout(() => {
      h2.innerHTML = text;
    }, 300);
  }

   input.addEventListener("input", enteringText);
});