import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def tumour_growth(C0, T, D, a, S, TD=180.):
    """
    :param c0: Initial tumour value
    :param T: End of simulation time
    :param D: drug matrix
    drug matrix
    np.array([
    ["d1", dose1, t1_start, t1_end]
    ["d1", dose2, t2_start, t2_end]
    ["d1", dose3, t3_start, t3_end]
    ...
    ["d2", dose1, t1_start, t1_end]
    ["d2", dose2, t2_start, t2_end]
    ["d2", dose3, t3_start, t3_end]
    ...
    ...
    ["d4", dose1, t1_start, t1_end]
    ["d4", dose2, t2_start, t2_end]
    ["d4", dose3, t3_start, t3_end]
    ])
    :param a: Allee shape parameter
    :param S: patient specific sensitivity values
    :param TD: tumour doubling time
    :return: C(t) cancer volume as function of time
    """
    g = np.log(2) / TD

    sol = integrate.solve_ivp(ode, t_span=(0, T), y0=(C0,), args=(g, a, S, D,), max_step=0.1,
                              method='LSODA')

    return sol


def ode(t, C, g, a, S, drug_matrix):
    s1, s2, s3, s4 = S

    d1 = drug_matrix[np.where(drug_matrix[:, 0] == "d1"), 1:4][0]
    d2 = drug_matrix[np.where(drug_matrix[:, 0] == "d2"), 1:4][0]
    d3 = drug_matrix[np.where(drug_matrix[:, 0] == "d3"), 1:4][0]
    d4 = drug_matrix[np.where(drug_matrix[:, 0] == "d4"), 1:4][0]

    h1 = d1[np.where((d1[:, 1] < t) & (t < d1[:, 2])), 0]
    if h1.size==0:
        h1 = 0.0

    h2 = d2[np.where((d2[:, 1] < t) & (t < d2[:, 2])), 0]
    if h2.size==0:
        h2 = 0.0

    h3 = d3[np.where((d3[:, 1] < t) & (t < d3[:, 2])), 0]
    if h3.size==0:
        h3 = 0.0

    h4 = d4[np.where((d4[:, 1] < t) & (t < d4[:, 2])), 0]
    if h4.size==0:
        h4 = 0.0


    return (g * np.square(C)) / (a + C) - s1 * h1 * C - s2 * h2 * C - s3 * h3 * C - s4 * h4 * C


def plot_solution(solution):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlabel("$t$")
    ax.set_ylabel("c(t)")
    plt.plot(solution.t, solution.y.T[:, 0], color="black", lw=2);


def final_tumour_volume(solution):
    return solution.y.T[:, 0][-1]