#!/usr/bin/env python3

import os, sys, subprocess, time

from common import *

def build(target):
  print('>>> Building for {}'.format(target))
  cmd('cargo', 'build', '--release', '--target={}'.format(target))
  print('>>> {} Completed'.format(target))

def main():
  # We keep a branch of mozilla's authenticator library
  # here, but we add fixes so it can be compiled
  # for windows using the GNU toolchain.

  authenticator_lib = os.path.join('libs', 'authenticator')
  if not os.path.exists(authenticator_lib):
    subprocess.run([
      'git', 'submodule', 'add', 'https://github.com/mozilla/authenticator-rs.git', authenticator_lib
    ])
  else:
    # This exists, let's just pull from origin/main real quick
    subprocess.run(['git', 'submodule', 'init'])
    subprocess.run(['git', 'submodule', 'update'])
    subprocess.run(['git', 'checkout', 'main'], cwd=os.path.abspath(authenticator_lib))
    subprocess.run(['git', 'pull'],             cwd=os.path.abspath(authenticator_lib))
  
  os.environ['PKG_CONFIG_ALLOW_CROSS'] = '1'

  build('x86_64-unknown-linux-gnu')
  build('x86_64-unknown-linux-musl')
  build('x86_64-pc-windows-gnu')
  #build('x86_64-apple-darwin') # TODO figure out why my cross-copile toolchain is broken


if __name__ == '__main__':
  check_cmds();

  # Any 3rd party libraries that need updates will be cloned
  # as sub-modules here
  if not os.path.exists('libs'):
    os.makedirs('libs')

  main();

  # Optional arg, if given we do a pull + build continuously
  if 'poll' in sys.argv:
    print("Polling...")
    time.sleep(2)
    cmd('git', 'pull');
    main();


