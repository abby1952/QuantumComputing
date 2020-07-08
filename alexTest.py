from dwave.system import EmbeddingComposite, DWaveSampler


Q = {('a', 'a'): 1, ('b', 'b'): 1, ('c', 'c'): -1, ('a', 'b'): -2, ('a', 'c'): 2, ('b', 'c'): -2}

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=10)

print(sampleset)
