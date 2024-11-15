// static/js/app.js

// Function to send the user's mood and get the recommendations using XMLHttpRequest
function getRecommendations() {
    var mood = document.getElementById('moodInput').value;  // Get the mood from the input field
    var xhr = new XMLHttpRequest();  // Create a new XMLHttpRequest object
    xhr.open('POST', '/get_recommendations', true);  // Configure the request (POST to /get_recommendations)

    // Set up the callback to handle the response
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);  // Parse the JSON response

            var recommendationsList = document.getElementById('recommendationsList');
            recommendationsList.innerHTML = '';  // Clear the previous recommendations

            // Display the new recommendations
            response.recommendations.forEach(function(song) {
                var li = document.createElement('li');
                li.textContent = song;  // Add the song name to the list
                recommendationsList.appendChild(li);
            });
        }
    };

    // Send the data (user mood) with the request
    var data = new FormData();
    data.append('mood', mood);  // Add the mood to the form data
    xhr.send(data);  // Send the request with the form data
}
