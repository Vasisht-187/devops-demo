from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# ── Route 1: Health check endpoint ────────────────────
# This is a standard DevOps practice: every service should
# expose a /health endpoint so monitoring tools can check it.
@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'devops-demo',
        'timestamp': str(datetime.datetime.now())
    }), 200

# ── Route 2: Simple calculator ────────────────────────
# A concrete function we can write unit tests for.
@app.route('/add/<int:a>/<int:b>')
def add_numbers(a, b):
    result = add(a, b)
    return jsonify({'a': a, 'b': b, 'result': result}), 200

# ── Route 3: Version info ─────────────────────────────
@app.route('/version')
def version():
    return jsonify({'version': '1.0.0', 'build': 'stable'}), 200

# ── Helper function (used by the route above) ─────────
def add(a, b):
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)