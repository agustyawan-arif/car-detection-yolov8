# Create the Kaggle directory
mkdir ~/.kaggle

# Copy the Kaggle API key file to the Kaggle directory
cp kaggle.json ~/.kaggle/

# Set appropriate permissions for the Kaggle API key file
chmod 600 ~/.kaggle/kaggle.json

# Download the car-object-detection dataset
kaggle datasets download sshikamaru/car-object-detection

# Unzip the downloaded dataset
unzip car-object-detection

# Create directory structure for training data
mkdir '/content/data/train_data'
mkdir '/content/data/train_data/images'
mkdir '/content/data/train_data/labels'

# Create directory structure for validation data
mkdir '/content/data/val_data'
mkdir '/content/data/val_data/images'
mkdir '/content/data/val_data/labels'