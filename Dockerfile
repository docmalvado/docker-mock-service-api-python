# From base image python
FROM python:3.9.6-alpine3.14

# Install extra packages
RUN apk update && apk add bash && apk add bind-tools && apk add curl

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copying required files from your file system to container file system
COPY ./src/ requirements.txt ./

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Command to run when intantiate an image
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]