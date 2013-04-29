// inner variables
var clockRadius = 100;

// draw functions :
function clear(ctx) { // clear canvas function
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function drawScene(canvas, ctx, clockImage, diff) { // main drawScene function
    clear(ctx); // clear canvas

    // get current time
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    hours = hours > 12 ? hours - 12 : hours;
    var diff_hours = Math.floor(diff/60);
    var diff_minutes = diff % 60;
    var hour = hours + minutes / 60 + diff_hours;

    var minute = minutes + seconds / 60 + diff_minutes;

    // save current context
    ctx.save();

    // draw clock image (as background)
    ctx.drawImage(clockImage, 0, 0, 200, 200);

    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.beginPath();

    // draw numbers
    ctx.font = '14px Arial';
    ctx.fillStyle = '#000';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    for (var n = 1; n <= 12; n++) {
        var theta = (n - 3) * (Math.PI * 2) / 12;
        var x = clockRadius * 0.7 * Math.cos(theta);
        var y = clockRadius * 0.7 * Math.sin(theta);
        ctx.fillText(n, x, y);
    }

    // draw hour
    ctx.save();
    var theta = (hour - 3) * 2 * Math.PI / 12;
    ctx.rotate(theta);
    ctx.beginPath();
    ctx.moveTo(-15, -5);
    ctx.lineTo(-15, 5);
    ctx.lineTo(clockRadius * 0.5, 1);
    ctx.lineTo(clockRadius * 0.5, -1);
    ctx.fill();
    ctx.restore();

    // draw minute
    ctx.save();
    var theta = (minute - 15) * 2 * Math.PI / 60;
    ctx.rotate(theta);
    ctx.beginPath();
    ctx.moveTo(-15, -4);
    ctx.lineTo(-15, 4);
    ctx.lineTo(clockRadius * 0.8, 1);
    ctx.lineTo(clockRadius * 0.8, -1);
    ctx.fill();
    ctx.restore();

    // draw second
    //ctx.save();
    //var theta = (seconds - 15) * 2 * Math.PI / 60;
    //ctx.rotate(theta);
    //ctx.beginPath();
    //ctx.moveTo(-15, -3);
    //ctx.lineTo(-15, 3);
    //ctx.lineTo(clockRadius * 0.9, 1);
    //ctx.lineTo(clockRadius * 0.9, -1);
    //ctx.fillStyle = '#0f0';
    //ctx.fill();
    //ctx.restore();

    ctx.restore();
}

