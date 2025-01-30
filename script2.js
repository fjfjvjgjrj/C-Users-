const songs = ["red", "blue", "green", "yellow", "purple"];

const button = document.getElementById("randomColorButton");
const result = document.getElementById("randomColor");

button.addEventListener("click", () => {
    const randomIndex = Math.floor(Math.random() * songs.length);
    result.style.backgroundColor = songs[randomIndex];
});
