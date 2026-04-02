import signal, subprocess, os
from flask import Flask

app = Flask(__name__)

def check_port(port: int) -> list[int]:
    command = ['lsof', '-i', f':{port}']
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pids = []
    for proces in result.stdout.split('\n')[1:]:
        if 'LISTEN' in proces:
            pids.append(int(proces.split()[1]))
    return pids

def kill_processes(pids: list[int]):
    for pid in pids:
        try:
            os.kill(pid, signal.SIGKILL)
        except PermissionError:
            print(f"No permission to kill PID {pid}")
        except ProcessLookupError:
            print(f"Process PID {pid} not found")

@app.route('/')
def simpl():
    return 'All done'

if __name__ == '__main__':
    processes = check_port(5000)
    if processes:
        print(f"Порт 5000 используется процессом: {processes}.")
        kill_processes(processes)
        print('The port is released')

    app.run(debug=False)