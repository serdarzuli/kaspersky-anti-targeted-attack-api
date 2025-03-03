from aiohttp import FormData

def prepare_form_data(payload):
    """Prepares multipart form data for file uploads."""
    data = FormData()
    data.add_field("content", open(payload["path"], "rb"))
    data.add_field("scanId", payload["id"])
    data.add_field("objectType", "file")
    return data

def prepare_detect_type_params(payload):
    """Prepares query parameters for the detect type request."""
    return {
        "detect_type": payload["type"],
        "limit": payload["no"],
        "token": payload.get("token", "default_token")
    }
