import matplotlib.pyplot as plt
import math as mt
import random
import numpy as np
import statistics as st
import seaborn as sns


class CLT:

    def __init__(self):
        self.number_of_tosses = 0
        self.size_of_sample = 0
        self.number_of_samples = 0
        self.tosses = []
        self.samples = []

        self.set_number_of_tosses()
        self.set_size_of_sample()
        self.set_number_of_samples()
        self.__simulate_tosses()
        self.__simulate_samples()

    def set_number_of_tosses(self):
        input_message = "Enter the number of tosses you would like to be performed: "
        warning_message = "that's not a valid number of tosses. Try again \n"
        self.number_of_tosses = get_input(input_message, warning_message)

    def set_size_of_sample(self):
        input_message = "Enter the size of sample you would like to be taken: "
        warning_message = "that's not a valid size of samples. Try again \n"
        self.size_of_sample = get_input(input_message, warning_message)
        while self.size_of_sample > self.number_of_tosses:
            print("Size of sample should be strictly lower than the number of tosses\n")
            self.size_of_sample = get_input(input_message, warning_message)

    def set_number_of_samples(self):
        input_message = "Enter the number of samples you would like to be taken: "
        warning_message = "that's not a valid number of samples. Try again \n"
        self.number_of_samples = get_input(input_message, warning_message)

    def __simulate_tosses(self):
        self.tosses = [random.uniform(0, 1) for i in range(self.number_of_tosses)]

    def __simulate_samples(self):
        self.samples = [st.mean(random.sample(self.tosses, self.size_of_sample))
                        for i in range(self.number_of_samples)]

    def displaySamples(self):
        set_of_point = np.asarray(self.samples)
        num_bins = round(1 + mt.log2(self.number_of_samples))
        fig = plt.figure(figsize=(12, 4))
        ax2 = fig.add_subplot(1, 2, 1)
        ax2 = sns.histplot(set_of_point, bins=num_bins, kde=True)
        ax2.lines[0].set_color('crimson')
        plt.show()

    def showInAction(self):
        num_bins = round(1 + mt.log2(self.number_of_samples))

        fig = plt.figure(figsize=(12, 8))
        ax1 = fig.add_subplot(2, 2, 1)  # add an Axes called ax1
        ax2 = fig.add_subplot(2, 2, 2)  # add an Axes called ax2
        ax3 = fig.add_subplot(2, 2, 3)  # add an Axes called ax3
        ax4 = fig.add_subplot(2, 2, 4)
        original_samples_size = self.number_of_samples

        self.number_of_samples = self.number_of_samples * 2
        set_of_point = np.asarray([st.mean(random.sample(self.tosses, self.size_of_sample))
                                   for i in range(self.number_of_samples)])
        sns.histplot(set_of_point, bins=num_bins, ax=ax1, kde=True)

        self.number_of_samples = self.number_of_samples * 2
        set_of_point = np.asarray([st.mean(random.sample(self.tosses, self.size_of_sample))
                                   for i in range(self.number_of_samples)])
        sns.histplot(set_of_point,label='test_label1', bins=num_bins, ax=ax2, kde=True)

        self.number_of_samples = self.number_of_samples * 2
        set_of_point = np.asarray([st.mean(random.sample(self.tosses, self.size_of_sample))
                                   for i in range(self.number_of_samples)])
        sns.histplot(set_of_point,label='test_label2', bins=num_bins, ax=ax3, kde=True)

        self.number_of_samples = self.number_of_samples * 2
        set_of_point = np.asarray([st.mean(random.sample(self.tosses, self.size_of_sample))
                                   for i in range(self.number_of_samples)])
        sns.histplot(set_of_point, bins=num_bins, ax=ax4, kde=True)

        plt.show()
        self.number_of_samples = original_samples_size


def get_input(input_message, warning_message):
    while True:
        try:
            value = int(input(input_message))
            if value <= 0:
                print(warning_message)
                continue
        except ValueError:
            value = 0
            print(warning_message)
            continue
        break
    return int(value)
