
import os
import sys
import subprocess
import shutil

# Stolen from https://stackoverflow.com/a/60878313, thanks for such a succinct and pythonic impl!
def read_in_secrets():
  with open('.secret_env', 'r') as fh:
    vars_dict = dict(
        tuple([x.strip() for x in line.split('=')])
        for line in fh.readlines() if '=' in line and not line.startswith('#')
    )
    os.environ.update(vars_dict)

def read_in_version():
  with open('Cargo.toml', 'r') as fh:
    for line in fh.readlines():
      if line.startswith("version"):
        version_str = line.strip().split("=")[1].strip()
        version_str = version_str.replace('"', '')
        return version_str
  return '0.0.0'

def check_cmds():
  if sys.version_info[0] < 3:
    print('These scripts are written against python 3 APIs, you must use python 3. Current sys.version={}'.format(sys.version))
    sys.exit(1)
  cmds = [
    'cargo', 'rustc', 'git', 'ssh', 'scp'
  ];
  for c in cmds:
    check_cmd(c);

def check_cmd(binary):
  if not shutil.which(binary):
    print("Warning, missing tool: {}".format(binary))

def cmd(*args):
  subprocess.run([x for x in args])


