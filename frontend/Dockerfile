FROM node:18-alpine

WORKDIR /app

# Instalar dependências (apenas lock file primeiro para cache)
COPY package.json package-lock.json ./
RUN npm ci

# Copiar resto do código
COPY . .

# Argumentos de build
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL

# Build da aplicação
RUN npm run build

# Expor porta
EXPOSE 3000

# Start
CMD ["npm", "start"]
