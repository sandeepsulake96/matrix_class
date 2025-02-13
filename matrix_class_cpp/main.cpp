#include <iostream>
#include <vector>
#include "matrix.h"

int main () {

    // assigning a 7x5 matrix to the variable initial_grid
    // all values in the matrix are 0.4
    std::vector <std:: vector <float> > 
        initial_grid (7, std::vector <float>(5, 0.4));

    // Using the initial grid variable to instantiate a matrix object
    Matrix matrixa(initial_grid);

    matrixa.matrix_print();

    // find the transpose and print

    Matrix transposea = matrixa.matrix_transpose();

    transposea.matrix_print();


    // 7x5 2-dimensional vector with values 0.2
    std::vector <std:: vector <float> > 
        second_grid (7, std::vector <float>(5, 0.2));

    // Instantiating an object called matrixb. Use the second_grid
    Matrix matrixb(second_grid);

    // Adding matrixa and matrixb and store the results in a new matrix
    // variable called matrixsum
    Matrix matrixsum(matrixa.matrix_addition(matrixb));

    // Print out the matrix contained in the matrixsum variable
    matrixsum.matrix_print();


    return 0;
}
