
import matplotlib.pyplot as plt
import numpy as np

# ============================ DADOS DE OPAL E MOA ============================
subniveis = [
    "1A", "1B", "1C", "1D",
    "2A", "2B",
    "3A",
    "4A", "4B",
    "5A", "5B", "5C",
    "6A", "6B",
    "7A", "7B", "7C", "7D", "7E"
]

opal = [
    None, 1, 1, 1,
    0, 0,
    0,
    1, 2,
    3, 3, 4,
    5, 3,
    3, 7, 5, 10, 4
]

moa = [
    None, 72, 71, 72,
    71, 70,
    84,
    89, 75,
    62, 68, 78,
    64, 64,
    70, 54, 63, 27, 29
]

opal[0] = round(np.mean([opal[1], opal[2], opal[3]]), 1)
moa[0] = round(np.mean([moa[1], moa[2], moa[3]]), 1)

subniveis = subniveis[::-1]
opal = opal[::-1]
moa = moa[::-1]

fig, ax = plt.subplots(figsize=(6, 10))
ax.plot(opal, subniveis, marker='o', label='OPAL', color='gold')
ax.plot(moa, subniveis, marker='s', label='MOA', color='orangered')
ax.invert_yaxis()
ax.set_xlabel('Valor (%)')
ax.set_ylabel('Subníveis (base → topo)')
ax.set_title('Distribuição vertical de OPAL e MOA (1A na base)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

# ============================ DADOS GEOQUÍMICOS ============================
subniveis_geo = [
    "7E", "7D", "7C", "7B", "7A",
    "6B", "6A",
    "5C", "5B", "5A",
    "4B",
    "3A",
    "2B", "2A",
    "1D", "1C", "1B", "1A"
]

toc = [
    None, None, None, None, None,
    None, 11.93,
    12.11, 11.7, 12.01,
    13.05,
    8.79,
    7.69, 5.73,
    7.42, 12.41, 12.97, None
]

tn = [
    None, None, None, None, None,
    None, 0.43,
    0.46, 0.44, 0.43,
    0.54,
    0.32,
    0.29, 0.18,
    0.26, 0.52, 0.54, None
]

fe2o3 = [
    None, None, None, None, None,
    None, 7.06,
    6.66, 6.41, 5.23,
    7.41,
    5.99,
    5.89, 5.78,
    5.25, 5.52, 4.94, None
]

u_th = [
    None, None, None, None, None,
    None, 2.06,
    1.98, 1.82, 1.81,
    1.66,
    1.35,
    1.28, 1.11,
    1.17, 1.51, 1.48, None
]

# Estimativas simples para 1A
toc[-1] = round(np.mean([toc[-2], toc[-3], toc[-4]]), 2)
tn[-1] = round(np.mean([tn[-2], tn[-3], tn[-4]]), 2)
fe2o3[-1] = round(np.mean([fe2o3[-2], fe2o3[-3], fe2o3[-4]]), 2)
u_th[-1] = round(np.mean([u_th[-2], u_th[-3], u_th[-4]]), 2)

subniveis_geo = subniveis_geo[::-1]
toc = toc[::-1]
tn = tn[::-1]
fe2o3 = fe2o3[::-1]
u_th = u_th[::-1]

fig, axs = plt.subplots(1, 4, figsize=(14, 10), sharey=True)
axs[0].plot(toc, subniveis_geo, marker='o', color='brown')
axs[0].set_xlabel('TOC (%)')
axs[1].plot(tn, subniveis_geo, marker='s', color='olive')
axs[1].set_xlabel('TN (%)')
axs[2].plot(fe2o3, subniveis_geo, marker='^', color='darkred')
axs[2].set_xlabel('Fe2O3 (%)')
axs[3].plot(u_th, subniveis_geo, marker='d', color='purple')
axs[3].set_xlabel('U/Th')

for ax in axs:
    ax.invert_yaxis()
    ax.grid(True)

fig.suptitle('Distribuição vertical dos parâmetros geoquímicos (1A na base)', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
