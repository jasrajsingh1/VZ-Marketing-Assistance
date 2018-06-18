from flask import Flask, request
from flask_restful import Resource, Api

ret = request.url('http://api.github.com/')
print ret.status_code

'''
e = create_engine('sqlite:///')

app = Flask(__name__)
api = Api(app)

class information(Resource):
    def get(self):
        # Connect to database
        conn = e.connect()
        # Perform query and return JSON data
        query = conn.execute("select * from information")
        return {'info: [i[0] for i in query.cursor.fetchall()]'}

api.add_resource(information, '/info')

if __name__ == '__main__':
    app.run()
'''