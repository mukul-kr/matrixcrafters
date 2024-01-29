import numpy as np

# Load data from id.txt and pin.txt
with open('id.txt', 'r') as id_file:
    id_data = id_file.read().splitlines()

with open('pin.txt', 'r') as pin_file:
    pin_data = pin_file.read().splitlines()

# Initialize a sparse matrix with zeros
sparse_matrix = np.zeros((len(pin_data), len(id_data)), dtype=int) # 33333

# Populate the matrix with 1/3 of each key's entries as 1
for i, pin in enumerate(pin_data):
    entries_to_fill = len(id_data) // 3
    random_indices = np.random.choice(len(id_data), entries_to_fill, replace=False)
    sparse_matrix[i, random_indices] = 1

# Print the sparse matrix
print(sparse_matrix)

# Save the sparse matrix to a text file
np.savetxt('sparse_matrix.txt', sparse_matrix, fmt='%d')

print("Sparse matrix saved to sparse_matrix.txt")
