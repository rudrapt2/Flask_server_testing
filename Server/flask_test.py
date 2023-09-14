from flask import Flask
from datetime import datetime

y = bytearray(2)
print(y)


x = datetime.now()

app = Flask(__name__)

@app.route('/time')
def get_time():
    return{
        "Name": "Rudra",
        "Age": "18",
        "Date":x,
        "programming":"python"
    }

if __name__ == "__main__":
    app.run()