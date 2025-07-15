import matplotlib.pyplot as plt

# Example: Let's say you evaluated FID and NIQE after every 10k images
image_indices = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Simulated scores (you can adjust slightly)
fid_scores = [45, 39, 34, 30, 27, 24, 22, 20, 19, 18.5, 18.4]
niqe_scores = [6.5, 6.0, 5.4, 5.0, 4.7, 4.4, 4.2, 4.1, 4.0, 3.95, 3.9]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(image_indices, fid_scores, marker='o', label='FID', color='blue')
plt.plot(image_indices, niqe_scores, marker='s', label='NIQE', color='green')

plt.title('FID and NIQE Scores over Training (100K Images)', fontsize=16)
plt.xlabel('Number of Images Trained', fontsize=14)
plt.ylabel('Score', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("fid_niqe_line_graph.png")
plt.show()
