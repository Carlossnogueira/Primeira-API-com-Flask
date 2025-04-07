from flask import Flask, request, jsonify
from models.Task import Task

# __name__ - "__main__"
app = Flask(__name__)

tasks = []
task_id_control = 1

# CRUD

#Create
@app.route('/tasks', methods=['POST'])
def create_task():
   global task_id_control #usando variaveis de fora na função
   #captura a entrada do json
   data = request.get_json()
   new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
   task_id_control += 1
   tasks.append(new_task)
   print(tasks)
   #retorno em json
   return jsonify({"message": "Nova tarefa criada com sucesso"})

#Read
@app.route('/tasks', methods=['GET'])
def get_tasks():
   #for rodando dentro da lista
   task_list = [task.to_dict() for task in tasks]
   output = {
      "tasks": task_list,
      "total_tasks": 0
   }
   return jsonify(output)

    
# Logs de consulta debug=true
if __name__ == "__main__":
    app.run(debug=True)