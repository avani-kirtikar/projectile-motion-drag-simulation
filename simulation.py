import numpy as np
import matplotlib.pyplot as plt

# 1. Environment & Simulation Constraints
g = 9.81          # Acceleration due to gravity (m/s^2)
c = 0.2           # Drag coefficient (kg/m, depends on air density, shape, area)
m = 1.5           # Mass of the projectile (kg)
dt = 0.01         # Time step size for numerical integration (seconds)

# 2. Initial Conditions
x_initial = 0.0
y_initial = 0.0
v0 = 50.0         # Initial velocity magnitude (m/s)
angle = 45.0      # Launch angle in degrees

# Convert angle to radians for numpy functions
theta = np.radians(angle)

# Initialize tracking lists with starting positions and velocity vectors
x_track = [x_initial]
y_track = [y_initial]
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)

# 3. Core Simulation Loop (Runs iteratively while projectile is in the air)
while y_track[-1] >= 0:
    # Current positions
    x = x_track[-1]
    y = y_track[-1]
    
    # Calculate current speed
    v = np.sqrt(vx**2 + vy**2)
    
    # Calculate Drag Force components: F_drag = c * v^2
    # Direction is opposite to the velocity vector components
    f_drag_x = -c * v * vx
    f_drag_y = -c * v * vy
    
    # Calculate Net Accelerations: a = F_net / m
    ax = f_drag_x / m
    ay = -g + (f_drag_y / m)
    
    # Update Velocity components via Euler-Cromer Integration
    vx = vx + ax * dt
    vy = vy + ay * dt
    
    # Update Positions
    x_new = x + vx * dt
    y_new = y + vy * dt
    
    # Save values to lists for graphing
    x_track.append(x_new)
    y_track.append(y_new)

# 4. Data Visualization
plt.figure(figsize=(10, 5))
plt.plot(x_track, y_track, label=f"Trajectory with Drag (c={c})", color="crimson", lw=2)
plt.title("2D Projectile Motion Simulation with Atmospheric Drag", fontsize=14)
plt.xlabel("Horizontal Distance (meters)", fontsize=11)
plt.ylabel("Vertical Height (meters)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(0, color='black', lw=1)
plt.legend()

# Save the visualization graph to an image file automatically
plt.savefig("trajectory_graph.png", dpi=300)
plt.show()
