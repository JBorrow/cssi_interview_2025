"""
A test for your solution.
"""

from random import random

from particleselect.core import ParticleConfigurator


def in_radius(position, particle, r):
    distance2 = (
        (position[0] - particle[0]) ** 2
        + (position[1] - particle[1]) ** 2
        + (position[2] - particle[2]) ** 2
    )
    r2 = r * r

    return distance2 <= r2


def test_example():
    test_centers = [[0.5, 0.5, 0.5], [0.25, 0.25, 0.25]]
    test_radii = [0.2, 0.1]

    particles = [[random(), random(), random()] for _ in range(1024)]

    configurator = ParticleConfigurator(particles)

    for center, radius in zip(test_centers, test_radii):
        brute_force = sum([in_radius(center, p, radius) for p in particles])
        test_answer = configurator.search(center, radius)

        assert test_answer == brute_force
