from flask import Flask, render_template, request, redirect
from Model.DatabaseClass import Database


app = Flask(__name__)
database = Database()

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/students")
def getStudents():
    return render_template("students.html", students=database.students)

@app.route("/courses")
def getCourses():
    return render_template("courses.html", courses=database.courses)

@app.route("/courses/add",methods=["POST"])
def addCourse():
    c_name = request.form.get("c_name")
    c_credit = request.form.get("c_credit")
    c_ins = request.form.get("c_ins")
    database.addCourse(c_name,c_credit,c_ins)
    return redirect("/courses")

@app.route("/students/add",methods=["POST"])
def addStudent():
    st_name = request.form.get("st_name")
    st_age = request.form.get("st_age")
    database.addStudent(st_name,st_age)
    return redirect("/students")

# @app.route("/enrollments/enroll", methods=["POST"])
# def enrollStudentInCourse():
#     data = request.json
#     studentID = data["student_id"]
#     courseID = data["course_id"]
#     #MAIN LOGIC
#     return jsonify({"message": "Student enrolled in course successfully"}), 200
#
# @app.route("/enrollments/courses/<course_id>", methods=["GET"])
# def getEnrolledStudentsInCourse():
#     pass
#
# @app.route("/enrollments/students/<student_id>", methods=["GET"])
# def getCoursesOfStudent():
#     pass


