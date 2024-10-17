from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': 'Kenneth T Gulmatico',
        'email': 'kenneth.gulmatico@hcdc.edu.ph',
        'phonenumber': '+63 9054549950',  # Add your phone number here
        'github': 'Daddyk5',
        'bio': (
            'I am a passionate and versatile individual with a strong foundation '
            'in machine learning, Python programming, and modern software development. '
            'With hands-on experience across multiple domains, I excel in building robust '
            'applications, developing innovative solutions, and working in dynamic environments. '
            'From Android development to web frameworks like React, I enjoy tackling challenges '
            'head-on and continuously expanding my skill set. As a self-motivated multitasker and '
            'lifelong learner, I thrive in collaborative projects, bringing both technical expertise '
            'and a problem-solving mindset to the table.'
        ),
        'skills': [
            ('Python', 'skills/python.jpg'),
            ('React', 'skills/react.jpg'),
            ('Android Development', 'skills/android.jpg'),
            ('C++', 'skills/cplusplus.jpg'),
            ('JavaScript', 'skills/javascript.jpg'),
            ('Technical Support', 'skills/techsupport.jpg'),
            ('Multitasker', 'skills/multitasker.jpg')
        ]
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
