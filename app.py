from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            expression = request.form['expression']
            result = eval(expression)
        except Exception as e:
            result = f"Error: {e}"

    return render_template('calculator.html', result=result)
if __name__  == '__main__':
    app.run(debug=True)