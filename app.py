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
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Montserrat', Arial, sans-serif;
            background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
            margin: 0; padding: 0;
            min-height: 100vh;
        }
        .container {
            max-width: 500px;
            margin: 48px auto;
            background: #fff;
            padding: 2.5em 2em 2em 2em;
            border-radius: 18px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.12);
            position: relative;
        }
        h1 {
            text-align: center;
            font-weight: 700;
            font-size: 2.2em;
            margin-bottom: 0.5em;
            letter-spacing: 1px;
            color: #ff7e5f;
        }
        .mood-emoji {
            font-size: 2.5em;
            display: block;
            text-align: center;
            margin-bottom: 0.5em;
        }
        form {
            text-align: center;
            margin-bottom: 2em;
        }
        select {
            font-size: 1.1em;
            padding: 0.6em 1.2em;
            border-radius: 8px;
            border: 1px solid #ffb88c;
            background: #fff7f0;
            margin-right: 0.5em;
            transition: border 0.2s;
        }
        select:focus {
            border: 1.5px solid #ff7e5f;
            outline: none;
        }
        button {
            font-size: 1.1em;
            padding: 0.6em 1.5em;
            border-radius: 8px;
            border: none;
            background: linear-gradient(90deg, #ffb88c 0%, #ff7e5f 100%);
            color: #fff;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(255,126,95,0.08);
            transition: background 0.2s, transform 0.1s;
        }
        button:hover {
            background: linear-gradient(90deg, #ff7e5f 0%, #ffb88c 100%);
            transform: translateY(-2px) scale(1.03);
        }
        .section {
            margin-bottom: 2.2em;
        }
        h2 {
            color: #ff7e5f;
            font-size: 1.3em;
            margin-bottom: 0.7em;
            border-left: 4px solid #ffb88c;
            padding-left: 0.5em;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin-bottom: 1.1em;
            background: #fff7f0;
            border-radius: 8px;
            padding: 0.8em 1em;
            box-shadow: 0 1px 4px rgba(255,184,140,0.07);
            transition: box-shadow 0.2s;
        }
        li:hover {
            box-shadow: 0 4px 12px rgba(255,126,95,0.13);
        }
        a {
            color: #ff7e5f;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.2s;
        }
        a:hover {
            color: #ffb88c;
            text-decoration: underline;
        }
        .suggestion-type {
            font-size: 0.95em;
            font-weight: 700;
            color: #ffb88c;
            margin-right: 0.5em;
        }
        @media (max-width: 600px) {
            .container { padding: 1.2em 0.5em; }
            h1 { font-size: 1.3em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Mood-Based Playlist & Inspiration</h1>
        <span class="mood-emoji">
            {% if selected_mood == 'happy' %}😊{% elif selected_mood == 'chill' %}😌{% elif selected_mood == 'focused' %}🎯{% elif selected_mood == 'energetic' %}⚡{% else %}🌈{% endif %}
        </span>
        <form method="post">
            <label for="mood" style="font-weight:600; color:#ff7e5f;">How are you feeling?</label>
            <select name="mood" id="mood">
                {% for mood in moods %}
                <option value="{{ mood }}" {% if mood == selected_mood %}selected{% endif %}>{{ mood.title() }}</option>
                {% endfor %}
            </select>
            <button type="submit">Show me!</button>
        </form>
        {% if mood_data %}
        <div class="section">
            <h2>Playlist</h2>
            <ul>
                {% for item in mood_data['playlist'] %}
                <li><a href="{{ item['url'] }}" target="_blank">{{ item['title'] }}</a></li>
                {% endfor %}
            </ul>
        </div>
        <div class="section">
            <h2>Suggestions</h2>
            <ul>
                {% for suggestion in mood_data['suggestions'] %}
                <li>
                    {% if suggestion['type'] == 'article' or suggestion['type'] == 'video' %}
                        <span class="suggestion-type">{{ suggestion['type'].title() }}:</span>
                        <a href="{{ suggestion['content'] }}" target="_blank">{{ suggestion['content'] }}</a>
                    {% else %}
                        <span class="suggestion-type">{{ suggestion['type'].title() }}:</span> {{ suggestion['content'] }}
                    {% endif %}
                </li>
                {% endfor %}
            </ul>
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