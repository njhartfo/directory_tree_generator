import os
import pathlib
import sys
from collections import deque

# CONSTANTS
PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
	def __init__(self, root_dir, dir_only=False, output_file=sys.stdout):
		self._output_file = output_file
		self._generator = _TreeGenerator(root_dir, dir_only)
		
	def genearte(self):
		tree = self._generator.build_tree()
		if self._output_file != sys.stdout:
			tree.appendleft("'''")
			tree.append("'''")
			self._output_file = open(
				self._output_file, mode = 'w', encoding="UTF-8"
			)
		with self._output_file as stream:
			for entry in tree:
				print(entry, file=stream)
		
class _TreeGenerator:
	# init
	# build tree
	# tree header
	# tree body generator
	# entry preparer
	# directory adder
	# file adder
	
