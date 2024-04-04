from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data scientist',
    'location': 'Deli, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Front eng Engineer',
    'location': 'Remote',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 4,
    'title': 'backend eng Engineer',
    'location': 'USA',
    'salary': '$15,00,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs = JOBS,
                        company_name = 'Jovian_wocao')
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  


if __name__ == "__main__":
  # app.run(host="0.0.0.0", debug=True, port=8080)
  app.run(host="0.0.0.0", debug=True)
