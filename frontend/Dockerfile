FROM node:18-alpine AS builder

WORKDIR /app

# Disable telemetry for privacy and speed
ENV NEXT_TELEMETRY_DISABLED 1

# Install dependencies
COPY package.json package-lock.json ./
# Use npm install instead of ci to be more lenient with lockfile differences
RUN npm install

# Copy source
COPY . .

# Build argument for API URL - defaults to localhost if not provided
ARG NEXT_PUBLIC_API_URL=http://localhost:8000
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL

# Build the application
RUN npm run build

# Production image, copy all the files and run next
FROM node:18-alpine AS runner
WORKDIR /app

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copy only necessary files
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

USER nextjs

EXPOSE 3000

ENV PORT 3000

CMD ["npm", "start"]
