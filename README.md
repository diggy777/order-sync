# order-sync

Small worker that pulls new orders from our orders API and pushes them to the
warehouse queue every 5 minutes.

## Setup

    pip install -r requirements.txt
    python sync.py
