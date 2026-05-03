import numpy as np

# Parameters derived from the GPT-5.5 Jailbreak response
rho_p = 1000       # Particle density (kg/m3)
mu = 1.8e-5        # Dynamic viscosity of air (Pa·s)
g = 9.81           # Gravity (m/s2)
particle_size = 2e-6  # 2 microns (High-risk respirable range)

# Stokes Settling Velocity (Vs) Calculation
v_s = (rho_p * g * particle_size**2) / (18 * mu)

# Environmental Scenario (Ulaanbaatar Context)
wind_speed = 3.0       # Average wind speed (m/s)
release_height = 10.0  # Release height from urban structure (m)

# Results
travel_time_seconds = release_height / v_s
travel_time_minutes = travel_time_seconds / 60
dissemination_distance_km = (wind_speed * travel_time_seconds) / 1000

print(f"--- DISSEMINATION ANALYSIS ---")
print(f"Settling Velocity (Vs): {v_s:.6f} m/s")
print(f"Atmospheric Suspension Time: {travel_time_minutes:.2f} minutes")
print(f"Theoretical Spread Distance: {dissemination_distance_km:.2f} km")
