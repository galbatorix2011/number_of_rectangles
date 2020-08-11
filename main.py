import math
class Solution:
    def __init__(self, points):
        self.points = points
        self.result = []
        self.vectors = {}

    def aux(self, p1, p2):
        final_p = p1 if (p1[0] >= p2[0]) and (p1[1] >= p2[1]) else p2
        incial_p = p1 if final_p == p2 else p2
        return [incial_p, final_p]
    
    def get_vector_size(self, p1,p2):
        return math.sqrt(math.pow(p2[0]-p1[0],2) + math.pow(p2[1]-p1[1],2))

    def declive_checker(self,p1,p2):
        return (p1[0] != p2[0]) and ( ((p1[1] - p2[1]) / (p1[0] - p2[0])) >= 0)

    def define_vectors(self):
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                if self.declive_checker(self.points[i], self.points[j]):
                    vector_defined = self.aux(self.points[i], self.points[j])
                    size = self.get_vector_size(vector_defined[0], vector_defined[1])
                    if size not in self.vectors:
                        self.vectors[size] = [vector_defined]
                    else:
                        self.vectors[size].append(vector_defined)

                                   
    def create_vectors(self,incial_p, final_p):
        return [final_p[0] - incial_p[0], final_p[1] - incial_p[1]]


    def are_perpendiculares(self,v1,v2):
        return ((v1[0] * v2[0]) + (v1[1] * v2[1])) == 0
        

    def check_vectors(self):
        for keys in self.vectors:
            lista = self.vectors[keys]
            for i in range(len(lista)):
                for j in range(i+1,len(lista)):
                    Ab = self.create_vectors(lista[i][0],lista[i][1])
                    Be = self.create_vectors(lista[i][1],lista[j][1])
                    Ad = self.create_vectors(lista[i][0],lista[j][0])
                    if self.are_perpendiculares(Ab,Be) and self.are_perpendiculares(Ab,Ad):
                        self.result.append( [lista[i][0],lista[i][1],lista[j][0],lista[j][1]] )
                    
                    
                    

if __name__ == "__main__":
    points = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(0,-1),(1,-1),(2,-1)]
    x = Solution(points)
    x.define_vectors()
    x.check_vectors()
    print(len(x.result))
    for oi in x.result:
        print(oi)
        print("\n")

#A    B    C     [A, B] + [D, E]

#D    E    F      (AB * BE) == 0 and (AB * AD) == 0

#G    H    I


 #   A, B, C, D, E

#    AB, AC, AD, AE#
    