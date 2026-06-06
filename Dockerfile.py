# Build from a slim Debian/Linux image
FROM debian:stable-slim

# Update apt and install build tooling
RUN apt update \
    && DEBIAN_FRONTEND=noninteractive apt upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt install -y \
        build-essential \
        zlib1g-dev \
        libncurses-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        wget \
        libbz2-dev \
    && rm -rf /var/lib/apt/lists/*

# Download Python interpreter code and unpack it
RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
RUN tar -xf Python-3.10.*.tgz

# Build the Python interpreter
RUN cd Python-3.10.8 && ./configure --enable-optimizations && make && make altinstall

# Copy our code into the image
COPY main.py main.py

# Copy our data dependencies
COPY books/ books/

# Run our Python script
CMD ["python3.10", "main.py"]
