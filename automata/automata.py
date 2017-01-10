
import bpy

import os
import sys
import logging


def extract_script_args(sysargs):
    blender_args_end = None
    try:
        blender_args_end = sys.argv.index('--')
        return sysargs[blender_args_end+1:]
    except ValueError as e:
        return []

def render(width, height, filename):
    old = os.dup(1)
    os.close(1)
    os.open("/dev/null", os.O_WRONLY) 

    bpy.context.scene.render.filepath = filename
    bpy.context.scene.render.resolution_x = width
    bpy.context.scene.render.resolution_y = height
    bpy.ops.render.render( write_still=True ) 

    os.close(1)
    os.dup(old) # should dup to 1
    os.close(old)

def save(filename):
    old = os.dup(1)
    os.close(1)
    os.open("/dev/null", os.O_WRONLY) 

    bpy.ops.wm.save_as_mainfile(filepath=filename)

    os.close(1)
    os.dup(old) # should dup to 1
    os.close(old)


def createMeshFromPrimitive(name, origin):
    bpy.ops.mesh.primitive_cone_add(
        vertices=64, 
        radius1=1.0, 
        radius2=0.0, 
        depth=1, 
        end_fill_type='NGON', 
        view_align=False, 
        enter_editmode=False, 
        location=origin, 
        rotation=(0, 0, 0))

    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.mode_set(mode = 'EDIT') 

    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'DESELECT')

    ob = bpy.context.object
    ob.name = name
    ob.show_name = True
    
    mesh = ob.data
    mesh.name = name+'Mesh'

    bpy.ops.object.mode_set(mode = 'OBJECT')
    count = 0
    for vert in mesh.vertices:  
        if vert.co[2] < 0:
            vert.select = True
        count += 1

    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.extrude_vertices_move(
        MESH_OT_extrude_verts_indiv={"mirror":False},
        TRANSFORM_OT_translate={
            "value": [0, 0, -5],
        }
    )

    return ob


args = extract_script_args(sys.argv)
sys.stdout.write("%s" % args)

filename = args.pop()
if not filename.endswith('.blend'):
    filename = "%s.blend" % filename

if 'Cube' in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]

    bpy.data.meshes.remove(mesh, do_unlink=True)

createMeshFromPrimitive("cone001", (0, 0, 0))
save(filename)

render(1024, 768, 'a.jpg')

