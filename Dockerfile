FROM fluentd:v1.14.0-1.0

USER root

RUN apk update && apk upgrade && \
    apk add build-base && \
    apk add ruby-dev

RUN gem install fluent-plugin-syslog \
    && gem install fluent-plugin-kafka

USER fluent
