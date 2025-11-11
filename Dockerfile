# 1) Base image
FROM python:3.13-slim

# 2) Workdir
WORKDIR /app

# 3) Install deps first (use layer cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy app code
COPY calculator_api.py .

# 5) Expose port (documentational)
EXPOSE 5000

# 6) Run the API
CMD ["python", "calculator_api.py"]

