import random
from convolution import *
from area_power import *

import csv
# import time
import multiprocessing
from functools import partial


def util(l, i, j, k, inputimage, kernal, exactop, opfile):
    # start_time = time.time()

    # print(f"i = {i}, j = {j}, k = {k}, l = {l}")
    pos = [i, j, k, l]
    # pos = [1,4,5,6]
    print(pos)
    [approxop]=conv_3x3_sobel_approx(inputimage,kernal,pos)
    ssim = metrics.structural_similarity(exactop, approxop, data_range=1.0)
    mul = "mul" + str(i) + str(j) + str(k) + str(l)

    # Hardware parameters extrapolation
    area=area_45nm(pos)
    power=power_45nm(pos)


    # Write data to the CSV file
    with open(opfile, mode='a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow([mul, pos, ssim])
        writer.writerow([mul, pos, ssim, area, power, area * power])
   
   
    # print("            SSIM : ",ssim)
    # print("            Cost Function :", area*power)
    # print("Time taken ", time.time() - start_time)


if __name__ == "__main__":
    # inputimage = imread('./ML_compressor_configuration/python_files/cameraman.png')
    # kernal = np.array([[-39	,-81,107],[127,-94,-69],[-90,44,-128]])   //range converted Kernal Used for Fmnist
    kernal = np.array([[ -128,   -26 ,  -30],[ -17 ,  109  ,  99],[ 16  , 127   , 94]])  //Range Converted Kernal Used for Mnist

# kernal=[[-0.0215, -0.0401,  0.0427];
#          [ 0.0514, -0.0458, -0.0348];
#          [-0.0442,  0.0148, -0.0608]];



# kernal=[[-0.0307, -0.0070, -0.0080];
# [-0.0048, 0.0245, 0.0220];
# [ 0.0028, 0.0286, 0.0209]];
#Modify this according to the dataset being used to loop through the folders
    for digit in range(0,10): 
        for count in range(100,1000):
            ipfilename = f"./mnist_images/{digit}/{digit}_"+str(count)+".png"
            inputimage = imread(ipfilename)
            inputimage = (inputimage/2).astype(int)

            [exactop]=conv_3x3_sobel_exact(inputimage,kernal)
            print(f"exacttop done for {ipfilename}")
            opfile = f"./dataset_mnist/{digit}/{digit}_"+str(count)+".csv"
        

            # # Open a CSV file and create a CSV writer
            # csv_file = open('output.csv', mode='w', newline='')
            # csv_writer = csv.writer(csv_file)

            # # Write headers to CSV
            # csv_writer.writerow(['Multiplier', 'Position', 'SSIM', 'Area', 'Power', 'Cost function'])
            with open(opfile, mode='w', newline='') as file:
                writer = csv.writer(file)
                # writer.writerow(['Multiplier', 'Position', 'SSIM'])
                writer.writerow(['Multiplier', 'Position', 'SSIM', 'Area', 'Power', 'Cost function'])



            # st = time.time()
            # Print each combination
            for i in range(1,10):
                for j in range(1,10):
                    for k in range(1,10):
                    
                        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        pool = multiprocessing.Pool(processes=9)
                        partial_func = partial(util, i=i, j=j, k=k, inputimage=inputimage, kernal=kernal, exactop=exactop, opfile=opfile)
                        pool.map(partial_func, numbers)
                        pool.close()
                        pool.join()
            # print("Total Time taken ", time.time() - st)
                            
