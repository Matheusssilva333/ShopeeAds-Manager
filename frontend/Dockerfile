FROM node:18-alpine

WORKDIR /app

# Instalar dependências (apenas lock file primeiro para cache)
COPY package.json package-lock.json ./
RUN npm ci

# Copiar resto do código
COPY . .

# Build da aplicação
RUN npm run build

# Expor porta
EXPOSE 3000

# Start
CMD ["npm", "start"]
