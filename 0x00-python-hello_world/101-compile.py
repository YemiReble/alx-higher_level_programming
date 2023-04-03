#!/usr/bin/python3

import py_compile

filename = "main.py"

try:
	py_compile.compile(filename)
	print("Compiling {}...".format(filename))
except py_compile.PyCompileError:
	print("Error Compiling File")
