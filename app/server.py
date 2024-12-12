import os

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from log_parser import log_parse_to_json  # Ensure this function exists in log_parser.py

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def read_root():
    return {"message": "Server is working fine"}


@app.post("/upload_log/")
async def create_upload_file(file: UploadFile):
    try:
        # Directory to save uploaded logs
        save_dir = "uploaded_logs"
        os.makedirs(save_dir, exist_ok=True)

        # Save the uploaded file
        file_path = os.path.join(save_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        print(f"File '{file.filename}' uploaded successfully")

        # Parse the log file
        print("Parsing logs...")
        try:
            log_data_in_json = log_parse_to_json(file_path)
        except Exception as parse_error:
            return {
                "message": "File uploaded, but log parsing failed",
                "error": str(parse_error),
            }

        return {
            "message": "File uploaded and parsed successfully",
            "log_data": log_data_in_json,
        }
    except Exception as upload_error:
        return {
            "message": "File upload failed",
            "error": str(upload_error),
        }
