class node(object) :
 def __init__(self,value,color):
  self.value = value;
  self.color = color;
  self.xcol = []
  for i in range(0,10):
   self.xcol.append(1)

class Graph:
 def __init__(self,V,E): #V - no.of vertices
  self.nV = V
  self.nE = len(E)
  self.E = E
  self.vertexList = [];
  self.degreeList = [];
  self.adjList = [[]]
  self.curr_node=-1;
  i=0
  while i<V :
   a = node(i,'')
   self.vertexList.append(a);
   self.adjList.append([])
   self.degreeList.append([i,0])
   i=i+1
  for k in E:
   self.adjList[k[0]].append(k[1]);
   self.degreeList[k[0]][1] +=1
   self.degreeList[k[1]][1] +=1
   self.adjList[k[1]].append(k[0]);  
  self.degreeList.sort(cmp=self.compare_deg)
 
  
 def compare_deg(self,a,b):
  if(a[1]<b[1]):
   return 1
  return -1
 
 def convert2dot(self):
  dot = open('graph.dot','w')
  dot.write('graph {\n')
  i=self.nV
  while i>0:
   i=i-1
   if(self.vertexList[i].color==''):
    if(i==self.curr_node):
      # dot.write(str(i)+'[style=filled,shape=doublecircle,color=lawngreen];\n');
      dot.write(str(i)+'[style=filled,shape=doublecircle,color=gray];\n');
    else:
      dot.write(str(i)+'[shape=circle];\n');
   else:
    dot.write(str(i)+'[shape=circle,style=filled,color='+self.vertexList[i].color+'];\n');
  for k in self.E:
    if(self.curr_node==k[0] or self.curr_node==k[1]):
      dot.write(str(k[0])+' -- '+str(k[1])+'[penwidth=3.0,color=lawngreen];\n');
    else:
      dot.write(str(k[0])+' -- '+str(k[1])+'[penwidth=3.0];\n');
  dot.write('}\n');
  dot.close();

 def update_color(self,ver,color): # color should be string
  self.vertexList[ver].color = color

