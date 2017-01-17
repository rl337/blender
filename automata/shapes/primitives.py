import bpy

class Primitive(object):

    def __init__(self, name):
        self.name = name

        self.mesh = self.create_mesh()
        self.obj = self.create_object(self.mesh)
    
    def create_mesh(self):
        return bpy.data.meshes.new("%sMesh" % self.name)
    
    def create_object(self, mesh):
        return bpy.data.objects.new(self.name, mesh)

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
