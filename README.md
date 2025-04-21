# Neural Network Augmented Compressor Selection for Error-Tolerant Multiplier Architecture Design

## Abstract 
Finding an optimal architectural design based on the application is one of the problems that researchers’ struggle to arrive at owing to the tedious nature of the task. Machine Learning based models have garnered popularity in such areas as they are time and cost effective. This work proposes a machine learning (ML) based model to design the best approximate multiplier from a varied set of compressors, which otherwise
requires an exhaustive design-space search approach or time consuming Meta-Heuristic optimization technique. A model is trained with custom parameters comprised of both hardware metrics and image based characteristics for the filtering operation on images. The dataset is further modified using clustering to enhance the accuracy. The model presents more than 85% accuracy with higher levels of clustering, for designing in-exact multipliers that offer hardware benefits and desired image output characteristics. All the model files, design files, and dataset for training the model is made freely available for easy adoption and further usage to the designers community.

## Tree Structure Navigation

- **`Dataset/`**: Contains the dataset info used in this work
  - **`Before Clustering/`**: Initial dataset created with SSIM and hardware metrics for all ccompressor combinations.
     - **`FMNIST/`**: [Dataset](https://iiitbac-my.sharepoint.com/:x:/g/personal/rachana_kaparthi_iiitb_ac_in/EeLTKVVfF2BPtMKkEQZqC88Bl3hZUCa1AgVIb3Zp8rFRqg?e=Xqyo7Q) derived from convolution on FMNIST images.
     - **`MNIST/`**: [Dataset](https://iiitbac-my.sharepoint.com/:x:/g/personal/rachana_kaparthi_iiitb_ac_in/Eb4zZBcZeHtEk3gHNEeiayEBbKPHdskqsFSWbZGr9lcjgw?e=f2aFJh) derived from convolution on MNIST images. 
  - **`After Clustering/`**: Dataset after performing the clustering. The number of datapoints are now reduced.
     - **`FMNIST/`**: Dataset derived from clustering the initial dataset of convolution on FMNIST images. Multiple levels of clustering are considered.
     - **`MNIST/`**: Dataset derived from clustering the initial dataset of convolution on MNIST images. Multiple levels of clustering are considered.
     - **`HASYV2/`**: Dataset derived from clustering the initial dataset of convolution on HASYV2 images. Multiple levels of clustering are considered.


- **`Codes/`**:  
  - **`Dataset Generation/`**: Codes for generation of initial datasets (before clustering).
     - **`Python_Codes/`**: Contains all python codes required for dataset generation.
     - **`Verilog_Codes/`**: Contains all verilog codes related to compressor and multiplier.
  - **`Clustering/`**: Codes for performing the custom clustering technique.
  - **`NN/`**: Neural Network Architecture design, train and test codes.


