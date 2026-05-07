document.addEventListener("DOMContentLoaded", function () {
  
    const dropdown = document.getElementById("drop-down");
    document.getElementById("header").style.backgroundImage = "url('Images/mainscreen.png')";
  
    dropdown.addEventListener("click", change_dropdown);
});

console.log("js loading")
function change_dropdown() {
    const target = document.getElementById("target");
    const dropdown = document.getElementById("drop-down")
    /*console.log("click")*/

    if (target.classList.contains("open")) {
        dropdown.innerHTML=(`My Projects <`)
        target.classList.remove("open");

    } else {
        dropdown.innerHTML=(`My Projects V`);
        target.classList.add("open");
    }
}