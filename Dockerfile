
# Stage 1: Build the frontend
FROM node:15 as builder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

FROM node:15 as production
# Set working directory
WORKDIR /app

# Copy only the package.json and package-lock.json to install production dependencies
COPY frontend/package*.json ./

# Set NODE_ENV to production to avoid installing devDependencies
ENV NODE_ENV=production

# Install only production dependencies
RUN npm install --production

# Copy the built files from the builder stage to the production stage
COPY --from=builder /app/dist /app/dist

# Stage 2: Setup Nginx
FROM nginx:latest
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
