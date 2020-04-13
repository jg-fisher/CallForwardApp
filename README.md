### Steps:
Download Python version 3.8.2
./ngrok http 80 (Twilio account needs to be configured to point to ngrok URL, basically a proxy which exposes APIs running on your desktop publicly)
pip install -r requirements.txt (make sure your pip --version == 3.8.2)
python3.8 main.py (My phone number was hardcoded in the tuple at index [1]. Logic for looping through staff on shift needs to be added)
