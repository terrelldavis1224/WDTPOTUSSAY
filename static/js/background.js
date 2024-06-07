
document.addEventListener('DOMContentLoaded', function() {
    window.onmousemove = function(e) {
        const percentX = (e.clientX / window.innerWidth) * 100;
        document.body.style.background = `linear-gradient(to right, rgb(232, 27, 35) ${percentX}%, rgb(0, 174, 243) ${percentX}%)`;
    };
});