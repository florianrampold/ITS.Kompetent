# Use an official Node.js runtime as a parent image
FROM node:15

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy project files
COPY . .


# Start the server

# Expose the port
EXPOSE 8080
