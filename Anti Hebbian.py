#anti hebbian öğrenme kuralını oluşturur.
import numpy as np
def theta(t1, t2):
    return 1 if t1 == t2 else 0

def anti_hebbian(W, X, sigma, tau1, tau2, d):
    k, n = W.shape
    for (i, j), _ in np.ndenumerate(W):
        W[i, j] -= X[i, j] * tau1 * theta(sigma[i], tau1) * theta(tau1, tau2)
        W[i, j] = np.clip(W[i, j], -d, d)
        print('Wgüncel=',W) #güncel ağırlık
        print('tau1=',tau1) #TPM1 çıkışı
        print('tau2=',tau2) #TPM2 çıkışı
