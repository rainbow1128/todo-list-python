# coding=utf-8
from flask import Flask, jsonify, request, abort
from task import TaskDAO
import pymongo

app = Flask('todoapp')
client = pymongo.MongoClient('mongodb://localhost')
database = client.todo_list
tasks_dao = TaskDAO(database)


@app.route('/tasks')
def list():
    return jsonify(tasks_dao.list()), 200


@app.route('/tasks', methods=['POST'])
def create():
    data = request.json
    title = data.get('title', None)
    description = data.get('description', None)

    if not title or not description:
        abort(400)

    task = tasks_dao.create(data)

    return jsonify(task), 201

app.run()
