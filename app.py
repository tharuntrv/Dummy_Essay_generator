from flask import Flask, render_template
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_essays', methods=['POST'])
def generate_essays():
    essays = generate_dummy_essays()
    return render_template('essays.html', essays=essays)

def generate_dummy_essays():
    return [fake.text() for _ in range(5)]

if __name__ == '__main__':
    app.run(debug=True)
