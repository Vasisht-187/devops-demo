import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.main import app, add, multiply
import pytest

# ── Flask test client setup ────────────────────────────
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ── Test 1: Health check returns 200 ──────────────────
def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

# ── Test 2: Add endpoint works correctly ──────────────
def test_add_endpoint(client):
    response = client.get('/add/3/5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8

# ── Test 3: Add helper function unit test ─────────────
def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

# ── Test 4: Multiply function unit test ───────────────
def test_multiply_function():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

# ── Test 5: Version endpoint ──────────────────────────
def test_version_endpoint(client):
    response = client.get('/version')
    assert response.status_code == 200
    data = response.get_json()
    assert 'version' in data