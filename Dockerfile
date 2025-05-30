FROM python:3.12-slim

# Create working folder and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application contents
COPY service/ ./service/

# Switch to a non-root user
RUN useradd --uid 1000 otayou && chown -R otayou /app
USER otayou

# Run the service
ENV FLASK_APP=service/app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
