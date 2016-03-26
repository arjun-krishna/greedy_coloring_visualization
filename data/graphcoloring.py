import subprocess
import sys
import graphplot as gp

subprocess.call(["gnome-open", "graph.png"])
# ./exe V edlist_file_name

colors = ["red","blue","green","violet","indigo","yellow","orange","brown","pink","chartreuse"];
def find_color(v):
 for k in range(0,10):
  if v.xcol[k] == 1 :
   return k
 return -1
def graph_coloring(G):
 i=0
 while( i < G.nV):
  curr_node = G.degreeList[i][0]
  G.curr_node = curr_node;
  G.convert2dot()
  subprocess.call(["dot","-Tpng","graph.dot","-o","graph.png"])
  subprocess.call(["sleep","1"])
  col = find_color(G.vertexList[curr_node])
  if(col==-1):
   print 'insufficient colors'
   exit()
  G.update_color(curr_node,colors[col])
  for neighbours in G.adjList[curr_node]:
   (G.vertexList[neighbours]).xcol[col] = 0;
  G.curr_node=-1;
  G.convert2dot()
  subprocess.call(["dot","-Tpng","graph.dot","-o","graph.png"])
  subprocess.call(["sleep","1"])
  i=i+1
def read_edL():
 E = []
 edgL = open(sys.argv[2],'r')
 s = edgL.readline()
 while(s):
  L = s.split(' ')
  L[1] = L[1].split('\n')
  L[1] = L[1][0]
  E.append([int(L[0]),int(L[1])])
  s = edgL.readline()
 
 return E


# MAIN

V = sys.argv[1]
V = int(V)
E = read_edL()
G = gp.Graph(V,E)
graph_coloring(G)
