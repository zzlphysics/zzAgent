from flask import Flask, request, jsonify

class WebInterface:
    def __init__(self, agent):
        self.app = Flask(__name__, static_url_path='', static_folder='static')
        self.agent = agent
        self.register_routes()
        self.run_flask()

    def register_routes(self):
        @self.app.route("/chat", methods=['POST'])
        def chat():
            user_input = request.json.get('input', '')
            response = self.agent.handle_request(user_input)
            return jsonify({'response': response})

        @self.app.route("/")
        def index():
            return self.app.send_static_file('index.html')

    def run_flask(self):
        self.app.run(host='0.0.0.0', port=5000)
