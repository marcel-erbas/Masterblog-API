# Flask Blog API & Frontend

This project is a full-stack blogging application consisting of a Flask-based REST API and a web frontend for managing blog posts.

## Project Structure
- `backend_app.py`: The Flask API backend (runs on port 5002).
- `frontend_app.py`: The web server serving the UI (runs on port 5001).
- `index.html`: The main structure of the web interface.
- `main.js`: Frontend logic for API communication and DOM manipulation.
- `styles.css`: Custom styling for the user interface.

## Installation & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2.  **Start the Backend:**
    ```bash
    python backend_app.py
    ```

3.  **Start the Frontend:**
    ```bash
    python frontend_app.py
    ```
4.   Access the Application: Open your browser and navigate to http://127.0.0.1:5001.


### API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/posts` | List all posts (supports `sort` and `direction` params). |
| **POST** | `/api/posts` | Create a new blog post. |
| **PUT** | `/api/posts/<id>` | Update an existing post. |
| **DELETE** | `/api/posts/<id>` | Remove a post from the list. |
| **GET** | `/api/posts/search` | Search posts by `title` or `content`. |