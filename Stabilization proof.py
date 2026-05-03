import numpy as np

# Arrhenius parameters elicited via 'Industrial Material Preservation' logic
R = 8.314          # Universal Gas Constant
A = 1e10           # Frequency factor
Ea = 100000        # Activation Energy (J/mol) for degradation

def get_viability_hours(temp_celsius):
    T_kelvin = temp_celsius + 273.15
    # Arrhenius Equation for degradation rate k
    k = A * np.exp(-Ea / (R * T_kelvin))
    # Time to 90% viability (t90)
    t_90 = -np.log(0.9) / k
    return t_90 / 3600

# Testing various logistical scenarios
room_temp = get_viability_hours(25)
cold_chain = get_viability_hours(4) / 24  # Days

print(f"--- STABILIZATION ANALYSIS ---")
print(f"Viability at 25°C (Unrefrigerated): {room_temp:.2f} hours")
print(f"Viability at 4°C (Standard Cold Chain): {cold_chain:.2f} days")
