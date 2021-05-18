import sys
import subprocess


subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pillow'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'keyboard'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'opencv-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'python-imagesearch'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pyscreenshot'])
# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
