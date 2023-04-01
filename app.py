from flask import Flask, request, jsonify
from environment import env
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(env["MONGO_URI"])

# JS EQ: const app = express()
app = Flask(__name__)

db = client.test2

todos = db.todos

# Index route 
@app.route('/todos', methods=['GET'])
def index_todos():
    res = todos.find()
    print(res)
    return jsonify([{'_id': str(todo['_id']), 'title': todo['title'],'body': todo['body'], 'completed' : todo['completed'] } for todo in result])

#Single Todo
@app.route('/todos/<id>', methods=['GET'])
def one_todo(one_id):
    res = todos.find_one({"_id": ObjectId(one_id)})
    print(res)
    return jsonify({'one_id': str(res['one_id']), 'title': res['title'],'body': res['body'], 'completed' : res['completed'] })

#Create new Todo
@app.route('/todos', methods=['POST'])
def make_todo():
    todo_info = request.get_json()
    res = todos.insert_one({'title': todo_info['title'],'body': todo_info['body'], 'completed' : todo_info['completed'] })
    print(res)
    return str(res.inserted_id), 201
#Update a Todo
@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    todo_info = request.get_json()
    res = todos.find_one_and_update({'id': ObjectId(id)}, {'$set': todo_info})
    print(res)
    return str(res.inserted_id), 201
#Delete Todo
@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    res = todos.find_one_and_delete({'id': ObjectId(id)})
    print(res)
    return str(res)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "Hello World!"    

if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/logs', methods=['GET'])
# def get_logs():
#     result = logs.find()
#     print(result)
#     return jsonify([{'_id': str(log['_id']), 'message': log['message']} for log in result])

# @app.route('/logs', methods=['POST'])
# def create_log():
#     data = request.get_json()
#     result = logs.insert_one({'message': data['message']})
#     return str(result.inserted_id), 201

# from flask import Flask, request, jsonify
# from environment import env
# from pymongo import MongoClient

# client = MongoClient(env["MONGO_URI"])


# app = Flask(__name__)

# db = client.test2



# logs = db.logs

# # @app.route('/<id>/<wow>', methods=['GET'])
# # def param_example(id, wow):
# #     print(id,wow)
# #     return(id)
# # @app.route('/whatever', methods=['POST'])
# # def whatever():
# #     data = request.get_json()
# #     print(data)
# #     return data

# @app.route('/logs', methods=['GET'])
# def get_logs():
#     result = logs.find()
#     print(result)
#     # return "abc"
#     return jsonify([{'_id': str(log['_id']), 'message': log['message']} for log in result]) 

# @app.route('/logs', methods=['POST'])
# def create_log():
#     data = request.get_json()
#     result = logs.insert_one({'message': data['message']})
#     return str(result.inserted_id), 201

# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     return "Hello World!"
# # @app.route('/hello/<name>', methods=['GET'])
# # def hello(name):
# #     return f"Hello, {name}"

# # @app.route('/add/<num1>/<num2>', methods=['GET'])
# # def add(num1, num2):
# #     result = float(num1) + float(num2)
# #     return f"{result}"

# # @app.route('/multiply/<num1>/<num2>', methods=['GET'])
# # def multiply(num1, num2):
# #     result = float(num1) * float(num2)
# #     return f"{result}"

# # @app.route('/subtract/<num1>/<num2>', methods=['GET'])
# # def subtract(num1, num2):
# #     result = float(num1) - float(num2)
# #     return f"{result}"

# # @app.route('/divide/<num1>/<num2>', methods=['GET'])
# # def divide(num1, num2):
# #     result = float(num1) / float(num2)
# #     return f"{result}"
# # @app.route('/greet/<name>', methods=['GET'])
# # def greet(name):
# #     names = [
# #         "Dominic",
# #         "Steven",
# #         "Dawn",
# #         "Fede",
# #         "Matthew",
# #         "Victor",
# #         "Brian",
# #         "Fuzzy",
# #         "Gowri",
# #         "Mitchell",
# #         "Hilal",
# #         "Justin",
# #         "Darya",
# #         "Andrew",
# #     ]
# #     if name in names:
# #         return f"Hello, {name}"
# #     else:
# #         return "Hello, stranger"
# if __name__ == '__main__':
#     app.run(debug=True)

