import matplotlib.pyplot as plt
import pandas as pd


def trait_irm(file):
    row_file = open("input-data/" + file, "r")

    rowdata = row_file.readlines()
    i = 0
    treated = []

    for line in rowdata:
        i += 1
        if i > 94:
            if len(line.replace("\n", "").split(",")) == 3:
                treated.append(line.replace("\n", "").split(","))

            elif len(line.replace("\n", "").split(",")) == 1:
                break

    df = pd.DataFrame(treated, columns=["f", "m", "nm"])

    df["f"] = df["f"].astype(float)
    df["m"] = df["m"].astype(float)
    df["nm"] = df["nm"].astype(float)

    return df


def trait_his(file):
    row_file = open("input-data/" + file, "r")

    rowdata = row_file.readlines()
    i = 0
    treated = []

    for line in rowdata:
        i += 1
        if i > 86:
            if len(line.replace("\n", "").split(",")) == 5:
                treated.append(line.replace("\n", "").split(","))

    df = pd.DataFrame(treated, columns=["f", "m", "af", "am", "nm"])

    df["f"] = df["f"].astype(float)
    df["m"] = df["m"].astype(float)
    df["af"] = df["af"].astype(float)
    df["am"] = df["am"].astype(float)
    df["nm"] = df["nm"].astype(float)

    df["nm"] = df["nm"] / df["nm"].max()
    df["am"] = df["am"] / df["am"].max()
    df["m"] = df["m"] / df["m"].max()

    return df


def plot(his, irm, name):
    his_data = trait_his(his)
    irm_data = trait_irm(irm)

    figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(his_data.af, his_data.nm, label='corrected', color='red')
    ax1.plot(his_data.af, his_data.m, label='uncorrected', color='royalblue')
    ax1.legend(loc='best')
    ax1.set_xlabel(r'$B \ (T)$')
    ax1.set_ylabel(r'$M/M_{MAX}$')
    ax1.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax1.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax1.hlines(0, -1, 1, color='k', alpha=0.2, linestyle='dashed')
    ax1.vlines(0, -1, 1, color='k', alpha=0.2, linestyle='dashed')
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)

    ax2.scatter(irm_data.f, irm_data.nm, marker='o', color='r')
    ax2.plot(irm_data.f, irm_data.nm, color='k')
    ax2.set_xlabel(r'$B \ (T)$')
    ax2.set_ylabel(r'$IRM \ (Am^{2}/kg)$')

    plt.tight_layout()
    plt.savefig("output-data/" + name + ".png", dpi=200)
    plt.close()
