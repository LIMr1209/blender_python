import bpy

appropriate_dimensions = 2

obj = bpy.data.objects['product2trans']

k1 = obj.dimensions.x
k2 = obj.dimensions.y
k3 = obj.dimensions.z
dimList = [k1, k2, k3]
k = min(dimList)

obj.scale *= appropriate_dimensions / k
