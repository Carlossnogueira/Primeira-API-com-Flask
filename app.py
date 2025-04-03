from flask import Flask, request
from models.Task import task

# __name__ - "__main__"
app = Flask(__name__)

tasks = []

# CRUD
@app.route('/tasks', methods=['POST'])
def create_task():
    # recepção de dados:
    data = request.get_json()
    return 'Test'

    
# Logs de consulta debug=true
if __name__ == "__main__":
    app.run(debug=True)