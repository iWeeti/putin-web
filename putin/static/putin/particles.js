var canvas = document.querySelector('.particles');
var c = canvas.getContext('2d');

var mouse = {
    x: innerWidth / 2,
    y: innerHeight / 2
};

addEventListener('resize', event => {
    init();
});

addEventListener('mousemove', event => {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
});

function randomFromRange(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}

function distance(x1, y1, x2, y2) {
    var xd = x1 - x2;
    var yd = y1 - y2;
    return Math.sqrt(Math.pow(xd, 2) + Math.pow(yd, 2));
}

function Circle(x, y, radius, id) {
    this.x = x;
    this.y = y;
    this.vx = randomFromRange(-3, 3);
    this.vy = randomFromRange(-3, 3);
    this.id = id;
    this.radius = radius;
    this.originalRadius = radius;

    this.draw = () => {
        c.beginPath();
        c.fillStyle = '#7289DA';
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
        c.closePath();
        c.fill();
    };

    this.update = () => {
        if (this.vx === 0) {
            this.vx = randomFromRange(-3, 3);
        }

        if (this.vy === 0) {
            this.vy = randomFromRange(-3, 3);
        }

        this.x += this.vx;
        this.y += this.vy;

        if (
            distance(this.x, this.y, mouse.x, mouse.y) <= 120 &&
            this.radius <= 30
        ) {
            this.radius++;
        } else if (this.radius >= this.originalRadius) {
            this.radius--;
        }

        if (this.x + this.radius > innerWidth || this.x - this.radius <= 0) {
            this.vx = -this.vx;
        }

        if (this.y + this.radius > innerHeight || this.y - this.radius <= 0) {
            this.vy = -this.vy;
        }

        this.draw();
    };
}

var circles;

function init() {
    circles = [];
    c.canvas.width = window.innerWidth;
    c.canvas.height = window.innerHeight;
    for (var i = 0; i < 100; i++) {
        var x = Math.round(Math.random() * innerWidth);
        var y = Math.round(Math.random() * innerHeight);
        var radius = randomFromRange(2, 4);
        circles.push(new Circle(x, y, radius, i));
    }
    console.log(randomFromRange(2, 4));
}

function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0, 0, innerWidth, innerHeight);
    circles.forEach(circle => {
        circle.update();
    });
}

init();
animate();
