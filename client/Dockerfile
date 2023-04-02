FROM node:19.8.1-bullseye-slim

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
ENV NEXT_TELEMETRY_DISABLED 1

COPY . .
RUN npm install

CMD ["npm", "run", "dev"]
