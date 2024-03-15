import subprocess

process1 = subprocess.Popen(["python", "api.py"])
process2 = subprocess.Popen(["python", "form.py"])

process1.wait()
process2.wait()
