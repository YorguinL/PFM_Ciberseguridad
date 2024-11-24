
from app import create_app

env = "pro"

application = create_app()

# Si estamos ejecutando en local, env == "pre"
if __name__ == "__main__" and env == "pre":
    application.run(host="127.0.0.1", port=5000, debug=True)