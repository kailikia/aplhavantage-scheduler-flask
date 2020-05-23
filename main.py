from flask import Flask
from my_scheduler import scheduler,callThis

app = Flask(__name__)

#Create the scheduler job
scheduler.add_job(callThis, 'interval', minutes=1)
#start the scheduler
scheduler.start()

@app.route('/')
def home():
    return 'Testing scheduler'

if __name__ == '__main__':
    app.run()



