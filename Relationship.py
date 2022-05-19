
from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# Define the problem as a Python dictionary and convert it to a BQM
Q = {('X','X'): 0,
    ('Y','Y'): 0,
    ('W','W'): 0,
    ('Z','Z'): 1,
    ('C','C'): 1,
    ('X','Y'): -1,
    ('X','W'): -1,
    ('Y','Z'): 1,
    ('Z','C'): -1,
    ('C','W'): 1}

bqm = BinaryQuadraticModel.from_qubo(Q)

# Convert the bqm to an Ising model
ising_model = bqm.to_ising()

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(
                h = ising_model[0],
                J = ising_model[1],
                num_reads = 20,
                label='Relationship')

print(sampleset)