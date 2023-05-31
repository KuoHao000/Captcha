const button = document.getElementById("toggle");
const body = document.querySelector("body");





button.onclick = function(){
    button.classList.toggle('dark');
    body.classList.toggle('dark');
}