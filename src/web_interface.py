from flask import Flask, request, jsonify

class WebInterface:
    def __init__(self, app, agent):
        self.app = app
        self.agent = agent
        self.register_routes()

    def register_routes(self):
        @self.app.route("/ask", methods=["POST"])
        def ask():
            data = request.json
            response = self.agent.generate_response(data.get("query", ""))
            return jsonify({"response": response})
