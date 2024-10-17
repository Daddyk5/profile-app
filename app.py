from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # User profile information
    profile = {
        'name': 'Kenneth T Gulmatico',
        'email': 'kenneth.gulmatico@hcdc.edu.ph',
        'phonenumber': '+63 9054549950',
        'github': 'DaddyK5',
        'bio': 'Passionate about machine learning, software development, and K-pop!',
        'skills': [
            ('Python', 'static/skills/python.jpg'),
            ('React', 'static/skills/react.jpg'),
            ('Android', 'static/skills/android.jpg'),
            ('C++', 'static/skills/c++.jpg'),
            ('JavaScript', 'static/skills/javascript.jpg')
        ]
    }
    # Render the template with the profile data
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
