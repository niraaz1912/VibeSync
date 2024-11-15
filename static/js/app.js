document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("recommendButton");
    const moodInput = document.getElementById('moodInput');
    
    if (button) {
        button.addEventListener("click", () => getRecommendations(moodInput.value));
    } else {
        console.error("Recommend button not found!");
    }
});

function getRecommendations(mood) {
    // Show loading indicator
    showLoading(true);
    
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/get_recommendations', true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            // Hide loading indicator
            showLoading(false);
            
            if (xhr.status == 200) {
                const response = JSON.parse(xhr.responseText);
                displayRecommendations(response.recommendations);
            } else {
                console.error("Error fetching recommendations:", xhr.statusText);
            }
        }
    };

    const data = new FormData();
    data.append('mood', mood);
    xhr.send(data);
}

function showLoading(isLoading) {
    const recommendationsList = document.getElementById('recommendationsList');
    recommendationsList.innerHTML = ''; // Clear previous recommendations
    
    if (isLoading) {
        const loadingMessage = document.createElement('p');
        loadingMessage.textContent = "Loading recommendations...";
        loadingMessage.classList.add('loading');
        recommendationsList.appendChild(loadingMessage);
    }
}

function displayRecommendations(recommendations) {
    const recommendationsList = document.getElementById('recommendationsList');
    
    if (recommendations.length === 0) {
        recommendationsList.innerHTML = "<p>No recommendations found.</p>";
        return;
    }

    recommendations.forEach(function(song) {
        const li = document.createElement('li');
        
        // Create elements for each attribute
        const title = document.createElement('p');
        title.textContent = song.song_title;
        title.classList.add('song-title');
        
        const artist = document.createElement('p');
        artist.textContent = song.artist;
        artist.classList.add('song-artist');
        
        const album = document.createElement('p');
        album.textContent = song.album_name;
        album.classList.add('song-album');
        
        const thumbnail = document.createElement('img');
        thumbnail.src = song.thumbnail;
        thumbnail.alt = "Album Cover";
        thumbnail.classList.add('thumbnail'); // Add class for styling

        // Make image clickable, opening the Spotify link
        thumbnail.addEventListener('click', () => {
            window.open(song.uri, '_blank');
        });

        // Append all elements to the list item
        li.appendChild(thumbnail);
        li.appendChild(title);
        li.appendChild(artist);
        li.appendChild(album);

        recommendationsList.appendChild(li);
    });
}
