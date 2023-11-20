def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height)/4
    return h

def pressure_gain_from_water_height(height):
    p = 998.2
    g = 9.80665
    P = (p * g * height)/1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    p = 998.2
    p_lost_from_pipe = (-1 * (friction_factor * pipe_length * p * (fluid_velocity ** 2))) / (2000 * pipe_diameter)
    return p_lost_from_pipe

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    p = 998.2
    p_lost_from_fittings = (-0.04 * (p * (fluid_velocity ** 2) * quantity_fittings)) / 2000
    return p_lost_from_fittings 

def reynolds_number(hydraulic_diameter, fluid_velocity):
    p = 998.2
    u = 0.0010016
    reynolds_number_value = (p * hydraulic_diameter * fluid_velocity) / u
    return reynolds_number_value

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    p = 998.2
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) -1)
    lost_pressure = (-1 * (k * p * (fluid_velocity ** 2))) / 2000
    return lost_pressure

def pressure_conversion():
    psi = 0.145038 * main()
    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    return pressure


if __name__ == "__main__":
    main()
    
print()
print(f"The final pressure value can be expressed as:\n{(main()):.2f} psi, which is equivalent to:\n{(pressure_conversion()):.2f} kPa.")