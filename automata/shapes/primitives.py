import bpy
import math

class Primitive(object):

    def __init__(self, name, location=(0,0,0)):
        self.name = name
        self.location = location

        self.mesh = self.create_mesh()
        self.obj = self.create_object(self.mesh)
    
    def create_object(self, mesh):
        obj = bpy.data.objects.new(self.name, mesh)
        obj.location = self.location
        obj.show_name = True

        scn = bpy.context.scene
        scn.objects.link(obj)
        scn.objects.active = obj
        obj.select = True

        return obj

    def create_mesh(self):
        mesh = bpy.data.meshes.new('%sMesh' % self.name)
        mesh.from_pydata(self.points, [], self.faces)
        mesh.update()  

        return mesh

class Tetrahedron(Primitive):

    def __init__(self, name, unit=1.0):
        self.unit = unit
        self.points = (
            (0.0, 0.0, 1.0),
            (0.0, 1.0, -math.sin(60.0 * math.pi / 180.0)/2),
            (math.sin(60.0 * math.pi / 180.0), -math.cos(60.0 * math.pi / 180.0), -math.sin(60.0 * math.pi / 180.0)/2),
            (-math.sin(60.0 * math.pi / 180.0), -math.cos(60.0 * math.pi / 180.0), -math.sin(60.0 * math.pi / 180.0)/2),
        )

        self.faces = (
            (1, 2, 3),
            (0, 1, 2),
            (0, 2, 3),
            (0, 3, 1),
        )

        super(Tetrahedron, self).__init__(name)

        top_group = self.obj.vertex_groups.new("top")
        top_group.add([0], 1.0, "ADD")

        base_group = self.obj.vertex_groups.new("base")
        base_group.add([1,2,3], 1.0, "ADD")


class Cube(Primitive):
    
    def __init__(self, name, unit=1.0):
        self.unit = unit
        self.points = (
            (-1.0, -1.0, -1.0),
            (-1.0,  1.0, -1.0),
            ( 1.0,  1.0, -1.0),
            ( 1.0, -1.0, -1.0),
            (-1.0, -1.0,  1.0),
            (-1.0,  1.0,  1.0),
            ( 1.0,  1.0,  1.0),
            ( 1.0, -1.0,  1.0),
        )

        self.faces = (
            (0, 1, 2, 3),
            (0, 1, 5, 4),
            (1, 2, 6, 5),
            (4, 5, 6, 7),
            (2, 3, 7, 6),
            (0, 3, 7, 4),
        )

        super(Cube, self).__init__(name)

        bottom_group = self.obj.vertex_groups.new("bottom")
        bottom_group.add([0, 1, 2, 3], 1.0, "ADD")

        top_group = self.obj.vertex_groups.new("top")
        top_group.add([4, 5, 6, 7], 1.0, "ADD")

        back_group = self.obj.vertex_groups.new("back")
        back_group.add([0, 1, 5, 4], 1.0, "ADD")

        front_group = self.obj.vertex_groups.new("front")
        front_group.add([2, 3, 7, 6], 1.0, "ADD")

        left_group = self.obj.vertex_groups.new("left")
        left_group.add([0, 3, 7, 4], 1.0, "ADD")

        right_group = self.obj.vertex_groups.new("right")
        right_group.add([1, 2, 6, 5], 1.0, "ADD")

class Cone(Primitive):

    def __init__(self, name, base_radius=1.0, height=1.0, location=(0, 0, 0), segments=16):
        self.base_radius = base_radius
        self.height = height
        self.location = location
        self.segments = segments

        degreestoradians = math.pi / 180.0
        baseradians = 360.0 / segments * degreestoradians
        pointlist = [
            (0.0, 0.0, height/2),
            (0.0, 0.0, -height/2),
        ] + [ 
            (math.sin(n * baseradians), math.cos(n * baseradians), -height/2)
            for n in range(segments)
        ]

        self.points = tuple(pointlist) 

        facelist = [
            (0, n, n+1) for n in range(2, segments+1)
        ] + [
            (1, n, n+1) for n in range(2, segments+1)
        ] + [
            (0, segments+1, 2),
            (1, segments+1, 2)
        ] 

        self.faces = tuple(facelist)

        super(Cone, self).__init__(name)

        top_group = self.obj.vertex_groups.new("top")
        top_group.add([0], 1.0, "ADD")

        base_group = self.obj.vertex_groups.new("base")
        base_group.add(range(1, len(self.points)+1), 1.0, "ADD")
