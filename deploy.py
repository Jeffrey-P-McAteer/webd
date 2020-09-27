#!/usr/bin/env python3

import os
import sys
import subprocess

from common import *

def main(argv):
  subprocess.run([sys.executable, 'build.py']).check_returncode()
  check_cmds()
  read_in_secrets()

  if not 'DEPLOY_RSA_KEY' in os.environ:
    print("No environment variable DEPLOY_RSA_KEY found; set this in .secret_env to manage automatic deployments.")

  if not 'DEPLOY_ACCT' in os.environ:
    print("No environment variable DEPLOY_ACCT found; set this in .secret_env to manage automatic deployments.")

  # scp target/x86_64-unknown-linux-musl/release/webd to
  # the server using rsa key
  subprocess.run([
    'scp',
    '-i', os.environ['DEPLOY_RSA_KEY'],
    'target/x86_64-unknown-linux-musl/release/webd',
    os.environ['DEPLOY_ACCT']+'@webd.jmcateer.pw:/opt/'
  ]).check_returncode()

  # ssh in and re-start the webd binary.
  subprocess.run([
    'ssh',
    '-i', os.environ['DEPLOY_RSA_KEY'],
    os.environ['DEPLOY_ACCT']+'@webd.jmcateer.pw', '/opt/webd', 'run-daemon-fork'
  ]).check_returncode()


if __name__ == '__main__':
  main(sys.argv)

