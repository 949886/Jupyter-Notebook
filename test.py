import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

# Define the object's coordinates in view space
x_view = np.array([1, 2, 3])
y_view = np.array([4, 5, 6])
z_view = np.array([7, 8, 9])

# Define the camera's position and orientation in view space
camera_pos = np.array([0, 0, 10])
camera_lookat = np.array([0, 0, 0])
camera_up = np.array([0, 1, 0])

# Define the projection matrix
near_clip = 5
far_clip = 15
aspect_ratio = 1
fov = np.pi / 4
proj_mat = np.array([
    [1 / (aspect_ratio * np.tan(fov / 2)), 0, 0, 0],
    [0, 1 / np.tan(fov / 2), 0, 0],
    [0, 0, -(far_clip + near_clip) / (far_clip - near_clip), -2 * far_clip * near_clip / (far_clip - near_clip)],
    [0, 0, -1, 0]
])

# Convert the object's coordinates from view space to clip space
object_view = np.vstack((x_view, y_view, z_view, np.ones(3)))
object_clip = proj_mat @ object_view
x_clip, y_clip, z_clip, _ = object_clip

# Set up the figure and axis
fig = plt.figure()
ax = p3.Axes3D(fig)

# Define the animation function
def animate(i):
    # Clear the axis
    ax.clear()

    # Define the camera's position and orientation in view space
    camera_pos = np.array([0, 0, 10])
    camera_lookat = np.array([0, 0, 0])
    camera_up = np.array([0, 1, 0])

    # Define the projection matrix
    near_clip = 5
    far_clip = 15
    aspect_ratio = 1
    fov = np.pi / 4
    proj_mat = np.array([
        [1 / (aspect_ratio * np.tan(fov / 2)), 0, 0, 0],
        [0, 1 / np.tan(fov / 2), 0, 0],
        [0, 0, -(far_clip + near_clip) / (far_clip - near_clip), -2 * far_clip * near_clip / (far_clip - near_clip)],
        [0, 0, -1, 0]
    ])

    # Convert the object's coordinates from view space to clip space
    object_view = np.vstack((x_view, y_view, z_view, np.ones(3)))
    object_clip = proj_mat @ object_view
    x_clip, y_clip, z_clip, _ = object_clip

    # Plot the object's coordinates in clip space
    ax.plot(x_clip, y_clip, z_clip, 'bo')

    # Set the axis limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    # Set the axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Rotate the view
    ax.view_init(elev=10, azim=i)

    # Return the axis
    return ax

ani = animation.FuncAnimation(fig, animate, frames=360, interval=50)
plt.show()