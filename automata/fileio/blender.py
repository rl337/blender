import bpy

import os
import logging

logger = logging.getLogger('fileio.blender')

class OutputRedirectedFile(object):

    def __init__(self, filename):
        self.filename = filename

    def protected_execute(self, func):

        old = None
        try:
            old = os.dup(1)
            os.close(1)
            os.open("/dev/null", os.O_WRONLY)

            if self.fnc is not None:
                self.fnc(self.filename)
        except:
            pass

        finally:
            if old is not None:
                os.close(1)
                os.dup(old) # should dup to 1
                os.close(old)


class MainFile(OutputRedirectedFile):
    def __init__(self, filename):
        super(MainFile, self).__init__(filename)

    def _save(self):
        bpy.ops.wm.save_as_mainfile(filepath=self.filename)

    def save(self):
        self.protected_execute(self._save)


class RenderFile(OutputRedirectedFile):
    def __init__(self, filename, width, height):
        super(RenderFile, self).__init__(filename)
        self.width = width
        self.height = height

    def _render(self):

        bpy.context.scene.render.filepath = self.filename
        bpy.context.scene.render.resolution_x = self.width
        bpy.context.scene.render.resolution_y = self.height
        bpy.ops.render.render( write_still=True )

    def render(self):
        self.protected_execute(self._render)

