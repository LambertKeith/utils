import shutil
import os
import zipfile
import time
import random
import string
from datetime import datetime

def generate_random_hex(length):
    """Generate a random hexadecimal string of given length."""
    return ''.join(random.choices(string.hexdigits.lower(), k=length))

def write_version_to_file():
    """Write date information (with seconds) and 8-digit random hex to version.txt."""
    now = datetime.now().strftime('%Y%m%d.%H%M%S')
    random_hex = generate_random_hex(8)
    version_info = f"{now}.{random_hex}"

    file_path = os.path.join(os.getcwd(), "version.txt")

    with open(file_path, "w") as file:
        file.write(version_info)
        
    return version_info
        
def create_zip(zip_filename, directories=[], files=[]):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for directory in directories:
            for root, _, filenames in os.walk(directory):
                if '__pycache__' in root:
                    continue 
                base_name = os.path.basename(directory)
                for filename in filenames:
                    if filename.endswith('.pyc'):
                        continue
                    file_path = os.path.join(root, filename)
                    arcname = os.path.relpath(file_path, directory)
                    zipf.write(file_path, base_name + "/" + arcname)

        for file in files:
            if '__pycache__' in file or file.endswith('.pyc'):
                continue
            zipf.write(file, os.path.basename(file))
            
        
            
# Example usage
if __name__ == "__main__":
    
    version_info = write_version_to_file()
    
    app_name = "text_format_conversion"
    
    directories = ['data', 'llm_utils', 'text_format_conversion']  # Replace with your list of directories to be included in the zip
    files = ["version.txt", "deploy.txt",f"start_{app_name}.sh",f"{app_name}_main.py","cmd.txt"]      # Replace with your list of files to be included in the zip
    target_zip_path = f"{app_name}.zip"  # Replace with the desired output zip file path        
    
    create_zip(target_zip_path, directories, files) 
    
    shutil.copy(target_zip_path, f"dist/{app_name}_{version_info}.zip")