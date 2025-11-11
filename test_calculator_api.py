import pytest
from calculator_api import app

@pytest.fixture
def client():
    # Configure the Flask app for testing
    app.testing = True
    client = app.test_client()
    return client


def test_add(client):
    """Test the addition endpoint"""
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    assert b'"result":5.0' in response.data


def test_subtract(client):
    """Test the subtraction endpoint"""
    response = client.get('/subtract?a=10&b=4')
    assert response.status_code == 200
    assert b'"result":6.0' in response.data


def test_multiply(client):
    """Test the multiplication endpoint"""
    response = client.get('/multiply?a=7&b=3')
    assert response.status_code == 200
    assert b'"result":21.0' in response.data


def test_divide(client):
    """Test the division endpoint"""
    response = client.get('/divide?a=8&b=2')
    assert response.status_code == 200
    assert b'"result":4.0' in response.data


def test_divide_by_zero(client):
    """Ensure dividing by zero returns an error"""
    response = client.get('/divide?a=8&b=0')
    assert response.status_code == 400 or response.status_code == 500
