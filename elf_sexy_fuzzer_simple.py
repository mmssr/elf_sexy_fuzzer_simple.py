#!/usr/bin/env python3

import argparse
import elf
import random

# Parse the command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="path to the ELF file")
parser.add_argument("iterations", type=int, help="number of iterations to run")
args = parser.parse_args()

# Load the ELF file.
elf_file = elf.ELF(args.filepath)

# Generate a random section name.
def generate_section_name():
  # Generate a random string of 8 characters.
  name = ""
  for i in range(8):
    name += chr(random.randint(32, 126))
  return name

# Fuzz the ELF file's section names.
for i in range(args.iterations):
  for section in elf_file.iter_sections():
    # Generate a random section name.
    name = generate_section_name()
    print("Iteration", i, ": Fuzzing section name:", section.name, "->", name)

    # Try to load the ELF file with the new section name.
    try:
      section.name = name
      elf_file.save("path/to/output/file")
    except Exception as e:
      print("Error:", e)
