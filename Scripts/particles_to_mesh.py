import bpy
from bpy.props import *

## OPERATORS
class ConvertParticleSystemModifierToMesh(bpy.types.Operator):
    """Convert particle system modifier to mesh"""
    bl_idname = "object.convert_particle_system_modifier_to_mesh"
    bl_label = "Convert Particle System Modifier to Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the active object
        obj = context.object
        
        if obj.modifiers.get("ParticleSystem"):
            # Convert the particle system modifier to a mesh
            # Check if the active object has a particle system modifier
            # Convert the particle system modifier to a mesh
    
            bpy.ops.object.modifier_convert(modifier="ParticleSystem")

            # Remove the particle system modifier
            obj.modifiers.remove(obj.modifiers.get("ParticleSystem"))

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Active object does not have a particle system modifier")
            return {'CANCELLED'}
        
class ConvertParticleSystemModifierToCurve(bpy.types.Operator):
    """Convert particle system modifier to mesh"""
    bl_idname = "object.convert_particle_system_modifier_to_curve"
    bl_label = "Convert Particle System Modifier to Curve"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        # Get the active object
        obj = context.object
    

        if obj.modifiers.get("ParticleSystem"):
            # Convert the particle system modifier to a mesh
            # Check if the active object has a particle system modifier
            # Convert the particle system modifier to a mesh
    
            bpy.ops.object.modifier_convert(modifier="ParticleSystem")
            bpy.ops.object.convert(target='CURVE')
            bpy.context.object.data.extrude = obj.hair_mesh_width
            bpy.ops.object.convert(target='MESH')

            # Remove the particle system modifier
            obj.modifiers.remove(obj.modifiers.get("ParticleSystem"))

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Active object does not have a particle system modifier")
            return {'CANCELLED'}
        
## UI

class Panel(bpy.types.Panel):
    bl_label = 'Panel'
    bl_idname = 'PT_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type= 'UI'
    bl_category = 'Add-On'


    def draw(self, context):
        
        obj = context.object
        layout = self.layout
        layout.use_property_split = True

       
        row = layout.row()
        row.label(text= "Convert partic to Mesh", icon= 'OBJECT_ORIGIN')
        row = layout.row()
        row.operator("object.convert_particle_system_modifier_to_mesh", text="Convert to Mesh")
        row = layout.row()
        row.operator("object.convert_particle_system_modifier_to_curve", text="Convert to Curve")
        row = layout.row()
        row.prop(obj, "hair_mesh_width")
        

#register       
       
def register():
    bpy.utils.register_class(ConvertParticleSystemModifierToMesh)
    bpy.utils.register_class(ConvertParticleSystemModifierToCurve)
    bpy.utils.register_class(Panel)
    bpy.types.Object.hair_mesh_width = bpy.props.FloatProperty(
                            name="Hair Mesh Width",
                            description="Scale",
                            default=0.01
                            )
   
def unregister():
    bpy.utils.unregister_class(ConvertParticleSystemModifierToMesh)
    bpy.utils.unregister_class(ConvertParticleSystemModifierToCurve)
    bpy.utils.unregister_class(Panel)
    del bpy.types.Object.number_of_pages

if __name__ == "__main__":
    register()
    