import os


# def check_local_port():
#     info_port = None
#     os.chdir("C:/Users")
#     port = os.popen("lsof -i :3000").readlines()
#     if len(port) != 0:
#         for text in port:
#             if "node" in text:
#                 info_port = text.split(" ")
#         pid = [port_data for port_data in info_port if port_data.isdigit()]
#         command = f"kill {int(pid[0])}"
#         os.system(command)

# check_local_port()

import subprocess
#
# command = ["lsof", "-i", ":3000"]
# output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT, shell=True)
# print()
# Теперь вы можете обрабатывать вывод команды, как вам нужно

import psutil

def kill_process_by_port(port):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            try:
                process = psutil.Process(conn.pid)
                print(process)
                process.terminate()
            except psutil.NoSuchProcess as e:
                print(f"Error terminating process: {e}")

# Используем функцию для завершения процесса на порту 3000
kill_process_by_port(3000)


