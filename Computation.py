import math

def k_genome_probabilities_compute(geneNumber, genomeLength):
    result = []
    constant = factorielle(genomeLength)
    totalGenomes = geneNumber ** genomeLength
    maxDistinctGeneNumber = min(geneNumber, genomeLength)
    for i in range(1, maxDistinctGeneNumber + 1):
        alpha_i = []
        n_tilde_i = []
        i_genome_number = k_parmi_n(i, geneNumber) * factorielle(i) * constant * family_genome_number_compute(alpha_i, n_tilde_i)
        result.append(i_genome_number / totalGenomes)
    return result

def family_genome_number_compute(alpha, n_tilde):
    result = 0
    for i in range(len(alpha)):
        temp = 1
        for j in range(len(alpha[i])):
            temp *= factorielle(alpha[i][j]) * factorielle(n_tilde[i][j]) ** alpha[i][j]
        result += 1 / temp
    return result


def factorielle(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def k_parmi_n(k, n):
    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    elif k == 1 or k == n - 1:
        return n
    else:
        numerateur = factorielle(n)
        denominateur = factorielle(k) * factorielle(n-k)
        return numerateur / denominateur

def triangle_pascal(n):
    print("1")
    for i in range(1, n + 1):
        line = "1"
        for j in range(1, i + 1):
            line = "{0} {1}".format(line, k_parmi_n(j, i))
        print(line)

def print_gnk(fileName, g_max):
    file = open(fileName, "w")
    gnk = build_decompo(g_max)
    summarize_string = ""
    decomposition_string = ""
    for g in range(1, g_max):
        decomposition_string += "Decomposition de {0} :\n".format(g)
        summarize_string += "Decomposition de {0} :\n".format(g)
        for k in range(1, g + 1):
            summarize_string += "{0} : {1}\n".format(k, len(gnk[g][k-1]))
            for decomposition in gnk[g][k - 1]:
                string = "{0}".format(decomposition[0])
                for i in range(1, len(decomposition)):
                    string = "{0} + {1}".format(string, decomposition[i])
                decomposition_string += "{0}\n".format(string)
        summarize_string += "\n"
        decomposition_string += "\n"
    file.write(summarize_string)
    file.write(decomposition_string)
    file.close()

def build_decompo(max_G):
    G_n_k = [[]]
    for g in range(1, max_G):
        g_decompo = []
        for k in range(1, g + 1):
            k_decompo = []
            if k == 1:
                k_decompo.append([g])
            elif k == g:
                k_decompo.append([1] * g)
            else :
                min = math.ceil(g / k)
                max = g - (k - 1)
                for g_tilde in range(max, min - 1, -1):
                    k_minus_decompo = G_n_k[g - g_tilde][k - 2] #(k-2) car indice de liste décale tout de 1
                    count = 0
                    while (count < len(k_minus_decompo) and k_minus_decompo[count][0] <= g_tilde):
                        k_decompo.append([g_tilde] + k_minus_decompo[count])
                        count += 1
            g_decompo.append(k_decompo)
        G_n_k.append(g_decompo)
    return G_n_k