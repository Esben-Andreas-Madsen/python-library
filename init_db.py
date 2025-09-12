from app import create_app, init_db
from seed import seed_data
from configs.prod_config import ProdConfig
from configs.test_config import TestConfig

def setup_database(config, db_name):
    app = create_app(config)
    with app.app_context():
        print(f"Initializing {db_name} database...")
        init_db(app)
        seed_data() # seed sample data
        print(f"{db_name} database ready!\n")

if __name__ == "__main__":
    setup_database(ProdConfig, "Production")
    setup_database(TestConfig, "Test")
