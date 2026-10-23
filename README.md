
# Website Health Monitor

A simple Python application that checks website availability
and measures HTTP response time.

## Features
- Sends HTTP GET requests
- Displays HTTP status codes
- Measures response time
- Handles network errors
- Uses a configurable request timeout

## Requirements
- Python 3.10+
- requests library

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python monitor.py
```

## Roadmap
- [x] Basic website health check
- [ ] Monitor multiple websites
- [ ] Add structured logging
- [ ] Add automated tests
- [ ] Dockerize the application
- [ ] Configure GitHub Actions
- [ ] Add monitoring alerts
