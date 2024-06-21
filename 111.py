import os

checkpoint_path = 'D:\\Projects\\mpl2\\Wav2Lip\\checkpoints'

# Check if the path exists
if not os.path.exists(checkpoint_path):
    print(f"Path does not exist: {checkpoint_path}")

# Check if the path is a file
if not os.path.isfile(checkpoint_path):
    print(f"Path is not a file: {checkpoint_path}")

# Check read permissions
if not os.access(checkpoint_path, os.R_OK):
    print(f"Read permission denied for: {checkpoint_path}")

# Check write permissions
if not os.access(checkpoint_path, os.W_OK):
    print(f"Write permission denied for: {checkpoint_path}")
