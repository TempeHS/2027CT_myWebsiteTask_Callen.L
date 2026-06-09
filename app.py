from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

# MAIN PAGES


@app.route('/terms-and-conditions')
def terms_and_conditions():
    return render_template('terms-and-conditions.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/about-us')
def about_us():
    return render_template('about-us.html')


@app.route('/site-map')
def site_map():
    return render_template('site-map.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
