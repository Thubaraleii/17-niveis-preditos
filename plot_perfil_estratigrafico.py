
import matplotlib.pyplot as plt

# Subníveis e suas espessuras (em cm)
subniveis = [
    "1A", "1B", "1C", "1D",
    "2A", "2B",
    "3A",
    "4A", "4B",
    "5A", "5B", "5C",
    "6A", "6B",
    "7A", "7B", "7C", "7D", "7E"
]
espessuras = [
    2.5, 1.5, 1.5, 1.5,
    6.5, 6.5,
    6.5,
    5.5, 3.5,
    8, 8, 7.5,
    6.5, 4.5,
    4.5, 3, 5.5, 5.5, 3.5
]

# Configuração do gráfico com 1A na base e 7E no topo
fig, ax = plt.subplots(figsize=(6, 10))

bottom = 0
for subnivel, espessura in zip(subniveis, espessuras):
    ax.bar(x=0, height=espessura, bottom=bottom, width=0.6, label=subnivel)
    bottom += espessura

# Texto indicando a espessura total no topo do gráfico
ax.text(0, bottom + 1, f"Total: {bottom} cm", ha='center', fontsize=12, weight='bold')

# Ajustes visuais
ax.set_xticks([])
ax.set_ylabel('Espessura acumulada (cm)')
ax.set_title('Perfil estratigráfico com 1A na base e 7E no topo')
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.show()
