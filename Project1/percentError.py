def main():
    obs, the = [], [] #for step size 10
    for line in open("results10","r"):
        values = [float(s) for s in line.split()]
        the.append(values[1])
        obs.append(values[2])
    total = 0.0
    for i in range(len(obs)):
        total = total+(the[i]-obs[i])/the[i]
    total = total/len(obs)*100
    print("The average percent error is: " + str(total))
    obs2, the2 = [], []
    for line in open("results2", "r"):
        values2 = [float(s) for s in line.split()]
        obs2.append(values2[2])
        the2.append(values2[1])
    total = 0.0
    for i in range(len(obs2)):
        total = total+(the2[i]-obs2[i])/the2[i]
    total = total/len(obs2)
    print("The average percent error is: " + str(total))
    obsr, ther = [],[]
    total = 0.0
    for line in open("results-rk4","r"):
        valuesr = [float(s) for s in line.split()]
        ther.append(valuesr[1])
        obsr.append(valuesr[2])
    for i in range(len(ther)):
        total = total + (ther[i]-obsr[i])/ther[i]
    total = total/len(ther)*100
    print("The average percent error is: " + str(total))
main()
