# CINEVERSE PRO // Intelligent Streaming Architecture

![Backend](https://img.shields.io/badge/Backend-Python_Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Security](https://img.shields.io/badge/Security-Java_SE-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-HTML5_&_JS-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Design](https://img.shields.io/badge/Design-Glassmorphism-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**CineVerse Pro** is a next-generation streaming platform prototype that demonstrates **Polyglot Programming** (Python + Java). It orchestrates a high-performance **Python (Flask)** backend that communicates with a compiled **Java** microservice for cryptographic session security, all fronted by a reactive, Netflix-inspired **Glassmorphism UI**.

---

## ⚡ Key Features

* **🧠 Mood-Based Intelligence:** A semantic search engine that analyzes natural language input (e.g., *"I want something scary but romantic"*) to dynamically filter content in real-time without heavy ML libraries.
* **☕ Hybrid Python-Java Bridge:** Features a custom Inter-Process Communication (IPC) layer where Python spawns a JVM subprocess to generate military-grade secure tokens via Java's `SecureRandom`.
* **⭐ Persistent Watchlist:** A robust Favorites system using `localStorage` and data-bound DOM elements, ensuring users' saved movies persist across sessions.
* **🎨 Dynamic Visuals:** The UI adapts to the content—searching for "Action" instantly transforms the massive hero background into a high-res action poster, creating an immersive experience.
* **🚀 Multi-Page Architecture:** A scalable Flask routing system supporting a Dashboard, Detailed Movie Views, and a dedicated Favorites Manager.

---

## 🛠️ Tech Stack

* **Server Core:** Python 3.13 (Flask Web Framework)
* **Security Module:** Java Development Kit (JDK)
* **Frontend Engine:** HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6+)
* **Data Structure:** JSON-based Internal Registry (12 High-Res Movies)
* **Design System:** Custom CSS Variables & Glassmorphism

---

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/cineverse-pro.git](https://github.com/yourusername/cineverse-pro.git)
    cd cineverse-pro
    ```

2.  **Verify Prerequisites**
    * Ensure **Python 3.x** is installed.
    * Ensure **Java (JDK)** is installed (for the security token generator).

3.  **Run the Server**
    * The system will automatically compile the Java security module on the first run.
    ```bash
    python movie_server.py
    ```

4.  **Launch**
    * Open your browser and navigate to:
    * `http://127.0.0.1:5000`

---

## 🧩 System Architecture

**1. The Polyglot Backend (IPC Handshake):**
Unlike standard apps that use one language, CineVerse Pro forces two languages to talk. When the server starts or a page loads, Python halts execution, calls the system shell to run `java TokenGenerator`, captures the standard output (`stdout`), and injects the secure token into the HTML session header.

**2. The Logic Engine (Mood Analysis):**
The `ai_filter` endpoint receives raw text input. Instead of simple string matching, it parses the user's emotional intent using a dictionary map (e.g., mapping "fear" or "dark" to *Horror* and *Thriller*) to curate a personalized list of movies.

**3. The Frontend Core (Dynamic DOM):**
The interface uses Vanilla JavaScript with `fetch` API for non-blocking updates. It features a "Staggered Animation" system where movie cards flow onto the screen sequentially (`animation-delay`) for a premium feel.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
<p align="center">
  <b>CineVerse Pro</b> • Created by <a href="https://github.com/pushtikadia"><b>Pushti Kadia</b></a>
</p>
