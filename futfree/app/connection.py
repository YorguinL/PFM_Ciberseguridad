
from flask import request
import json
from datetime import datetime

class Connection:

    def __init__(self):

        self.connection = {
            "timestamp": None,
            "client_ip": None,
            "user_agent" : None,
            "user_action": {
                "signup": False,
                "social": None,
                "email": None,
                "password": None,
            }
        }

    def connection_data(self, signup, social, email, password):

        # Obtener fecha y hora y dar formato
        timestamp = datetime.now().isoformat() 
        formatted_date = datetime.fromisoformat(timestamp).strftime("%d-%m-%Y %H:%M")
        self.connection["timestamp"] = formatted_date
        
        # Obtener la IP del cliente
        client_ip = request.remote_addr or "IP desconocida"
        self.connection["client_ip"] = client_ip

        # Obtener el User-Agent (incluye información del navegador y sistema operativo)
        user_agent = request.headers.get('User-Agent', 'Desconocido')
        self.connection["user_agent"] = user_agent

        # Asignar la acción y datos del usuario
        self.connection["user_action"]["signup"] = signup
        self.connection["user_action"]["social"] = social
        self.connection["user_action"]["email"] = email
        self.connection["user_action"]["password"] = password

        self.save_data()


    def save_data(self):

        # Guarda la información en el archivo JSON
        filename = "log_connections.json"

        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(self.connection)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        