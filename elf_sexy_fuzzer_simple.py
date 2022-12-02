import elf
import random

# Load the ELF file.
elf_file = elf.ELF("path/to/elf/file")

# Generate a random section name.
def generate_section_name():
  # Generate a random string of 8 characters.
  name = ""
  for i in range(8):
    name += chr(random.randint(32, 126))
  return name

# Fuzz the ELF file's section names.
for section in elf_file.iter_sections():
  # Generate a random section name.
  name = generate_section_name()
  print("Fuzzing section name:", section.name, "->", name)

  # Try to load the ELF file with the new section name.
  try:
    section.name = name
    elf_file.save("path/to/output/file")
  except Exception as e:
    print
