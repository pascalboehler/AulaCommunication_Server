FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
# none in my case

# Bundle app source
COPY main.py /src/main.py

# Set Port
EXPOSE 33000
CMD ["python3", "/src/main.py", "-Port 33000"]