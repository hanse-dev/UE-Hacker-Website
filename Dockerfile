# Frontend build
FROM node:22-alpine AS frontend
RUN apk add --no-cache python3
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# API + static (single process, one port)
FROM node:22-alpine
WORKDIR /app

COPY api/package*.json ./api/
RUN cd api && npm install --omit=dev

COPY api/src ./api/src
COPY --from=frontend /app/dist ./dist

RUN mkdir -p /app/data

ENV NODE_ENV=production
ENV DATA_DIR=/app/data
ENV STATIC_DIR=/app/dist
ENV API_PORT=8080

EXPOSE 8080

CMD ["node", "api/src/index.js"]
