FROM alpine:3.20

RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community "hugo=~v0.134.2"

RUN apk add --no-cache vim bash

WORKDIR /root/src

CMD ["hugo", "server"]
