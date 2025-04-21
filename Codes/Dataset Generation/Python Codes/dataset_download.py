############################## FMNIST Dataset  #################################
# import itertools
# import pandas as pd

# import torch
# import torchvision
# import torchvision.transforms as transforms
# import os
# from PIL import Image

# # Define a transform to convert the data to tensor and resize the image
# transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Resize((64, 64))
# ])

# # Download and load the training data
# trainset = torchvision.datasets.FashionMNIST(root='./data', train=True,
#                                              download=True, transform=transform)
# trainloader = torch.utils.data.DataLoader(trainset, batch_size=1,
#                                           shuffle=True, num_workers=2)

# # Define the classes
# classes = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#            'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot')

# # Create a directory to save images
# save_dir = './fashion_mnist_images'
# if not os.path.exists(save_dir):
#     os.makedirs(save_dir)

# # Create a directory for each class
# for class_name in classes:
#     class_dir = os.path.join(save_dir, class_name.replace('/', '_'))
#     if not os.path.exists(class_dir):
#         os.makedirs(class_dir)

# # Dictionary to keep track of saved images count for each class
# saved_counts = {class_name: 0 for class_name in classes}

# # Save images
# for images, labels in trainloader:
#     class_name = classes[labels[0]]
#     # Convert the tensor to a PIL image
#     img = transforms.ToPILImage()(images[0])
#     # Replace invalid characters in class names
#     class_name_safe = class_name.replace('/', '_')
#     # Save the image in the corresponding class directory with a class label and count
#     class_dir = os.path.join(save_dir, class_name_safe)
#     img.save(os.path.join(class_dir, f'{class_name_safe}_{saved_counts[class_name]}.png'))
#     saved_counts[class_name] += 1
#     print(f'Saved {class_name_safe}_{saved_counts[class_name] - 1}.png')

# print("All images have been saved successfully.")
################################### MNIST Dataset ######################################
import torch
import torchvision
import torchvision.transforms as transforms
import os
from PIL import Image

# Define a transform to convert the data to tensor and resize the image
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((64, 64))  # Resize the image (optional)
])

# Download and load the MNIST dataset
trainset = torchvision.datasets.MNIST(root='./data_mnist', train=True,
                                      download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=1,
                                          shuffle=True, num_workers=2)

# Define the classes (digits 0-9)
classes = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Create a directory to save images
save_dir = './mnist_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Create a directory for each class
for class_name in classes:
    class_dir = os.path.join(save_dir, class_name)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

# Dictionary to keep track of saved images count for each class
saved_counts = {class_name: 0 for class_name in classes}

# Save images
for images, labels in trainloader:
    class_name = classes[labels[0]]
    # Convert the tensor to a PIL image
    img = transforms.ToPILImage()(images[0])
    # Save the image in the corresponding class directory with a class label and count
    class_dir = os.path.join(save_dir, class_name)
    img.save(os.path.join(class_dir, f'{class_name}_{saved_counts[class_name]}.png'))
    saved_counts[class_name] += 1
    print(f'Saved {class_name}_{saved_counts[class_name] - 1}.png')

print("All images have been saved successfully.")
