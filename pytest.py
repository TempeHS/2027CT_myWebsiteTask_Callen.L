import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for our Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ============ HOME PAGE TESTS ============

def test_homepage_load(client):
    """Test home page returns status 200."""
    response = client.get('/')
    assert response.status_code == 200


def test_homepage_title(client):
    """Test homepage has site title"""
    response = client.get('/')
    assert b'My Flask Site' in response.data


def test_homepage_navigation(client):
    """Test homepage has navigation bar."""
    response = client.get('/')
    assert b'navbar' in response.data


def test_homepage_bootstrap(client):
    """Test homepage has Bootstrap CSS linked."""
    response = client.get('/')
    assert b'bootstrap' in response.data


# ============ CONTACT PAGE TESTS ============ FOR FUTURE USE

# def test_contact_page_loads(client):
#    """Test that the contact page returns status 200."""
#    response = client.get('/contact')
#    assert response.status_code == 200


# def test_contact_page_has_form(client):
#    """Test that the contact page has a form."""
#    response = client.get('/contact')
#    assert b'<form' in response.data
