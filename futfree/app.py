
from app import create_app

if __name__ == '__main__':

    app = create_app()
    app.run(host='192.168.0.25', port=5000, debug=True)