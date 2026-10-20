import torch as tt

nn = tt.tensor([[1,1,1],[2,2,2],[3,3,3]])
#print(nn)

nn[0][0] = 5
#print(nn)

#print(tt.cuda.is_available())
#print(tt.rand(1).item())

print(nn.device) # cpu

gpu_tensor = nn.to('cuda')
#print(gpu_tensor)

longtensor = tt.tensor([[1,2,3,4],[2,1,4,5]])
print(longtensor)

longtensor = longtensor.to(dtype=tt.float32)
print(longtensor)

ran = tt.rand(2,4)
print(ran.log2()) # make new tensor to store new tensor
print(ran.log2_()) # inplace , don't make new tensor , it save memory
t1 = tt.rand(625)

vi1 = t1.view([1,25,25])
#print(vi1)
rsh = t1.reshape([1,25,25])
#print(rsh)


