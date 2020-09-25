#!/usr/bin/env python3

import os, sys, subprocess

def cmd(*args):
  subprocess.run([x for x in args])

def build(target):
  print('>>> Building for {}'.format(target))
  cmd('cargo', 'build', '--release', '--target={}'.format(target))
  print('>>> {} Completed'.format(target))


if __name__ == '__main__':
  #build('x86_64-unknown-linux-gnu')
  build('x86_64-unknown-linux-musl')
  build('x86_64-pc-windows-gnu')
  #build('x86_64-apple-darwin') # TODO figure out why my cross-copile toolchain is broken



