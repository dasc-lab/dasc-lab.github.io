FROM alpine:latest

RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community "hugo~0.160.1-r1"

RUN apk add --no-cache vim bash npm

WORKDIR /root/src

CMD ["sh", "-c", "echo '\n---------------------------------------------------' && echo '🚀 Dev server running at: http://localhost:1313/' && echo '---------------------------------------------------\n' && exec hugo server --bind 0.0.0.0 --port 1313 --baseURL http://localhost:1313/"]
