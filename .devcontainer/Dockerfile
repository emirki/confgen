FROM ubuntu:20.04

# Install essential packages
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    wget \
    tar \
    unzip \
    sudo \
    && apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Install build dependencies
RUN apt-get update -y && \
    apt-get install -y \
    git \
    python3-pip \
    ncurses-dev \
    net-tools \
    iproute2 \
    && apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Create ulakhaberlesme user that can do sudo without password
RUN adduser ulakhaberlesme \
    && echo "ulakhaberlesme ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER confgen

WORKDIR /home/confgen

# Let binaries built be accessible in the PATH
ENV PATH=/workspace/build/bin:${PATH}

# Install python user packages into build directory
ENV PYTHONUSERBASE=/workspace/build/.local
ENV PATH=/workspace/build/.local/bin:${PATH}
