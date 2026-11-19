import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ["ORDERS_API_URL"]
API_KEY = os.environ["ORDERS_API_KEY"]


def fetch_new_orders(since: str) -> list[dict]:
    response = requests.get(
        f"{BASE_URL}/v1/orders",
        params={"since": since},
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=10,
    )
    response.raise_for_status()
    return response.json().get("orders", [])


def main() -> None:
    since = "1970-01-01T00:00:00Z"
    while True:
        for order in fetch_new_orders(since):
            print("queued", order.get("id"))
            since = order.get("updated_at", since)
        time.sleep(300)


if __name__ == "__main__":
    main()
