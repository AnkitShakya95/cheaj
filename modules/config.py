import os

# config.py
BOT_NAME = "Free bot"
BOT_TOKEN = "6755775439:AAGkahjp3xK71u-jG6V0uQUR-xJgqLPt9yw"
API_ID = 28328736
API_HASH = "802254a44896baa87f3083b7af36b2e5"
MONGO_URI = "mongodb+srv://mrnobody:modernhackers@mrnobody.q8e87ij.mongodb.net/?retryWrites=true&w=majority&appName=MrNobody"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
