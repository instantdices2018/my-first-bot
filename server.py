from flask import Flask
from extend import run_extend  # move the logic into a callable

app = Flask(__name__)

@app.route("/trigger")
def trigger():
    success = run_extend()
    return ("OK" if success else "FAIL"), (200 if success else 500)
