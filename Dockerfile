# Use a lightweight base image
FROM python:3.9-alpine
# Set the working directory
WORKDIR /home/data

# Copy Python script and text files to the container
COPY script.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .

# Install dependencies
RUN pip install contractions

# Create an output directory
RUN mkdir /home/data/output

# Run the Python script on container start
CMD ["python", "script.py"]
