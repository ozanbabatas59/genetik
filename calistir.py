import matplotlib.pyplot as plt

def ters_tamamlayici(dna_dizisi):
    tamamlayici = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    ters_dizi = dna_dizisi[::-1]  # Reverse the string
    ters_tamamlayici_dizi = ''.join([tamamlayici[baz] for baz in ters_dizi])
    return ters_tamamlayici_dizi

# DNA sequence
dna_dizisi = "ATGCTAGCTAG"
ters_tamamlayici_dizi = ters_tamamlayici(dna_dizisi)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set axis limits and labels
ax.set_xlim(-1, len(dna_dizisi))  # Shifted to center the strands
ax.set_ylim(-2, 2)
ax.set_xticks(range(len(dna_dizisi)))
ax.set_yticks([])

# Labels for the strands
ax.text(0, 1.5, "Orijinal Dizi", fontsize=12, color='blue', ha='center')
ax.text(0, -1.5, "Ters Tamamlayıcı Dizi", fontsize=12, color='green', ha='center')

# Display original bases and complementary bases aligned correctly
for j in range(len(dna_dizisi)):
    ax.text(j, 1.1, dna_dizisi[j], fontsize=12, ha='center', color='blue')  # Original strand letters
    ax.text(j, -1.1, ters_tamamlayici_dizi[j], fontsize=12, ha='center', color='green')  # Complementary strand letters

    # Draw a line connecting complementary bases
    ax.plot([j, j], [1, -1], color='red', lw=2)

# Show the plot
plt.show()
