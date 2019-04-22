from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData,functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif(functionName == "divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        #if I am here, then the resource Add was requested using the method POST

        #step 1 : Get posted Data:
        postedData = request.get_json()

        #step 1 b: varify validity of posted data
        status_code = checkPostedData(postedData,"add")
        if (status_code != 200):
            retJson = {
                "Message":"An error happened",
                "Status Code" : status_code
            }
            return jsonify(retJson)
        #if I am here status code is 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)
        #step 2 : add the Posted data
        ret = x + y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        #if I am here, then the resource Subtract was requested using the method POST

        #step 1 : Get posted Data:
        postedData = request.get_json()

        #step 1 b: varify validity of posted data
        status_code = checkPostedData(postedData,"subtract")
        if (status_code != 200):
            retJson = {
                "Message":"An error happened",
                "Status Code" : status_code
            }
            return jsonify(retJson)
        #if I am here status code is 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)
        #step 2 : Subtract the Posted data
        ret = x - y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #if I am here, then the resource Multiply was requested using the method POST

        #step 1 : Get posted Data:
        postedData = request.get_json()

        #step 1 b: varify validity of posted data
        status_code = checkPostedData(postedData,"multiply")
        if (status_code != 200):
            retJson = {
                "Message":"An error happened",
                "Status Code" : status_code
            }
            return jsonify(retJson)
        #if I am here status code is 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)
        #step 2 : Multiply the Posted data
        ret = x * y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        #if I am here, then the resource Divide was requested using the method POST

        #step 1 : Get posted Data:
        postedData = request.get_json()

        #step 1 b: varify validity of posted data
        status_code = checkPostedData(postedData,"divide")
        if (status_code != 200):
            retJson = {
                "Message":"An error happened",
                "Status Code" : status_code
            }
            return jsonify(retJson)
        #if I am here status code is 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)
        #step 2 : add the Posted data
        ret = (x*1.0)/y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


@app.route('/')
def hellp_world():
    return "hello everyone!"



if __name__ == "__main__":
    app.run(debug = True)
