#!/usr/bin/env python3

import argparse
import elf
import secrets

# Parse the command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-f", "filepath", help="path to the ELF file")
parser.add_argument("-i", "iterations", type=int, help="number of iterations to run")
args = parser.parse_args()

# Handle the uninitialized argparse variable.
if args.iterations is None:
  iterations = 1

# Load the ELF file.
elf_file = elf.ELF(args.filepath)

# Generate a random section name.
def generate_section_name():
  # Generate a random string of 8 characters.
  name = ""
  name = secrets.token_bytes(8)
  return name

# Fuzz the ELF file's section names.
for i in range(args.iterations):
  for section in elf_file.iter_sections():
    # Generate a random section name.
    name = generate_section_name()
    print("Iteration ", i, ": Fuzzing section name: ", section.name, " -> ", name, "\n")

    # Try to save the ELF file with the new section name.
    try:
      section.name = name
      elf_file.save("path/to/output/file")
    except Exception as e:
      print("Error: ", e, "\n")
