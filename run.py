import os
from app import create_app

from dotenv import load_dotenv
load_dotenv()

port = int(os.getenv('PORT', 3018))
print(f"Using port: {port}")

app = create_app()

if __name__ == '__main__':
    app.run(port=port)
