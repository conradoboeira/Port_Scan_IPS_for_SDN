import subprocess

ad = ["10.0.0.21",
      "10.0.0.31",
      "10.0.0.33",
      "10.0.0.41",
      "10.0.0.42"]

for a in ad:
    subprocess.call(["nmap","-p 8000", a])
