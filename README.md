# FastAPI Log File Parser

This FastAPI application allows users to upload log files, save them on the server, and parse the log data into JSON format. The application supports CORS to facilitate communication with a React frontend.

---

## Features

- Upload log files via HTTP POST requests.
- Save uploaded log files to a specific directory.
- Parse log files into structured JSON data using regex.
- Enable CORS for frontend integration.

---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/mrayushmehrotra/backend_ros
cd backend_ros
```

### Install Dependencies
```bash
python3 -m venv . # for creating a virtual env 
pip install -r app/requirements.txt
uvicorn server:app --reload
```

---

## File Structure
```
.
├── server.py          # FastAPI application
├── log_parser.py      # Log parsing utility
├── uploaded_logs      # Directory for storing uploaded log files
├── sample.log         # Example log file
├── README.md          # Project documentation
```

---

## Usage

### Start the Server
```bash
uvicorn server:app --reload
```
The server will run at `http://127.0.0.1:8000`.

### API Endpoints

#### 1. Health Check
**GET /**
- **Description**: Check if the server is running.
- **Response**:
  ```json
  {
    "Message": "Server is Working fine"
  }
  ```

#### 2. Upload Log File
**POST /upload_log/**
- **Description**: Upload a log file to the server and parse it.
- **Request**:
  - `file`: Log file to upload (type: multipart/form-data).
- **Response** (Success):
  ```json
  {
    "message": "File Uploaded successfully",
    "parsed_logs": [
      {
        "timestamp": "2024-12-11 11:31:58",
        "severity": "DEBUG",
        "source": "controller",
        "message": "Debugging path planner outputs."
      },
      ...
    ]
  }
  ```
- **Response** (Error):
  ```json
  {
    "error": "Error details"
  }
  ```

