from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/file-processing', methods=['POST'])
def file_processing():
    text = request.files["file"]
    json_response ={

    }
    
if __name__ == '__main__':
    app.run()