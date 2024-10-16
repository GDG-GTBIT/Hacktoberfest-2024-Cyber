from flask import Flask, render_template, jsonify, redirect, url_for
import os
from encoder import encode
from decoder import decode
import atexit

app = Flask(__name__)
cleanup = True
def exit_program():
    global cleanup
    if cleanup:
        print("exiting...")
        encode('gtbit')

atexit.register(exit_program)
@app.route('/')
def index():
    return redirect(url_for('logs_page'))

@app.route('/logs')
def logs_page():
    return render_template('logs.html') 



@app.route('/get_logs')
def get_logs():
    log_file_path = 'logfile.txt'
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r+') as file:
            logs = file.readlines()
        return jsonify(logs=logs)
    else:
        return jsonify(logs=["Log file not found."])

if __name__ == '__main__':
    try:
        decode('gtbit')
    except Exception as e:
        cleanup = False
    app.run(port=1438, debug=True)
