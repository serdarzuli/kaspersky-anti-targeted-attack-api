import pytest
from src.utils import prepare_form_data

def test_prepare_form_data():
    """Test if form data is correctly formatted."""
    payload = {"id": "123", "type": "scan", "content": "test_file"}
    
    form_data = prepare_form_data(payload)
    
    assert form_data is not None, "FormData should not be None"
    assert "content" in form_data, "FormData should contain content"
    assert "id" in form_data, "FormData should contain id"
    assert "type" in form_data, "FormData should contain type"
