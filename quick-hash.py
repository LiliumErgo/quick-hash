import os
import hashlib
import argparse

def compute_hash(file_path):
    """Compute SHA256 hash of a file"""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def write_hashes_to_file(folder_path, output_file):
    """Write SHA256 hashes of all images in a folder to a file"""
    with open(output_file, 'w') as f:
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(folder_path, file_name)
                hash_value = compute_hash(file_path)
                f.write(f'{file_name}: {hash_value}\n')

def main():
    parser = argparse.ArgumentParser(description="Compute SHA256 hashes of images in a folder")
    parser.add_argument('folder_path', help="Path to the folder of images")
    parser.add_argument('output_file', help="Path to the output file")
    args = parser.parse_args()
    write_hashes_to_file(args.folder_path, args.output_file)

if __name__ == "__main__":
    main()
