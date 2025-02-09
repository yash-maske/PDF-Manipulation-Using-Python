import os
file_path = "r2.pdf"
try:
  os.remove(file_path)
  print("File deleted successfully!")
except FileNotFoundError:
  print("Error: File not found.")
except PermissionError:
  print("Error: You don't have permission to delete the file.")
except OSError as e:
  print(f"Error deleting file: {e}")