from dotenv import load_dotenv
load_dotenv()

import os
from app import create_app

port = int(os.getenv('PORT', 3018))
print(f"Using port: {port}")

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
