from flask import Flask, request, render_template_string

app = Flask(__name__)

MOOD_CONTENT = {
    'happy': {
        'playlist': [
            {'title': 'Happy Hits! (Spotify)', 'url': 'https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC'},
            {'title': 'Feel Good Songs (YouTube)', 'url': 'https://www.youtube.com/watch?v=ZbZSe6N_BXs&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'},
        ],
        'suggestions': [
            {'type': 'quote', 'content': 'Happiness is not something ready made. It comes from your own actions. – Dalai Lama'},
            {'type': 'poem', 'content': '“If you want to be happy, be.” – Leo Tolstoy'},
            {'type': 'article', 'content': 'https://www.psychologytoday.com/us/basics/happiness'},
            {'type': 'video', 'content': 'https://www.youtube.com/watch?v=ZbZSe6N_BXs'},
        ]
    },
    'chill': {
        'playlist': [
            {'title': 'Chill Vibes (Spotify)', 'url': 'https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6'},
            {'title': 'Lo-fi Hip Hop (YouTube)', 'url': 'https://www.youtube.com/watch?v=jfKfPfyJRdk'},
        ],
        'suggestions': [
            {'type': 'quote', 'content': 'Keep calm and carry on.'},
            {'type': 'poem', 'content': '“Peace comes from within. Do not seek it without.” – Buddha'},
            {'type': 'article', 'content': 'https://www.headspace.com/meditation/relaxation'},
            {'type': 'video', 'content': 'https://www.youtube.com/watch?v=2OEL4P1Rz04'},
        ]
    },
    'focused': {
        'playlist': [
            {'title': 'Deep Focus (Spotify)', 'url': 'https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ'},
            {'title': 'Focus Music (YouTube)', 'url': 'https://www.youtube.com/watch?v=hHW1oY26kxQ'},
        ],
        'suggestions': [
            {'type': 'quote', 'content': 'Concentrate all your thoughts upon the work in hand. – Alexander Graham Bell'},
            {'type': 'poem', 'content': '“Success is the result of perfection, hard work, learning from failure, loyalty, and persistence.” – Colin Powell'},
            {'type': 'article', 'content': 'https://www.nytimes.com/guides/smarterliving/how-to-be-more-productive'},
            {'type': 'video', 'content': 'https://www.youtube.com/watch?v=WPni755-Krg'},
        ]
    },
    'energetic': {
        'playlist': [
            {'title': 'Power Workout (Spotify)', 'url': 'https://open.spotify.com/playlist/37i9dQZF1DX70RN3TfWWJh'},
            {'title': 'Upbeat Songs (YouTube)', 'url': 'https://www.youtube.com/watch?v=QH2-TGUlwu4&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI'},
        ],
        'suggestions': [
            {'type': 'quote', 'content': 'Energy and persistence conquer all things. – Benjamin Franklin'},
            {'type': 'poem', 'content': '“The energy of the mind is the essence of life.” – Aristotle'},
            {'type': 'article', 'content': 'https://www.healthline.com/health/energy-boosting-foods'},
            {'type': 'video', 'content': 'https://www.youtube.com/watch?v=QH2-TGUlwu4'},
        ]
    },
}

