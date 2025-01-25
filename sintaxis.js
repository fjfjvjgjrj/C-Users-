const launchButton = document.getElementById("launchButton");

launchButton.addEventListener("click", () => {
    setTimeout(() => {
            launchButton.textContent = "Запуск через 3...";
            launchButton.style.backgroundColor = "#f39c12";
            launchButton.style.border = "2px solid #d35400";

            setTimeout(() => {
                launchButton.textContent = "Запуск через 2...";

                setTimeout(() => {
                    launchButton.textContent = "Запуск через 1...";

                setTimeout(() => {
                    launchButton.textContent = "Підтверджено: запуск ракети!";
                    launchButton.style.backgroundColor = "#e74c3c";
                    launchButton.style.color = "#ffffff";
                    launchButton.style.border = "2px solid #c0392b";
                }, 1000);
            }, 1000);
        }, 1000);
    }, 1000);
});






