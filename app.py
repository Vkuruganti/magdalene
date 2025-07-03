from flask import Flask, request, render_template

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

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_mood = None
    mood_data = None
    if request.method == 'POST':
        selected_mood = request.form.get('mood')
        mood_data = MOOD_CONTENT.get(selected_mood)
    return render_template('index.html', moods=MOODS, selected_mood=selected_mood, mood_data=mood_data)

if __name__ == '__main__':
    app.run(debug=True) 