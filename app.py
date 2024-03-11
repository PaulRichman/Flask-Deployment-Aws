from flask import Flask, render_template, request
import re

app = Flask(__name__)


######################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/email_Validity', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(regex_pattern, email)
    if is_valid:
        return render_template('email_Validity.html', email=email, valid=True)
    else:
        return render_template('email_Validity.html', email=email, valid=False)


########################################

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=5000)
