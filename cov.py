from flask import Flask,request,jsonify
from covid import Covid

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    d={}
    covid = Covid()
    country_name = request.args['Country']
    cases = covid.get_status_by_country_name(country_name)
    d[country_name] =cases['confirmed']
    return jsonify(d)

if __name__ == '__main__':
    app.run()