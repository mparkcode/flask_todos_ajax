from flask import Flask, render_template, request, redirect
import os
import json

app = Flask(__name__)

tasks = {
    1: {
        "id": 1,
        "name": "Get coffee",
        "description": "Decaf",
        "urgent": True,
        "done": True,
    },
    2: {
        "id": 2,
        "name": "Get milk",
        "description": "In a carton",
        "urgent": False,
        "done": True,
    },
    3: {
        "id": 3,
        "name": "Learn to code",
        "description": "Python",
        "urgent": False,
        "done": False,
    },
    4: {
        "id": 4,
        "name": "Get a job",
        "description": "Preferably that pays a lot",
        "urgent": False,
        "done": True,
    },
}

next_id = 5


@app.route("/")
def show_index():
    return render_template("index.html", tasks=tasks.values())

@app.route("/add", methods=["GET", "POST"])
def show_add_form():
    global next_id
    if request.method == "POST":
        new_item = {
            "id": next_id,
            "name": request.form["name"],
            "description": request.form["description"],
            "urgent": "urgent" in request.form,
            "done": "done" in request.form,
        }
        
        tasks[next_id] = new_item
        next_id += 1
        return redirect("/")        
    else:
        return render_template("todo_form.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    if request.method == "POST":
        changed_item = {
            "id": id,
            "name": request.form["name"],
            "description": request.form["description"],
            "urgent": "urgent" in request.form,
            "done": "done" in request.form
        }
        tasks[id] = changed_item
        return redirect("/")
    else:
        return render_template("edit_task_form.html", task = tasks[id])



@app.route("/toggle/<int:id>", methods=["POST"])
def toggle_task(id):
    task = tasks[id]
    task['done'] = not task['done']
    tasks[id] = task
    return json.dumps(task)



if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)