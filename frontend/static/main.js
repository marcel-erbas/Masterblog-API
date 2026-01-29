window.onload = function() {
    var savedBaseUrl = localStorage.getItem('apiBaseUrl');
    if (savedBaseUrl) {
        document.getElementById('api-base-url').value = savedBaseUrl;
        loadPosts();
    }
}

function loadPosts() {
    var baseUrl = document.getElementById('api-base-url').value;
    localStorage.setItem('apiBaseUrl', baseUrl);

    fetch(baseUrl + '/posts')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load posts');
            }
            return response.json();
        })
        .then(data => {
            const postContainer = document.getElementById('post-container');
            postContainer.innerHTML = '';

            data.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.className = 'post';
                postDiv.innerHTML = `<h2>${post.title}</h2><p>${post.content}</p>
                <button onclick="deletePost(${post.id})">Delete</button>`;
                postContainer.appendChild(postDiv);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            alert(error.message);
        });
}

function addPost() {
    var baseUrl = document.getElementById('api-base-url').value;
    var postTitle = document.getElementById('post-title').value;
    var postContent = document.getElementById('post-content').value;

    if (!postTitle || !postContent) {
        alert("Missing title or content");
        return;
    }

    fetch(baseUrl + '/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: postTitle, content: postContent })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.message || 'Failed to add post'); });
        }
        return response.json();
    })
    .then(post => {
        console.log('Post added:', post);
        document.getElementById('post-title').value = '';
        document.getElementById('post-content').value = '';
        loadPosts();
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error: " + error.message);
    });
}

function deletePost(postId) {
    var baseUrl = document.getElementById('api-base-url').value;

    fetch(baseUrl + '/posts/' + postId, {
        method: 'DELETE'
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.message || 'Delete failed'); });
        }
        console.log('Post deleted:', postId);
        loadPosts();
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Delete failed: " + error.message);
    });
}