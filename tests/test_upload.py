
import os
import pytest
from flask import Flask
from app import create_app

@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as testing_client:
        yield testing_client

def test_upload_pdf(test_client):
    data = {
        'name': (open('tests/sample_files/sample.pdf', 'rb'), 'sample.pdf')
    }
    response = test_client.post('/PDF_result', data=data, content_type='multipart/form-data')
    assert response.status_code == 200

def test_upload_docx(test_client):
    data = {
        'name': (open('tests/sample_files/sample.docx', 'rb'), 'sample.docx')
    }
    response = test_client.post('/PDF_result', data=data, content_type='multipart/form-data')
    assert response.status_code == 200

def test_upload_txt(test_client):
    data = {
        'name': (open('tests/sample_files/sample.txt', 'rb'), 'sample.txt')
    }
    response = test_client.post('/PDF_result', data=data, content_type='multipart/form-data')
    assert response.status_code == 200