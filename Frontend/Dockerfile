# Build stage
FROM node:16 as builder
# Set working directory in the container
WORKDIR /app
# Copy package.json and package-lock.json to the container
COPY package*.json ./
# Install dependencies
# RUN npm install
# Copy the rest of the application code to the container
COPY . .
# Expose port 5173
EXPOSE 5173
RUN chmod +x shell.sh
ENTRYPOINT bash shell.sh
# Build the Vue.js application for production
# RUN npm run dev --host





