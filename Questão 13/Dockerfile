# Questão 13 — Imagem com Node.js e Express (via clone de projeto GitHub)

FROM node:18-alpine

RUN apk add --no-cache git

WORKDIR /app

#  Clonando diretamente do GitHub.
RUN git clone https://github.com/eMahtab/node-express-hello-world.git .

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]