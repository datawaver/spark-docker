FROM bitnami/spark:latest
USER root

# install just on a debian bookworm base
RUN apt update && \
    apt install -y --no-install-recommends wget gpg lsb-release && \
    wget -qO - 'https://proget.makedeb.org/debian-feeds/prebuilt-mpr.pub' | gpg --dearmor | tee /usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg 1> /dev/null && \
    echo "deb [arch=all,$(dpkg --print-architecture) signed-by=/usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg] https://proget.makedeb.org prebuilt-mpr $(lsb_release -cs)" | tee /etc/apt/sources.list.d/prebuilt-mpr.list && \
    apt update && \
    apt install just && \
    rm -rf /var/lib/apt/lists/*

# install addional tools
# RUN apt update && \
#     apt install -y --no-install-recommends pipenv && \
#     rm -rf /var/lib/apt/lists/*

USER 1001
CMD [ "/bin/bash" ]