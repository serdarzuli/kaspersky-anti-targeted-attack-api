import ssl
from config import CLIENT_CERT, CLIENT_KEY

def create_ssl_context():
    """Creates and returns an SSL context for secure requests."""
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)
    return ssl_context
