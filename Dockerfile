FROM debian:stable-slim
ENV PORT=8991
# COPY source destination
COPY go-server-docker /bin/goserver
CMD ["/bin/goserver"]
