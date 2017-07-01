from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import sys
import pandas as pd

def getExps(file_path):
    exp_file  = open(file_path, 'r');
    exp = dict()
    for line in exp_file:
        idx, val1, val2 = line.split(",")
        idx =  float(idx)
        val2 = float(val2.strip())
        val1 = float(val1)
        if idx in exp:
            exp[idx].append((val1, val2))
        else:
            exp[idx] = [(val1, val2)]
    exp_file.close()
    return exp


def main(args):
    exp = getExps(args[1])
    std_exp = [np.std(np.asarray(exp[round(val*0.1, 2)]), axis=0)
            for val in range(1, 10, 1)]
    std_exp = np.asarray(std_exp)
    
    print(std_exp)
    df_exp = pd.DataFrame([stats.describe(exp[round(val*0.1, 2)]).mean
        for val in range(1, 10, 1)], columns=["Clustering", "Diameter"],
        index = exp.keys())
    
    sns.set()
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].plot(df_exp["Clustering"], label="Mean Clustering Coefficient")
    ax[1].plot(df_exp["Diameter"], label="Mean Diameter")
    ax[0].set_xlabel("Rewiring probability")
    ax[0].set_ylabel("Clustering Coefficient")
    ax[1].set_xlabel("Rewiring probability")
    ax[1].set_ylabel("Diameter")
    ax[0].fill_between(df_exp.index, 
            df_exp["Clustering"]-std_exp[0:,0], 
            df_exp["Clustering"]+std_exp[0:,0], alpha=0.5, label="Standard Deviation")
    ax[1].fill_between(df_exp.index, 
            df_exp["Diameter"]-std_exp[0:,0], 
            df_exp["Diameter"]+std_exp[0:,1], alpha=0.5, label="Standard Deviation")
    ax[0].legend(loc="upper right")
    ax[1].legend(loc="upper right")
    plt.suptitle("Clustering Coefficiente and Diameter")
    plt.show()


if __name__ == '__main__':
    main(sys.argv)

