import bpy

if bpy.context.active_object.type == 'MESH':
    # The active object is a mesh, so you can proceed with the rest of the script

    # Get the active object
    obj = bpy.context.active_object

    # Get the mesh data
    mesh = obj.data

    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Deselect all faces
    bpy.ops.mesh.select_all(action='DESELECT')

    # Enter object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Create an empty list to store the selected faces
    selected_faces = []

    # Loop through all the faces in the mesh
    for face in mesh.polygons:
        # Assume that all the vertices of the face are on the plus X axis
        all_vertices_on_plus_x = True
        # Loop through all the vertices in the face
        for vertex in face.vertices:
            # Get the position of the vertex
            vertex_pos = mesh.vertices[vertex].co
            # Check if the vertex is not on the plus X axis | If you want to invert this, change the '<' for a '>'
            if vertex_pos.x <= 0:
                # If the vertex is not on the plus X axis, set the flag to False
                all_vertices_on_plus_x = False
                # Break out of the loop, as we only need to find one vertex that is not on the plus X axis
                break
        # If all the vertices of the face are on the plus X axis, add the face to the list of selected faces
        if all_vertices_on_plus_x:
            selected_faces.append(face)

    # Select the faces in the list
    for face in selected_faces:
        face.select = True

    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')
else:
    # The active object is not a mesh, so you can print an error message or do something else
    print("Error: The active object is not a mesh")
