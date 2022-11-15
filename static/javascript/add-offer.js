document.getElementById('description').addEventListener("input", function (event) {
    document.getElementById('length-counter').textContent = 5000 - this.value.length + "/5000";
});