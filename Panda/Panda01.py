import pinocchio as pin
from os.path import dirname, join, abspath

from pinocchio.visualize import RVizVisualizer

# Load the URDF model.
pinocchio_model_dir = '/home/unknown/Documents/PostDoc/Pinocchio_examples/Panda' 
mesh_dir = pinocchio_model_dir + '/Panda_description/meshes/'
urdf_model_path =pinocchio_model_dir + '/Panda_description/urdf/panda.urdf'
model, collision_model, visual_model = pin.buildModelsFromUrdf(urdf_model_path, mesh_dir)
viz = RVizVisualizer(model, collision_model, visual_model)

# Initialize the viewer.
viz.initViewer()
viz.loadViewerModel("pinocchio")

# Display a robot configuration.
q0 = pin.neutral(model)
viz.display(q0)


q = q0.copy()
q[1] = 1.0

input("Press enter to exit...")

viz.clean()