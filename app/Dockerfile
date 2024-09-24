# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose necessary ports
EXPOSE 8000 8501

# Command to run both FastAPI and Streamlit concurrently (using sh)
CMD bash -c "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0"
