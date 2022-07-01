import matplotlib.pyplot as plt
def main():
    t, rk, an = [], [], []
    for line in open("results-rk4", "r"):
        values = [float(s) for s in line.split()]
        t.append(values[0])
        an.append(values[1])
        rk.append(values[2])
    plt.plot(t,an, label= "Analytical")
    #plt.scatter(t,an)
    plt.plot(t,rk, label = "RK4")
    plt.scatter(t,rk)
    plt.axis([0,700,0,100])
    plt.xlabel("Time (yrs.)")
    plt.ylabel("Particles Remaining (%)")
    plt.legend()
    plt.grid()
    plt.title("RK4 Radioactive Decay")
    plt.show()
main()
