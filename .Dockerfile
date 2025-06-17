FROM alpine:latest

# Install curl and uv
RUN apk add --no-cache curl

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy all project in /app
COPY . /app

# Change workdir
WORKDIR /app

# Launch application
CMD uv run main.py > logs/output.log 2>&1
