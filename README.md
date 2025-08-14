Interview Question
------------------

### Introductory remarks

- Please read this description in its entirety - it's all important!
- Do not use any AI-assisted tools for this project. That includes, but is
  not limited to: ChatGPT, Claude Code, and GitHub Copilot.
- You must only use the python standard library to solve these questions. 
  That means no imports that you would need to `pip` install. So libraries
  like `math` are ok, `numpy` is not. The only allowed libraries are in
  the `pyproject.toml` as dependencies.

### Repository Overview

This repository contains one important file - `particleselect/core.py`. Inside that
file there's a class, `ParticleConfigurator`, with two stub methods: `setup`, and
`search`. That's where you'll be making your changes.

### Stub Functions

`setup` takes a list of three-dimensional particle positions, bounded by [0,1]. So
for example it could take:

```
particles=[
  [0.1, 0.1, 0.1],
  [0.2, 0.2, 0.1]
]
```

You should use `setup` to create any necessary internal state inside
`ParticleConfigurator` to allow the below `search` function to be as efficient
as possible.

`search` takes a center and a radius, and returns the number of particles within
a sphere with the radius provided centered on the provided center.

So for the above set of particles, using a center of `[0.9, 0.9, 0.9]` and radius
`[0.3]` would return 0. `[0.1, 0.1, 0.1], 1.0` would return 2.

There is a test that can be run with `pytest` that solves the brute-force version
of the problem and compares it to your answer. Your main goal is to have a solution
that is more efficient than the brute force one.

The boundaries for the problem are open, i.e. not periodic.

### Running Tests

You should probably create a virtual environment and install the package in editable
mode. Using `pytest` from the root of the repository will tell you whether your
solution works or not.
