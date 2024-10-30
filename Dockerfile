FROM node:23-alpine

WORKDIR /app/my-app

CMD ["npm", "run", "dev"] # 実行時に上書き可能
