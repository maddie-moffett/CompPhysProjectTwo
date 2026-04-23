# CompPhysProjectTwo
Second project for Computational Physics Project Version 1

## Electric Field of a Parallel Plate Capacitor

This project test relaxation methods in calculating the electric potential in a 2D region with parallel-plates
held at opposite potentials (say ±1) surrounded by a grounded square box. Here, you’ll test the basic Jacobi
method versus simultaneous over-relaxation (SOR) and also use the final result to calculate and plot the electric
field. Consider the electric potential and electric field in a grounded square box with two parallel plates:

Assume that the plates are half as tall as the side of the box and that they are positioned so that 1/3 of the
box is to the left of the negative plate, 1/3 in the middle and 1/3 to the right of the positive plate.

### Part A
Discuss qualitatively what you expect for the electric field in this region. Describe what you expect to
happen to the electric field as the plates are brought close together.

### Part B
Write a program to solve for the potential in the box using basic Jacobi and SOR routines. Design the
program to run until a convergence criteria is met: max |Vnew − V | < ε where max indicates the maximum value of
this array and ε is a small (user specified) number.

### Part C
Use a box with N = 100 grid points on each side and test the number of iterations required to come to
convergence as you vary the weighting of the over-relaxation from 1.0 to 1.5. What is the optimal value?

### Part D
Use the optimal weighting found in the previous step and compare the scaling of the convergence with the
number of grid points. Plot the scaling of the basic Jacobi convergence and the optimal SOR convergence
versus N. You can use other values but use at least N = 50, 100, 200, 400.

### Part E
Use finite difference to calculate the electric field of the solution and make a quiver plot of the electric
field. Move the positions of the plates closer together, make new plots of the electric field and check your
hypothesis from part (a).
