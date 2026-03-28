# Retrospective-

AI Scrum Master retrospective app built with Streamlit.

## Features
- Mood Indicator
- Sprint Insights Dashboard
- Google Sheets save/test integration
- AI Generated Questions
- Action Tracker

## Project Structure
- `app.py`: the only Streamlit entrypoint used for local runs and Streamlit Cloud
- `requirements.txt`: Python dependencies for deployment
- `.streamlit/secrets.toml`: local-only secrets file, not committed

## Local Run
1. Install dependencies:
	`pip install -r requirements.txt`
2. Add a local `.streamlit/secrets.toml` or place a local `credentials.json` next to `app.py`.
3. Start the app:
	`streamlit run app.py`

## Streamlit Cloud
1. Deploy using the repository root.
2. Set the main file path to `app.py`.
3. Add the Google service account JSON in Streamlit Cloud secrets as `gcp_service_account`.

Example secrets structure:

```toml
[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."
universe_domain = "googleapis.com"
```

## Notes
- The app first looks for `st.secrets["gcp_service_account"]`.
- If that is not present, it falls back to a local `credentials.json`.
- Do not commit service account keys to the repository.
