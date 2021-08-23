import subprocess

if __name__ == '__main__':
    subprocess.run('cd app')
    subprocess.run('export FLASK_APP=app')
    subprocess.run('flask run')