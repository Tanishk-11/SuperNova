import numpy as np
def dfs(adj,n,traversal,vis,node):
    vis[node]=1
    traversal.append(node+1)
    for i in adj[node]:
        if(vis[i]==0):
            dfs(adj,n,traversal,vis,i)


def main():
    n=int(input("Enter the number of nodes:"))
    m=int(input("Enter the number of edges which are connected:"))
    adj_ls=[[] for _ in range(n)]
    for i in range(m):
        n1=int(input("Enter the first node :  "))
        n2=int(input("Enter the second node :  "))
        adj_ls[n1].append(n2)
    
    # print(adj_ls)
    traversal=[]
    vis=np.zeros(n,dtype='int')
    for i in range(n):
        dfs(adj_ls,n,traversal,vis,i)
        print(traversal)
        for i in range(n):
           vis[i]=0
        traversal.clear()
main()