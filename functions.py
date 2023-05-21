import matplotlib.pyplot as plt
import numpy as np


def hysteresis_load(file):
    f, m, af, am, nm = np.loadtxt(file, delimiter=',', skiprows=86, max_rows=2003, unpack=True)
    nm = nm / max(nm)
    am = am / max(am)
    m = m / max(m)
    return f, m, af, am, nm


def irm_load(file):
    f, m, nm = np.loadtxt(file, delimiter=',', skiprows=94, max_rows=101, unpack=True)
    return f, m, nm


def plot(his, irm, name):
    f1, m1, af1, am1, nm1 = hysteresis_load("input-data/"+his)
    f_irm, m_irm, nm_irm = irm_load("input-data/"+irm)

    figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(af1, nm1, label='corrected', color='red')
    ax1.plot(af1, m1, label='uncorrected', color='royalblue')
    ax1.legend(loc='best')
    ax1.set_xlabel(r'$B \ (T)$')
    ax1.set_ylabel(r'$M/M_{MAX}$')
    ax1.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax1.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax1.hlines(0, -1, 1, color='k', alpha=0.2, linestyle='dashed')
    ax1.vlines(0, -1, 1, color='k', alpha=0.2, linestyle='dashed')
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)

    ax2.scatter(f_irm, nm_irm, marker='o', color='r')
    ax2.plot(f_irm, nm_irm, color='k')
    ax2.set_xlabel(r'$B \ (T)$')
    ax2.set_ylabel(r'$IRM \ (Am^{2}/kg)$')

    plt.tight_layout()
    plt.savefig("output-data/" + name + ".png", dpi=200)
    plt.close()
