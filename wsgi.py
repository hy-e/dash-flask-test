"""Application entry point."""
from app import init_server
import os

server = init_server()


if __name__ == "__main__":
    server.run(host='0.0.0.0', debug=True, port=80)