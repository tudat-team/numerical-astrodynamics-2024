'''
Copyright (c) 2010-2020, Delft University of Technology
All rigths reserved

This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.
'''


import os
from integrator_analysis_helper_functions import *

current_directory = os.getcwd( )

spice.load_standard_kernels()
spice.load_kernel( current_directory + "/juice_mat_crema_5_1_150lb_v01.bsp" );

bodies = create_bodies( )

# Define list of integrator tolerances
integration_tolerances = [1.0E-12, 1.0E-10, 1.0E-8, 1.0E-6]

# Iterate over the mission phases
for current_phase in range( len(central_bodies_per_phase )):

    # Create initial state and time
    current_phase_start_time = ...
    current_phase_end_time = ...

    # Define central body of propagation
    current_central_body = central_bodies_per_phase[ current_phase ]

    # Define termination conditions (enforce exact termination time)
    termination_condition = propagation_setup.propagator.time_termination(
        current_phase_end_time,
        terminate_exactly_on_final_condition=True)

    # Create acceleration models for perturbed case
    perturbed_acceleration_models = get_perturbed_accelerations( current_central_body, bodies)

    # Define integrator settings for benchmark
    benchmark_integrator_settings = ...

    # Create integrator settings
    step_size_control_settings = propagation_setup.integrator.step_size_control_elementwise_scalar_tolerance( ... )
    step_size_validataion_settings = propagation_setup.integrator.step_size_validation( ... )
    variable_step_integrator_settings = propagation_setup.integrator.runge_kutta_variable_step( ... )

    # Create propagator settings for perturbed case
    perturbed_propagator_settings = ...

    # Propagate benchmark dynamics
    benchmark_dynamics_simulator = ...

    # Create interpolator for benchmark results
    interpolator_settings = interpolators.lagrange_interpolation( 8 )
    benchmark_interpolator = interpolators.create_one_dimensional_vector_interpolator(
        benchmark_dynamics_simulator.state_history, interpolator_settings )

    # Perform integration of dynamics with different tolerances
    for current_tolerance in integration_tolerances:

        # Define integrator step settings
        initial_time_step = 10.0
        minimum_step_size = 1.0E-16
        maximum_step_size = np.inf

        # Retrieve coefficient set
        coefficient_set = ...

        # Create variable step-size integrator settings
        integrator_settings = ...

        # Define output file name
        file_output_identifier = "Q3_tolerance_index_" + str(integration_tolerances.index(current_tolerance)) + "_phase_index" + str(current_phase)

        # Propagate dynamics for perturbed and unperturbed case
        perturbed_dynamics_simulator = ...

        write_propagation_results_and_benchmark_difference_to_file(
                perturbed_dynamics_simulator,
                file_output_identifier,
                benchmark_interpolator)
    
