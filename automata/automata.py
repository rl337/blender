
import bpy

import os
import sys
import logging

import fileio.blender
import shapes.primitives

def extract_script_args(sysargs):
    blender_args_end = None
    try:
        blender_args_end = sys.argv.index('--')
        return sysargs[blender_args_end+1:]
    except ValueError as e:
        return []

args = extract_script_args(sys.argv)
sys.stdout.write("%s" % args)

filename = args.pop()
if not filename.endswith('.blend'):
    filename = "%s.blend" % filename

mainfile = fileio.blender.MainFile(filename)
renderfile = fileio.blender.RenderFile('a.jpg', 1024, 768)

if 'Cube' in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]

    bpy.data.meshes.remove(mesh, do_unlink=True)

tetrahedron = shapes.primitives.Tetrahedron("tetrahedron0001")

mainfile.save()
renderfile.render()
