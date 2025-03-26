from flask import Flask
import os
from config.configuration import DevConfig, QAConfig, ProdConfig
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

env = os.getenv('ENV')

if env == "Dev":
    app.config.from_object(DevConfig)
elif env == "QA":
    app.config.from_object(QAConfig)
elif env == "Prod":
    app.config.from_object(ProdConfig)

@app.route('/hi')
def main():
    return f"Environment is {app.config['ENV_NAME']}"

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])