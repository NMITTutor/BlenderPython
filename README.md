# BlenderPython
Code for sharing - fixes for https://www.linkedin.com/learning/blender-python-scripting

Kia Ora Hello Patrick

We've been using this tutorial in our Compuer Graphics Imagery class. There are some changes when we use Blender 2.92 (and possibly earlier versions e.g. 2.8.x). 
For examples:

1. In the Interactive Python window, TAB is now used for autocompletion. For example "Importing and exploring bpy" 0.45 the autocomplete shortcut is TAB at Blender 2.92.

2. Chapter 1 , 01_06 "add_smooth_monkey_script.py" should be:

import bpy

bpy.ops.mesh.primitive_monkey_add(size=12, align='WORLD', enter_editmode=False,

location=(0, 0, 0))

bpy.ops.object.shade_smooth()

bpy.ops.object.modifier_add(type='SUBSURF')

bpy.context.object.modifiers["Subdivision"].levels = 3

This has consequences in "Chapter 4. Build Your Own Add-On" .

See a version in this repo.

3. Also  when adding a to a panel key word arguments are used for example , 
def draw(self, context):
      self.layout.label("Hi Panel")
      
Should  be,

def draw(self,context):     
         self.layout,.label( text="Hi Panel")
        
        
The Add Smooth Monkey add on needs Class property registration annotations for smoothness, size and name, like this:

smoothness : bpy.props.IntProperty(

          name="Smoothness",

          default=2,

          description="Subsurf level"

)

size : bpy.props.FloatProperty(

       name = "Size",

       default=1,

       description="Size of added monkey"

)

name : bpy.props.StringProperty(

name = "Name",

default = "Monkey",

description = "Added object name"

)



See an adjusted version - in this repo NOT tested but should work.
