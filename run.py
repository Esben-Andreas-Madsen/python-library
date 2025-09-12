from app import create_app
from configs.prod_config import ProdConfig
from configs.test_config import TestConfig

app = create_app(TestConfig)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
