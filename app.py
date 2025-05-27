from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Collect form data
            reviews = int(request.form.get('reviews'))
            size = float(request.form.get('size'))
            price = float(request.form.get('price'))
            content_rating = request.form.get('content_rating')

            # Custom Rating Logic
            if reviews > 100000:
                prediction = 5.0
            elif reviews > 50000:
                prediction = 4.8
            elif reviews > 20000:
                prediction = 4.5
            elif reviews > 10000:
                prediction = 4.2
            elif reviews > 5000:
                prediction = 4.0
            elif reviews > 1000:
                prediction = 3.8
            else:
                prediction = 3.5

        except Exception as e:
            print(f"Error: {e}")
            prediction = "Error occurred. Please try again."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