MOODS = list(MOOD_CONTENT.keys())

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mood-Based Playlist & Inspiration</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            background: #fff;
            font-family: 'Roboto', Arial, sans-serif;
            margin: 0;
            min-height: 100vh;
        }
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 90vh;
        }
        .google-box {
            background: #fff;
            border-radius: 24px;
            box-shadow: 0 2px 8px rgba(60,64,67,.15);
            padding: 2.5em 2em 2em 2em;
            max-width: 420px;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .google-logo {
            font-family: 'Product Sans', 'Roboto', Arial, sans-serif;
            font-size: 2.5em;
            font-weight: 700;
            color: #4285f4;
            letter-spacing: 1px;
            margin-bottom: 0.5em;
        }
        .google-logo span {
            color: #ea4335;
        }
        .google-logo .g-yellow { color: #fbbc05; }
        .google-logo .g-green { color: #34a853; }
        .google-logo .g-red { color: #ea4335; }
        .google-logo .g-blue { color: #4285f4; }
        form {
            width: 100%;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            margin-bottom: 1.5em;
        }
        select {
            font-size: 1.1em;
            padding: 0.7em 1.2em;
            border-radius: 24px 0 0 24px;
            border: 1px solid #dfe1e5;
            background: #f8f9fa;
            outline: none;
            width: 70%;
            transition: border 0.2s;
        }
        select:focus {
            border: 1.5px solid #4285f4;
        }
        button {
            font-size: 1.1em;
            padding: 0.7em 1.5em;
            border-radius: 0 24px 24px 0;
            border: 1px solid #dfe1e5;
            background: #f8f9fa;
            color: #3c4043;
            font-weight: 500;
            cursor: pointer;
            margin-left: -1px;
            transition: background 0.2s, border 0.2s;
        }
        button:hover {
            background: #f1f3f4;
            border: 1.5px solid #4285f4;
        }
        .results {
            margin-top: 2em;
            width: 100%;
            max-width: 420px;
        }
        .card {
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 1px 4px rgba(60,64,67,.13);
            padding: 1.5em 1.2em;
            margin-bottom: 1.5em;
        }
        .card h2 {
            font-size: 1.1em;
            color: #4285f4;
            margin-bottom: 0.7em;
            font-weight: 700;
        }
        .card ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .card li {
            margin-bottom: 1em;
            font-size: 1em;
        }
        .card a {
            color: #1a0dab;
            text-decoration: none;
        }
        .card a:hover {
            text-decoration: underline;
        }
        .mood-emoji {
            font-size: 2em;
            margin-bottom: 0.5em;
            text-align: center;
        }
        @media (max-width: 600px) {
            .google-box, .results { max-width: 98vw; padding: 1em 0.2em; }
            .main-container { min-height: 100vh; }
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="google-box">
            <div class="google-logo">
                <span class="g-blue">M</span><span class="g-red">a</span><span class="g-yellow">r</span><span class="g-green">s</span>
            </div>
            <span class="mood-emoji">
                {% if selected_mood == 'happy' %}😊{% elif selected_mood == 'chill' %}😌{% elif selected_mood == 'focused' %}🎯{% elif selected_mood == 'energetic' %}⚡{% else %}🌈{% endif %}
            </span>
            <form method="post">
                <select name="mood" id="mood">
                    {% for mood in moods %}
                    <option value="{{ mood }}" {% if mood == selected_mood %}selected{% endif %}>{{ mood.title() }}</option>
                    {% endfor %}
                </select>
                <button type="submit">I'm Feeling...</button>
            </form>
        </div>
        {% if mood_data %}
        <div class="results">
            <div class="card">
                <h2>Playlist</h2>
                <ul>
                    {% for item in mood_data['playlist'] %}
                    <li><a href="{{ item['url'] }}" target="_blank">{{ item['title'] }}</a></li>
                    {% endfor %}
                </ul>
            </div>
            <div class="card">
                <h2>Suggestions</h2>
                <ul>
                    {% for suggestion in mood_data['suggestions'] %}
                    <li>
                        {% if suggestion['type'] == 'article' or suggestion['type'] == 'video' %}
                            <strong>{{ suggestion['type'].title() }}:</strong> <a href="{{ suggestion['content'] }}" target="_blank">{{ suggestion['content'] }}</a>
                        {% else %}
                            <strong>{{ suggestion['type'].title() }}:</strong> {{ suggestion['content'] }}
                        {% endif %}
                    </li>
                    {% endfor %}
                </ul>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_mood = None
    mood_data = None
    if request.method == 'POST':
        selected_mood = request.form.get('mood')
        mood_data = MOOD_CONTENT.get(selected_mood)
    return render_template_string(HTML_TEMPLATE, moods=MOODS, selected_mood=selected_mood, mood_data=mood_data)

if __name__ == '__main__':
    app.run(debug=True) 