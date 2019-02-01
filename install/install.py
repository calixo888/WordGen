import subprocess

subprocess.call("curl https://bootstrap.pypa.io/get-pip.py | python",shell=True)
subprocess.call("pip install tqdm",shell=True)
print('[+] All packages successfully installed')
