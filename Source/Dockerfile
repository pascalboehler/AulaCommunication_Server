FROM alpine:3.9

# Update
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install app dependencies
# none in my case

# Bundle app source
COPY main.py /src/main.py

# Set Port
EXPOSE 33000
CMD ["python3", "/src/main.py", "-p 33000"]
