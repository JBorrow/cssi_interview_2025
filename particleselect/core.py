"""
Use this interface to implement your solution.
"""

import math


class ParticleConfigurator:
    def __init__(self, particles: list[list[float]]):
        self.setup(particles=particles)

    def setup(self, particles: list[list[float]]):
        """
        This function should set up any necessary internal state.
        """
        # Example:
        self.particles = particles
        return

    def search(self, center: list[float], radius: float) -> int:
        """
        This function should return the number of particles in a sphere
        centered on 'center' and with 'radius'.
        """
        # Example:
        in_radius = 0
        for n in range(len(self.particles)):
            dx = center[0] - self.particles[n][0]
            dy = center[1] - self.particles[n][1]
            dz = center[2] - self.particles[n][2]

            r = math.sqrt(dx**2 + dy**2 + dz**2)

            if r < radius:
                in_radius = in_radius + 1

        return in_radius
