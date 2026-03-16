import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return "ALIVE", 200

if __name__ == "__main__":
    # The absolute must-haves for Cloud Run
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
