import matplotlib.pyplot as plt
def main():
    t10, t2, yAct, y10, y2 = [], [], [], [], []
    for line in open("results10","r"):
        values = [float(s) for s in line.split()]
        t10.append(values[0])
        y10.append(values[2])
    for line in open("results2", "r"):
        values = [float(s) for s in line.split()]
        t2.append(values[0])
        yAct.append(values[1])
        y2.append(values[2])
    plt.plot(t10,y10, label = "31.645 Years")
    plt.plot(t2,yAct, label  = "Analytic Solution")
    plt.plot(t2,y2, label= "6.329 Years")
    plt.scatter(t10,y10, s=5)
    #plt.scatter(t2,yAct, s=5)
    plt.scatter(t2,y2, s=5)
    plt.axis([0,700,0,100])
    plt.xlabel("Time (yrs.)")
    plt.ylabel("Particles Remaining (%)")
    plt.legend()
    plt.grid()
    plt.title("Euler's Method Radioactive Decay")
    plt.show()
main()
