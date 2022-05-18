
from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# Define the problem as a Python dictionary and convert it to a BQM
Q = {('B','B'): 1,
    ('K','K'): 1,
    ('A','C'): 2,
    ('A','K'): -2,
    ('B','C'): -2}

bqm = BinaryQuadraticModel.from_qubo(Q)

# Convert the bqm to an Ising model
ising_model = bqm.to_ising()

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(
                h = ising_model[0],
                J = ising_model[1],
                num_reads = 10,
                label='Example - Simple Ocean Programs: Conversion')

print(sampleset)