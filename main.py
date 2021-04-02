import numpy as np
import matplotlib.pyplot as plt
# Pour la question 4
from scipy.optimize import minimize

from mpl_toolkits.mplot3d import Axes3D

# Labelsize (display)
labelsize   = 14
    
# Load the input data
# Input data (with missing traces)
gpanel = np.load('gpanel.npy')
# Dense data (with all traces, only for comparison)
panel_dense = np.load('panel_dense.npy')
nt, nx = gpanel.shape

# Vertical axis -- time
dt   = 3.125e-3  # increment (s)
at   = np.linspace(0,dt*(nt-1),nt)
# Horizontal axis -- space
dx   = 10. # increment (m)
ax   = np.linspace(0,dx*(nx-1),nx)

# # Display of the input data
# vmax    = np.max(np.abs(gpanel))
# fig = plt.figure()
# av = plt.subplot(111)
# plt.imshow(gpanel,extent=[ax[0],ax[-1],at[-1],at[0]],aspect='auto')
# plt.title('Observables (avec traces manquantes mises à zero)', fontsize = labelsize)
# av.set_ylabel("Time (s)", fontsize = labelsize)
# av.set_xlabel("Position x (m)", fontsize = labelsize)
# av.tick_params(axis='both', which='major', labelsize=labelsize)
# plt.clim([-vmax,vmax])
# plt.set_cmap('bwr')

# fig = plt.figure()
# av = plt.subplot(111)
# plt.imshow(panel_dense,extent=[ax[0],ax[-1],at[-1],at[0]],aspect='auto')
# plt.title('Observables (seulement pour comparaison)', fontsize = labelsize)
# av.set_ylabel("Time (s)", fontsize = labelsize)
# av.set_xlabel("Position x (m)", fontsize = labelsize)
# av.tick_params(axis='both', which='major', labelsize=labelsize)
# plt.clim([-vmax,vmax])
# plt.set_cmap('bwr')

# calcul de la transformée de fourier
img_c1 = np.fft.fft2(gpanel)


# définition des axes
nf, nk = gpanel.shape

# axe vertical -- fréquence temporelle
# la fréquence d'échantillonnage est de 1/dt, d'après le théorème de Shannon, les fréquences peuvent aller jusque fe/2
af = np.linspace(0, 1/(2*dt), nf)

# axe horizontal -- nombre d'onde (fréquence spatiale)
ak = np.linspace(0, 1/(2*dx), nk)

# affichage de la transformé de fourier

fig = plt.figure()
av = plt.subplot(111)

plt.imshow(20*np.log(np.abs(img_c1)),extent = [ak[0], ak[-1], af[-1], af[0]], aspect = 'auto')
plt.title("Spectre d'amplitude", fontsize = 1.5*labelsize)

av.set_ylabel("Fréquence temporelle (Hz)", fontsize = labelsize)
av.set_xlabel("Nombre d'onde (1/m)", fontsize = labelsize)

cbar = plt.colorbar()
cbar.set_label("Amplitude (dB)")

# zoom

fig = plt.figure()
av = plt.subplot(111)

plt.imshow(20*np.log(np.abs(img_c1[:30][:])))


plt.show()
