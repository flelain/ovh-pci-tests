ARG IMAGE_RELEASE=latest

FROM gcr.io/distroless/base-debian12:${IMAGE_RELEASE}
LABEL maintainer="ynachi" \
      description="Amazing App" \
      documentation="https://github.com/GoogleContainerTools/distroless"

COPY app /

USER 1001

ENTRYPOINT [ "/app" ]
