# Mood-Based Playlist & Inspiration App

A simple Flask web application that lets you select your current mood (happy, chill, focused, energetic, etc.), then generates a custom playlist (YouTube/Spotify/SoundCloud) and suggests articles, poems, quotes, or short videos that fit your mood.

---

## Features
- Select your mood from a friendly UI
- Get a curated playlist and inspirational content for your mood
- Modern, responsive design

---

## Getting Started

### 1. Check Python Installation
Make sure you have Python 3.7 or higher installed:

```
python --version
```
*or*
```
python3 --version
```

---

### 2. Install Dependencies
Install Flask and other dependencies using pip:

```
pip install -r requirements.txt
```

---

### 3. Run the App
Start the Flask application:

```
python app.py
```
*or*
```
python3 app.py
```

---

### 4. Open in Your Browser
After running the app, open your browser and go to:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

You should see the Mood-Based Playlist & Inspiration app running!

---

## Screenshots

![screenshot](screenshot.png)

---

## Customization
- Add more moods or content in `app.py` under the `MOOD_CONTENT` dictionary.
- Update the UI by editing the `HTML_TEMPLATE` in `app.py`.

---

## License
Feel Free to use it 