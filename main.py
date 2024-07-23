import os
import sys

def process_folder(folder_path):
  '''
  Your code will go here. All required modules can be called from here
  '''
  
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    process_folder(folder_path)

if __name__ == "__main__":
    main()
