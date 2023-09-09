from flask import Flask, request, jsonify
import json 

app = Flask(__name__)

tasks = [
    {
    'id':0,
    'responsável':'Matheus', 
    'tarefa':'Listar tarefas da API',
    'status':'Ok'
    },
    
    {
    'id':1,
    'responsável':'Fernando', 
    'tarefa':'Gerenciamento de Tarefas',
    'status':'Ok'   
    }
    
    ]

# To List and Add new tasks 
@app.route('/lisad/', methods=['POST', 'GET'])
def listAndAdd():   
    if request.method == 'POST':
        taskData = json.loads(request.data)
        position = len(tasks)
        taskData['id'] = position
        tasks.append(taskData)
        return jsonify(tasks[position])
    elif request.method == 'GET':
          return jsonify(tasks)
      

@app.route('/lisad/<int:task_id>/', methods=['GET', 'PUT', 'DELETE'])
def idAlt(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)

    
    if task is None:
        return jsonify({"status":"This task don't exists"}), 400
    
    if request.method == 'GET':
        return jsonify(task), 200 
    elif request.method == 'PUT': 
        taskData = request.get_json()       
        taskData = json.loads(request.data)
        if 'tarefa' in taskData:
            task['tarefa'] = taskData['tarefa']
            return jsonify({"status": "Item atualizado com sucesso"}), 200     
        else:
            pass
    elif request.method == 'DELETE':
        tasks.remove(task)
        return jsonify({"status":"Item excluído com sucesso"})
    else:
        return jsonify({"status":"ERROR"})
    
if __name__ == '__main__':
    app.run()