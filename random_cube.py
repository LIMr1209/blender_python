import bpy
from random import random
from mathutils import Vector

maxIterations = 1000  # Max iterations to prevent while loop from running forever

# min and max values for each axis for the random numbers
ranges = {
    'x': {'min': -10, 'max': 10},
    'y': {'min': -10, 'max': 10},
    'z': {'min': -10, 'max': 10}
}

# Generates a random number within the axis minmax range
randLocInRange = lambda axis: ranges[axis]['min'] + random() * (ranges[axis]['max'] - ranges[axis]['min'])

size = 250  # Number of cubes
cubes = []  # Cube coordinates list

loopIterations = 0
while len(cubes) < size and loopIterations < maxIterations:
    loopIterations += 1
    loc = Vector([randLocInRange(axis) for axis in ranges.keys()])  # Generate a random 3D coordinate
    if len(cubes) > 0:
        overlappingPoints = [p for p in cubes if (
                p - loc).length < 2]  # Search for overlapping points (within the cube radius radius)
        if overlappingPoints: continue  # if any found, skip this location
    cubes.append(loc)  # Add coordinate to cube list

# Add the first cube (others will be duplicated from it)
bpy.ops.mesh.primitive_cube_add(location=cubes[0])
cube = bpy.context.scene.objects['Cube']

# Add all other cubes
for c in cubes[1:]:
    dupliCube = cube.copy()
    dupliCube.location = c
    bpy.context.collection.objects.link(dupliCube)

import random
import bpy

obj_ctr = []
# one object must be created outside the loop for data structure to be available for testing
x = random.randint(-5, 4)
y = random.randint(-2, 7)
z = random.randint(3, 10)
obj_ctr.append((x, y, z))

# while len(obj_ctr) < 10:
for a in range(10):
    test_x = False
    test_y = False
    test_z = False
    x = random.randint(-5, 4)
    y = random.randint(-2, 7)
    z = random.randint(3, 10)
    for test in obj_ctr:  # verify the new randoms will not allow collision
        if abs(test[0] - x) < 1 * 2:
            test_x = False
        else:
            test_x = True
        if abs(test[1] - y) < 1 * 2:
            test_y = False
        else:
            test_y = True
        if abs(test[2] - y) < 1 * 2:
            test_z = False
        else:
            test_z = True
    if (test_x and test_y and test_z):
        obj_ctr.append((x, y, z))

for obj in obj_ctr:
    bpy.ops.mesh.primitive_cube_add(location=obj)
