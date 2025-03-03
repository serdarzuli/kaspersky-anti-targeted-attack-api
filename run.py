import asyncio
from src.api import KataAPI

async def main():
    api = KataAPI()

    # Example payload
    scan_payload = {"path": "example.jpg", "id": "12345"}

    result = await api.scan_file(scan_payload)
    print("Scan Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
