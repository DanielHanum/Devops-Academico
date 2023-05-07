from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas armazenadas em memória
tasks = []

index_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Tarefas</title>
</head>
<body>
    <h1>Lista de Tarefas</h1>
    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Digite uma nova tarefa" required>
        <input type="submit" value="Adicionar">
    </form>
    <ul>
        {% for task in tasks %}
            <li>
                {{ task }}
                <a href="{{ url_for('delete_task', task_id=loop.index0) }}">X</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(index_template, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

