import dolfin
import mshr

def create_mesh(inner_radius, outer_radius, res=20):
    C1 = mshr.Circle(dolfin.Point(0, 0), outer_radius)
    C0 = mshr.Circle(dolfin.Point(0,0),inner_radius)
    domain = C1-C0
    mesh = mshr.generate_mesh(domain,res)
    return mesh