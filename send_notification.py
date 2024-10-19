import os
import json
import requests
import google.auth
from google.auth.transport.requests import Request

# Get credentials from the service account JSON stored in GitHub secrets
def get_access_token():
    # Load the service account key from environment variable
    service_account_info = json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON"))
    credentials = google.auth.credentials.with_scopes_if_required(
        google.auth.load_credentials_from_info(service_account_info),
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    return credentials.token

# Function to send the notification
def send_fcm_notification(fcm_token, title, body):
    project_id = "chatflow-59776"  # Your Firebase project ID

    # Get OAuth 2.0 token
    access_token = get_access_token()

    # FCM HTTP v1 API endpoint
    fcm_url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"

    # Notification payload
    message = {
        "message": {
            "token": fcm_token,
            "notification": {
                "title": title,
                "body": body
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Send POST request
    response = requests.post(fcm_url, headers=headers, json=message)

    # Check the response status
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}, response: {response.text}")

if __name__ == "__main__":
    # Test with your device's FCM token
    test_fcm_token = "dhecCTtXQfSchJgT4VO6mR:APA91bGI3qDNjq1cPaBVoQQBm0bBDKrE7XGUB5xQ8l6i-mY8-yL_ZUMR5Ms35-bo6lNV3JiU_7uS9CJBsnF3jh1b-rNkszMYqJUYSxA78qEzK-sKSdwDLxdorZWUp8Bw3N2bng33rPvo"
    send_fcm_notification(test_fcm_token, "Test Notification", "This is a test notification.")
