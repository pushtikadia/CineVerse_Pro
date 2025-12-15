document.addEventListener('DOMContentLoaded', () => {
    // Only run home logic if search bar exists
    if(document.getElementById('userMood')) {
        // Fallback Background (Netflix Style)
        setHeroBackground("https://assets.nflxext.com/ffe/siteui/vlv3/f841d4c7-10e1-40af-bcae-07a3f8dc141a/f6d7434e-d6de-4185-a6d4-c77a2d08737b/US-en-20220502-popsignuptwoweeks-perspective_alpha_website_large.jpg");
        fetchMovies('/api/list');
    }
});

function setHeroBackground(url) {
    const header = document.querySelector('header');
    if(header) {
        header.style.backgroundImage = `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.9)), url('${url}')`;
    }
}

function askAI() {
    const mood = document.getElementById('userMood').value;
    const btn = document.querySelector('.search-bar button');
    const originalText = btn.innerText;
    
    btn.innerText = "Scanning...";
    btn.style.opacity = "0.8";
    
    fetch('/api/ai-filter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mood: mood })
    })
    .then(res => res.json())
    .then(data => {
        if(data.length > 0 && data[0].backdrop) setHeroBackground(data[0].backdrop);
        displayMovies(data);
        btn.innerText = originalText;
        btn.style.opacity = "1";
    });
}

function fetchMovies(endpoint) {
    fetch(endpoint).then(res => res.json()).then(data => displayMovies(data));
}

function displayMovies(movies) {
    const container = document.getElementById('movieList');
    if(!container) return; 
    container.innerHTML = '';
    
    movies.forEach((m, index) => {
        const div = document.createElement('div');
        div.className = 'card';
        div.style.animationDelay = `${index * 50}ms`;
        div.onclick = () => window.location.href = `/movie/${m.id}`;
        
        div.innerHTML = `
            <span class="rating">${m.rating}</span>
            <img src="${m.img}" onerror="this.src='https://via.placeholder.com/500x750?text=No+Image'">
            <div class="info">
                <h3>${m.title}</h3>
                <p class="genre">${m.genre} • ${m.year}</p>
            </div>
        `;
        container.appendChild(div);
    });
}

// --- FAVORITES SYSTEM ---
function addToFavorites(id, title) {
    let favs = JSON.parse(localStorage.getItem('cineFavorites') || '[]');
    if(!favs.includes(id)) {
        favs.push(id);
        localStorage.setItem('cineFavorites', JSON.stringify(favs));
        alert(`${title} added to Favorites!`);
    } else {
        alert("Already in your favorites!");
    }
}

function loadFavoritesPage() {
    const container = document.getElementById('favList');
    if(!container) return;
    
    let favIds = JSON.parse(localStorage.getItem('cineFavorites') || '[]');
    if(favIds.length === 0) {
        container.innerHTML = '<h3 style="color:white; text-align:center; grid-column:span 3;">No favorites yet.</h3>';
        return;
    }

    fetch('/api/list')
        .then(res => res.json())
        .then(allMovies => {
            const myMovies = allMovies.filter(m => favIds.includes(m.id));
            container.innerHTML = '';
            myMovies.forEach(m => {
                const div = document.createElement('div');
                div.className = 'card';
                div.onclick = () => window.location.href = `/movie/${m.id}`;
                div.innerHTML = `
                    <span class="rating">${m.rating}</span>
                    <img src="${m.img}">
                    <div class="info"><h3>${m.title}</h3></div>
                `;
                container.appendChild(div);
            });
        });
}

function clearFavorites() {
    localStorage.removeItem('cineFavorites');
    location.reload();
}