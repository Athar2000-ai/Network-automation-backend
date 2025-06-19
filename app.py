from flask import Flask, request, jsonify
from flask_cors import CORS
# from netmiko import ConnectHandler  # Uncomment when using real devices

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "Pong from Flask!"}, 200


@app.route('/configure', methods=['POST'])
def configure_device():
    data = request.get_json()

    ip = data.get('ip')
    username = data.get('username')
    password = data.get('password')
    secret = data.get('secret')
    commands = data.get('commands')

    # ------------------ MOCKED OUTPUT ------------------
    mock_output = f"""
    🟢 MOCK MODE ACTIVE
    Pretending to connect to device: {ip}
    Username: {username}
    Sent {len(commands)} commands:
    {chr(10).join(commands)}

    ✅ Configuration 'successful'.
    """
    return jsonify({"output": mock_output})

    # ------------------ REAL SSH CODE (uncomment when ready) ------------------
    """
    try:
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
            "secret": secret,
        }

        net_connect = ConnectHandler(**device)
        net_connect.enable()

        output = ""
        for cmd in commands:
            output += net_connect.send_command(cmd) + "\n"

        net_connect.disconnect()
        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    """
