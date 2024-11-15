document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("recommendButton");
    if (button) {
        button.addEventListener("click", getRecommendations);
    } else {
        console.error("Button not found!");
    }
});

function getRecommendations() {
    console.log("Button clicked!");  // Temporary test log to verify function is called
    var mood = document.getElementById('moodInput').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/get_recommendations', true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            var recommendationsList = document.getElementById('recommendationsList');
            recommendationsList.innerHTML = '';

            response.recommendations.forEach(function(song) {
                var li = document.createElement('li');
                li.textContent = song;
                recommendationsList.appendChild(li);
            });
        }
    };

    var data = new FormData();
    data.append('mood', mood);
    xhr.send(data);
}
