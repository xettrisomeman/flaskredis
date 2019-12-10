from flask import Flask 
import redis 


app = Flask(__name__)
redisClient = redis.Redis(host='redis')



@app.route('/')
def hello():
    cache = redisClient.incr('visit')
    return f"This is your {cache} visits"


if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)

