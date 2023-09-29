"""

In an API, typically, some kind of data is accessible

via HTTP requests (GET/POST/PUT/PATCH/DELETE)

http://localhost:1234/api/employees/234

When we visit (or access) the above URL, we are actual expecting an employee data whose id is 234


"""
import json
from flask import Flask, Response, request


app = Flask('myapp')


emps = [
    dict(id=121, name='John Scott', salary=23000, department='admin'),
    dict(id=827, name='Ramesh Kumar', salary=33000, department='marketing'),
    dict(id=918, name='Rajesh Rao', salary=12000, department='admin'),
    dict(id=672, name='Allen Smith', salary=16000, department='production')
]


@app.route('/')
def home_page():
    return '<h1>Hello, from Flask!</h1>'


@app.route('/api/employees/<int:emp_id>')
def get_employee_for_id(emp_id):
    result = [e for e in emps if e['id'] == emp_id]
    if len(result) == 1:
        return Response(json.dumps(result[0]), status=200, mimetype='application/json')
    else:
        err = {'err': f'No data found for {emp_id}'}
        return Response(json.dumps(err), status=404, mimetype='application/json')


@app.route('/api/employees', methods=['POST'])
def post_new_employee():
    data = request.get_json()
    if 'id' not in data or 'name' not in data:
        err = dict(err='id and name are mandatory')
        return Response(json.dumps(err), status=400, mimetype='application/json')

    result = [e for e in emps if e['id'] == data.get('id')]
    if len(result) == 1:
        err = dict(err=f'employee with this id {data.get("id")} already exists')
        return Response(json.dumps(err), status=400, mimetype='application/json')

    emps.append(data)
    return Response(json.dumps(data), status=201, mimetype='application/json')


@app.route('/api/employees/<int:emp_id>', methods=['PUT'])
def put_employee(emp_id):
    result = [e for e in emps if e['id'] == emp_id]
    if len(result) == 0:
        err = {'err': f'No data found for {emp_id}'}
        return Response(json.dumps(err), status=404, mimetype='application/json')

    emp_to_update = result[0]
    data = request.get_json()
    if 'id' in data:
        del data['id']

    emp_to_update.update(data)
    return Response(json.dumps(emp_to_update), status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=1234)
