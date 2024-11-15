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
                
                // Create elements for each attribute
                var title = document.createElement('p');
                title.textContent = "Title: " + song.song_title;
                
                var artist = document.createElement('p');
                artist.textContent = "Artist: " + song.artist;
                
                var album = document.createElement('p');
                album.textContent = "Album: " + song.album_name;
                
                var thumbnail = document.createElement('img');
                thumbnail.src = song.thumbnail;
                thumbnail.alt = "Album Cover";
                thumbnail.style.width = "50px"; // Adjust thumbnail size if needed

                var link = document.createElement('a');
                link.href = song.uri;
                link.textContent = "Listen on Spotify";
                link.target = "_blank";  // Open link in a new tab

                // Append all elements to the list item
                li.appendChild(thumbnail);
                li.appendChild(title);
                li.appendChild(artist);
                li.appendChild(album);
                li.appendChild(link);

                recommendationsList.appendChild(li);
            });
        }
    };

    var data = new FormData();
    data.append('mood', mood);
    xhr.send(data);
}

