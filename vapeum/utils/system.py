"""
Gives information about the current operating system.
"""
import sys

def is_windows():
	return sys.platform in ('win32', 'cygwin')

def _is_mac():
	return sys.platform == 'darwin'

def _is_linux():
	return sys.platform.startswith('linux')

def get_canonical_os_name():
	if is_windows():
		return 'windows'
	elif _is_mac():
		return 'mac'
	elif _is_linux():
		return 'linux'
