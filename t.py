import torch
from memory_transformer_xl import MemoryTransformerXL

model = MemoryTransformerXL(
    num_tokens = 1000,
    dim = 128,
    heads = 8,
    depth = 5,
    seq_len = 512,
    mem_len = 256,            # short term memory (the memory from transformer-xl)
    lmem_len = 256,           # long term memory (memory attention network attending to short term memory and hidden activations)
    mem_write_iters = 2,      # number of iterations of attention for writing to memory
    memory_layers = [3,4,5],  # which layers to use memory, only the later layers are actually needed
    num_mem_kv = 128,         # number of memory key/values, from All-attention paper

).cuda()

x1 = torch.randint(0, 1000, (1, 512)).cuda()
logits1, mem1 = model(x1)

x2 = torch.randint(0, 1000, (1, 512)).cuda()
logits2, mem2 = model(x2, memories = mem1)

print(logits2)