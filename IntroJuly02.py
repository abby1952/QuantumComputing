import networkx as nx
from collections import defaultdict
from dwave.system.samplers import DwaveSampler
from dwave.system.composites import EmbeddingComposite


G=nx.Graph()

G.add_edges_from([(0,4),(0,5),(1,2),(1,6),(2,4),(3,7),(5,6),(6,7)])

Q=defaultdict(int)

# Constraint

for i in range(8):
	Q[(i,1)] += -7
	for j in range(i+1,8):
		Q[(i,j)] +=2

# Objective

for i,j in G.edges:
	Q[(i,i)] +=1
	Q[(j,j)] +=1
	Q[(i,j)] +=-2

sampler=EmbeddingComposite(DWaveSampler(solver='DW_2000Q_6'))

sampleset = sampler.sample_qubo(Q, num_reads=10)

print(sampleset)
	