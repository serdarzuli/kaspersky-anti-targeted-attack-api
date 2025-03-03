import pytest
import asyncio
from src.api import KataAPI  # Import the API class

@pytest.mark.asyncio
async def test_ksc_scan():
    """Test the KSC scan method with a sample payload."""
    app = KataAPI()
    payload = {"path": "sample_file.txt", "id": "12345", "content": "test_content"}

    response = await app.ksc_scan(payload)
    
    assert isinstance(response, str), "Response should be a string"
    assert "error" not in response.lower(), "Response should not contain an error"

@pytest.mark.asyncio
async def test_delete_file():
    """Test the file deletion functionality."""
    app = KataAPI()
    payload = {"file_no": "98765"}
    
    response = await app.delete_file(payload)
    
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "success" in response or "message" in response, "Response should contain success or message field"

@pytest.mark.asyncio
async def test_file_result():
    """Test fetching file scan results."""
    app = KataAPI()

    response = await app.file_result()
    
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "status" in response, "Response should contain a status field"

@pytest.mark.asyncio
async def test_detected_type():
    """Test detected type functionality."""
    app = KataAPI()
    payload = {"type": "malware", "no": 10}

    response = await app.detectedtype(payload)
    
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "results" in response, "Response should contain results"

@pytest.mark.asyncio
async def test_object_get_restriction():
    """Test retrieving object restrictions."""
    app = KataAPI()

    response = await app.object_get_restriction()
    
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "filters" in response, "Response should contain filters"
