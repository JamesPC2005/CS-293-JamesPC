document.addEventListener("DOMContentLoaded", function () {
  
  const dropdown = document.getElementById("drop-down");

  
  dropdown.addEventListener("click", change_dropdown);
});

const fill = null

function change_dropdown(event) {
    let target = document.getElementById("target");
    if(target.innerHTML === ""){
        target.innerHTML = '<li><p>My 2025-2026 <a href="https://github.com/JamesPC2005/CS-293-JamesPC">web development</a>work for class</p></li><li><p>Some of my<a href="https://github.com/JamesPC2005/personal_projects">personal projects</a>from 2024-2025 </p></li>'
    }
}