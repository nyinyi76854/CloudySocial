import os
import requests

def send_fcm_notification(fcm_token, title, body):
    # FCM endpoint for sending notifications
    fcm_url = "https://fcm.googleapis.com/fcm/send"

    # Your server key from the Firebase console
    server_key = os.getenv("FCM_SERVER_KEY")

    # Payload of the notification
    headers = {
        "Authorization": f"key={server_key}",
        "Content-Type": "application/json"
    }

    # Message payload with the fcmToken
    data = {
        "to": fcm_token,
        "notification": {
            "title": title,
            "body": body
        },
        "priority": "high"
    }

    # Sending the notification to FCM
    response = requests.post(fcm_url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}, response: {response.text}")

if __name__ == "__main__":
    # Replace with a valid fcmToken for testing
    test_fcm_token = "dhecCTtXQfSchJgT4VO6mR:APA91bGI3qDNjq1cPaBVoQQBm0bBDKrE7XGUB5xQ8l6i-mY8-yL_ZUMR5Ms35-bo6lNV3JiU_7uS9CJBsnF3jh1b-rNkszMYqJUYSxA78qEzK-sKSdwDLxdorZWUp8Bw3N2bng33rPvo"
    send_fcm_notification(test_fcm_token, "Test Notification", "This is a test notification from GitHub Actions!")

