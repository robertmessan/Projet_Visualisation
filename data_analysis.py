class DataAnalysis:

    def __init__(self, chaine):
        self.chaine = chaine
        self.chaine = [int(x) for x in self.chaine.split(',')]

    def max(self):
        maximum = float('-inf')

        for x in self.chaine:
            if x >= maximum:
                maximum = x
        return maximum

    def mean(self):
        somme = 0

        for x in self.chaine:
            somme += x
        moyenne = somme / len(self.chaine)
        return moyenne

    def get_bins(self, n_bins):
        dist = self.max() - min(self.chaine)
        return dist/n_bins


if __name__ == '__main__':
    data1 = DataAnalysis('20,90,50,50,22,46,99,54,55,44,66,15,18,50,88,2,59,25,69,2')
    max1 = data1.max()
    moy = data1.mean()
    print("Le maximum du tableau est:", max1)
    print("la mean du tableau est:", moy)
    print("le nombre d'intervalle de taille", 10, "est", data1.get_bins(10))
