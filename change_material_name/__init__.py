import bpy

bl_info = {
    "name" : "ChangeMaterialName",
    "author" : "ndg",
    "description" : "change material's name to (object's name)->(material's name)",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Edit > Change Material Name",
    "warning" : "",
    "category" : "Generic"
}

def main():
    objects = list(bpy.data.objects)

    for ob in objects:
        try:
            #select one
            bpy.context.view_layer.objects.active = ob

            name = ob.name + '->'
            size = len(bpy.context.object.material_slots.keys())

            if size != 0:
                for i in range(size):
                    #set active_material
                    bpy.context.object.active_material_index = i
     
                    #make material name
                    m_name = bpy.context.object.active_material.name
                    if '->' not in m_name:
                        m_name = name + m_name
        
                    else:
                        m_name = m_name.split('->')[-1]
                        m_name = name + m_name

                    #set new material name
                    bpy.context.object.active_material.name = m_name

        except:
            continue


class ChangeMaterialName(bpy.types.Operator):
    bl_idname = 'object.change_material_name'
    bl_label = 'Change Material Name'

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        main()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator('object.change_material_name')

def register():
    bpy.utils.register_class(ChangeMaterialName)
    bpy.types.TOPBAR_MT_edit.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ChangeMaterialName)
    bpy.types.TOPBAR_MT_edit.remove(menu_func)

if __name__ == '__main__':
    register()
