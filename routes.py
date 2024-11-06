from flask import Blueprint, render_template, request
from app.process import analyze_traffic

# Create a Blueprint for your routes
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']  # Get the uploaded image
        vehicle_count, signal_time = analyze_traffic(image)  # Analyze the traffic
        return render_template('result.html', vehicle_count=vehicle_count, signal_time=signal_time)  # Pass results to template

    return render_template('index.html')
