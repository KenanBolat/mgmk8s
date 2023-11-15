import time

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from ftplib import FTP

app = Flask(__name__)
scheduler = BackgroundScheduler()


def check_ftp():
    # FTP checking logic here
    # ...
    print('checking ftp ...')
    time.sleep(3)
    print('checking ftp ...')
    time.sleep(3)
    print('checking ftp ...')
    time.sleep(3)
    print('checking done ...')


@app.route('/start', methods=['GET'])
def start_monitoring():
    scheduler.add_job(func=check_ftp, trigger="interval", minutes=1)
    scheduler.start()
    return "FTP Monitoring Started"


@app.route('/stop', methods=['GET'])
def stop_monitoring():
    scheduler.shutdown()
    return "FTP Monitoring Stopped"


if __name__ == '__main__':
    app.run(debug=False, port=5021, host='0.0.0.0')
