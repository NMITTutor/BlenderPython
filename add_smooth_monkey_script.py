import bpy

bpy.ops.mesh.primitive_monkey_add(size=12, align='WORLD', enter_editmode=False,
location=(0, 0, 0))
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 3