import numpy as np, matplotlib.pyplot as plt
t = np.array([[0.8, 0.6, 1.4], [0.3, 1.0, 1.3], [-0.3, 1.0, 0.6], [-0.8, 0.6, -0.2], [-1.0, 0.0, -1.0], [-0.8, -0.6, -1.4], [-0.3, -1.0, -1.3], [0.3, -1.0, -0.6], [0.8, -0.6, 0.2], [1.0, 0.0, 1.0]])
(I,J) = (len(t), len(t[0]))
ab = []
cl = [[[i] for i in range(1,I+1)]]
p = [1]*I
g = [t[i] for i in range(I)]
d = [[1/2 * sum((t[i]-t[j])[k]**2 for k in range(J)) for j in range(i)] for i in range(1,I)]
nc = [[i for i in range(1,I+1)]]
for k in range(1,I):
    md = [min(d[i]) for i in range(I-k)]
    m = min(md)
    b = md.index(m)
    a = d[b].index(m)
    b = b+1
    ab += [(a,b)]
    cl += [cl[k-1][:a] + cl[k-1][a+1:b] + cl[k-1][b+1:] + [cl[k-1][a] + cl[k-1][b]]]
    p = p[:a] + p[a+1:b] + p[b+1:] + [len(cl[k][-1])]
    g = g[:a] + g[a+1:b] + g[b+1:] + [1/p[-1] * (len(cl[k-1][a])*g[a] + len(cl[k-1][b])*g[b])]
    if a==0:
        d = d[:b-1] + d[b:]
        d = [d[i][1:b] + d[i][b+1:] for i in range(1,I-k-1)]
    else:
        d = d[:a-1] + d[a:b-1] + d[b:]
        d = [d[i][:a] + d[i][a+1:b] + d[i][b+1:] for i in range(I-k-2)]
    d += [[p[-1]*p[i]/(p[-1]+p[i]) * sum((g[-1]-g[i])[j]**2 for j in range(J)) for i in range(I-k-1)]]
    nc += [nc[k-1][:a] + nc[k-1][a+1:b] + nc[k-1][b+1:] + [I+k]]
x = [0]*I
y = [i for i in range(1,I+1)]
plt.scatter(x,y,c='b',lw=2)
for k in range(1,I):
    (a,b) = ab[k-1]
    if x[a] == 0:
        y[a] = cl[-1][0].index(y[a])+1
    if x[b] == 0:
        y[b] = cl[-1][0].index(y[b])+1
    plt.plot([x[a],k],[y[a],y[a]],'b',lw=1)
    plt.text(x[a],y[a],str(nc[k-1][a]))
    plt.plot([x[b],k],[y[b],y[b]],'b',lw=1)
    plt.text(x[b],y[b],str(nc[k-1][b]))
    plt.plot([k,k],[y[b],y[a]],'b',lw=1)
    x = x[:a] + x[a+1:b] + x[b+1:] + [k]
    y = y[:a] + y[a+1:b] + y[b+1:] + [(y[a]+y[b])/2]
plt.show()