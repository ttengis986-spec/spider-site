const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let mouseX = 200;
let mouseY = 200;

window.addEventListener("mousemove", function(e){
    mouseX = e.clientX;
    mouseY = e.clientY;
    draw();
});

function draw(){

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // утас
ctx.strokeStyle = "white";
ctx.lineWidth = 1.5;
ctx.beginPath();
ctx.moveTo(mouseX, 0);
ctx.lineTo(mouseX, mouseY - 20);
ctx.stroke();

// хөл
ctx.strokeStyle = "black";
ctx.lineWidth = 2;

// legs
for (let i = -2; i <= 2; i++) {
    if (i === 0) continue;

    ctx.beginPath();
    ctx.moveTo(mouseX - 5, mouseY + i * 5);
    ctx.lineTo(mouseX - 15, mouseY + i * 6);
    ctx.lineTo(mouseX - 30, mouseY + i * 4);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(mouseX + 5, mouseY + i * 5);
    ctx.lineTo(mouseX + 15, mouseY + i * 6);
    ctx.lineTo(mouseX + 30, mouseY + i * 4);
    ctx.stroke();
}

// бие
ctx.fillStyle = "red";
ctx.beginPath();
ctx.arc(mouseX, mouseY, 10, 0, Math.PI * 2);
ctx.fill();

    // body
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 10, 0, Math.PI * 2);
    ctx.fill();

    // head
    ctx.beginPath();
    ctx.arc(mouseX, mouseY - 14, 6, 0, Math.PI * 2);
    ctx.fill();
}

draw();