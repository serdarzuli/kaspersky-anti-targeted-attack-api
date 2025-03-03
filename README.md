# Kata API Integration

## 📌 Project Overview
This project provides an asynchronous integration with the Kata scanning service, allowing users to securely upload files, scan them, and retrieve results. The API leverages `aiohttp` for efficient async communication and uses SSL certificates for secure requests.

## 🚀 Features
- **File Upload & Scanning**: Upload and scan files securely.
- **Delete Files**: Remove scanned files using unique file numbers.
- **Retrieve Scan Results**: Fetch the current status of scanned files.
- **Detection & Filtering**: Retrieve detection types and filter scanned objects.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/serdarzuli/kaspersky-anti-targeted-attack-api
   cd kata-api-integration
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure SSL certificates (modify `kata.py` if needed).

## 🔧 Usage
Run the API script to interact with the scanning service:
```bash
python run_kata.py
```

## 📜 File Structure
```
📦 Kata-API
├── src/
│   ├── api.py          # Core API methods
│   ├── utils.py        # Helper functions
├── tests/              # Unit tests
├── .gitignore
├── README.md          # Documentation
├── requirements.txt   # Required dependencies
└── run_kata.py        # Main script to execute API requests
```

## 📂 API Endpoints
| Function | Description |
|----------|------------|
| `ksc_scan(payload)` | Uploads and scans a file. |
| `delete_file(payload)` | Deletes a scanned file. |
| `file_result()` | Fetches scan results. |
| `detectedtype(payload)` | Retrieves detection type. |
| `object_get_restriction()` | Gets object restrictions. |

## ✅ Testing
Run tests using `pytest`:
```bash
pytest -v
```

## 📜 License
This project follows the **MIT License**. See `LICENSE` for details.

