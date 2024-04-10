import argparse
import os
import json
from flask import Flask, render_template, send_from_directory
from utils.plot_functions import create_plot_for_category

app = Flask(__name__)

with open("track_stats.json", "r") as f:
    data = json.load(f)
    

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/graphs')
def graphs():
    plots = []
    categories = ['badges', 'furnis', 'clothes', 'effects']
    
    for category in categories:
        plots.append(create_plot_for_category(data, category))
    
    plots_html = ''.join(plots)
    return render_template('graphs.html', plots=plots)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'img'), 'H.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/raw_stats")
def raw_stats():
    return data


@app.route("/google06cec27a8c7f7b33.html")
def google():
    return render_template('google06cec27a8c7f7b33.html')


@app.route("/yandex_060f2438c56f59b8.html")
def yandex():
    return render_template('yandex_060f2438c56f59b8.html')


@app.route("/robots.txt")
def robots():
    return render_template('robots.txt')


@app.route("/sitemap.xml")
def sitemap():
    return render_template('sitemap.xml')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Flask application.')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    args = parser.parse_args()
    
    if args.debug:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0', port=80)
