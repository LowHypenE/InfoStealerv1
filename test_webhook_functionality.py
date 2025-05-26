import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE"

def send_test_message():
    data = {
        "content": "@everyone ✅ Webhook test successful!",
        "username": "Webhook Test Bot"
    }

    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204 or response.status_code == 200:
        print("[✅] Webhook is working!")
    else:
        print(f"[❌] Failed to send webhook: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    send_test_message()
