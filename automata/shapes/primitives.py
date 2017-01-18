import bpy
import math

class Primitive(object):

    def __init__(self, name, location=(0,0,0)):
        self.name = name
        self.location = location

        self.mesh = self.create_mesh()
        self.obj = self.create_object(self.mesh)
    
    def create_mesh(self):
        return bpy.data.meshes.new("%sMesh" % self.name)
    
    def create_object(self, mesh):
        obj = bpy.data.objects.new(self.name, mesh)
        obj.location = self.location
        obj.show_name = True

        scn = bpy.context.scene
        scn.objects.link(obj)
        scn.objects.active = obj
        obj.select = True

        return obj

class Tetrahedron(Primitive):

    def __init__(self, name, unit=1.0):
        self.unit = unit
        self.points = (
            (0.0, 0.0, -1.0),
            (0.0, 1.0, math.sin(60.0 * math.pi / 180.0)/2),
            (math.sin(60.0 * math.pi / 180.0), -math.cos(60.0 * math.pi / 180.0), math.sin(60.0 * math.pi / 180.0)/2),
            (-math.sin(60.0 * math.pi / 180.0), -math.cos(60.0 * math.pi / 180.0), math.sin(60.0 * math.pi / 180.0)/2),
        )

        self.faces = (
            (1, 2, 3),
            (0, 1, 2),
            (0, 2, 3),
            (0, 3, 1),
        )

        super(Tetrahedron, self).__init__(name)

    def create_mesh(self):
        mesh = bpy.data.meshes.new('%sMesh' % self.name)
        mesh.from_pydata(self.points, [], self.faces)
        mesh.update()  

        return mesh

class Cone(Primitive):

    def __init__(self, name, base_radius=1.0, depth=1.0, location=(0, 0, 0)):
        self.base_radius = base_radius
        self.depth = depth
        self.location = location
        super(Cone, self).__init__(name)

    def create_mesh(self):
        bpy.ops.mesh.primitive_cone_add(
            vertices=64,
            radius1=self.base_radius,
            radius2=0.0,
            depth=self.depth,
            end_fill_type='NGON',
            view_align=False,
            enter_editmode=False,
            location=self.location,
            rotation=(0, 0, 0))

        return bpy.context.object.data
