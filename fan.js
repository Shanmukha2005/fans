let on = document.getElementById("btn1");
let off = document.getElementById("btn2");
let b1 = document.getElementById("btn3");
let b2 = document.getElementById("btn4");
let b3 = document.getElementById("btn5");
let img = document.getElementById("image");

function onbtn() {
    img.style.animation = "rotate 4s infinite linear";
}

function offbtn() {
    img.style.animation = "none";
}

function speed1btn() {
    img.style.animation = "rotate 1s infinite linear";
}

function speed2btn() {
    img.style.animation = "rotate 0.5s infinite linear";
}

function speed3btn() {
    img.style.animation = "rotate 0.01s infinite linear";

}


