
from email import message
from urllib import response
from flask import Flask, jsonify, request
# rivescript configuration
import bot
import utilis
# create app
app = Flask(__name__)

# Route
# @app.route("/chat",methods=["GET"])


@app.route("/chat", methods=["POST"])
def chat():
    request_data = request.get_json()
    message = request_data['message']
   
    #message="tell me a poem"
    # return Value
    data = {}
    status, response = bot.chat(message)

    if status == 0:
        data["reply"] = response
        data["status"] = "success"

    else:
        data["reply"] = response
        data["status"] = "failed"
    return jsonify(data)

#DB Test
@app.route("/test",methods=["GET"])
def test():
    return jsonify( utilis.save("2"))


# app run
if __name__ == "__main__":
    app.run()
