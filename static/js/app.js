document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("recommendButton");
    if (button) {
        button.addEventListener("click", getRecommendations);
    } else {
        console.error("Button not found!");
    }

    // Fetch default recommendations on page load
    fetchDefaultRecommendations();
});

function fetchDefaultRecommendations() {
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
                title.textContent = song.song_title;
                title.className = 'song-title';
                
                var artist = document.createElement('p');
                artist.textContent = song.artist;
                artist.className = 'song-artist';
                
                var album = document.createElement('p');
                album.textContent = song.album_name;
                album.className = 'song-album';
                
                var thumbnail = document.createElement('img');
                thumbnail.src = song.thumbnail;
                thumbnail.alt = "Album Cover";
                thumbnail.className = 'thumbnail';

                // Append all elements to the list item
                li.appendChild(thumbnail);
                li.appendChild(title);
                li.appendChild(artist);
                li.appendChild(album);

                recommendationsList.appendChild(li);
            });
        }
    };

    var data = new FormData();
    data.append('mood', 'default'); // You can change this to a default mood if needed
    xhr.send(data);
}

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
                title.textContent = song.song_title;
                title.className = 'song-title';
                
                var artist = document.createElement('p');
                artist.textContent = song.artist;
                artist.className = 'song-artist';
                
                var album = document.createElement('p');
                album.textContent = song.album_name;
                album.className = 'song-album';
                
                var thumbnail = document.createElement('img');
                thumbnail.src = song.thumbnail;
                thumbnail.alt = "Album Cover";
                thumbnail.className = 'thumbnail';

                // Append all elements to the list item
                li.appendChild(thumbnail);
                li.appendChild(title);
                li.appendChild(artist);
                li.appendChild(album);

                recommendationsList.appendChild(li);
            });
        }
    };

    var data = new FormData();
    data.append('mood', mood);
    xhr.send(data);
}
