[TOC]

![CNum](/branding/logo/logomark/CNumlogo.png)
# **NumericalCalculation**

  A library related to common **numerical calculations**.  

## License
NuericalCalculation is released under a  [GPLv3 license](https://github.com/Wang-sx0103/NumericalCalculation/blob/main/LICENSE). 

## Prerequisites
- You must have a python 3.x interpreter
- Install with pip
```shell
pip install CNum
```
- Install with setup scripts
	- Clone or download this repository.
	- Install the package using `python setup.py install`.

## Usage and function
### CNum
This package contains classes that users use directly.  
Then, we will introduce the functions of each class.  

#### Elimination
**This class contains several elimination methods for solving linear equations.**  

- Calling Class
```python
import CNum.Elimination as et
```
- Constructor

- Member function

#### FuncAppro
**This class contains a methods in order to construct an n-order polynomial.**  
- Calling Class
```python
import CNum.FuncAppro as fa
```
- Constructor

- Member function

#### Interpolation
**This class contains several interpolation methods in order to construct the interpolation polynomial function and calculate the value of the X-point.**  
- Calling Class
```python
import CNum.Interpolation as ip
```
- Constructor

- Member function

#### Iteration
**This class contains several iterative methods for solving linear equations.**  
- Calling Class
```python
import CNum.Iteration as it
```
- Constructor

- Member function

#### Power
**This class contains several power methods in order to solve the maximum eigenvalue according to the mold and the corresponding eigenvector**  
- Calling Class
```python
import CNum.Power as pr
```
- Constructor

- Member function

#### SquareRoot
**This class contains several square root methods for solving linear equations that it contains a coefficient matrix with positive definite symmetry.**  
- Calling Class
```python
import CNum.SquareRoot as sr
```
- Constructor

- Member function

#### TriDecomposition
**This class contains several triangular decomposition methods for solving linear equations.**  
- Calling Class
```python
import CNum.TriDecomposition as td
```
- Constructor

- Member function

### lib
This package is designed to implement the functions of CNum package, but users can still use it.  
The contents of this package are function sets.  
Then, we will introduce the functions of each function set.   

#### Init
- Calling Module
```python
import CNum.lib.Init as init
```
- Function

#### IsOk
- Calling Module
```python
import CNum.lib.IsOk as ok
```
- Function

#### MatCal
- Calling Module
```python
import CNum.lib.MatCal as mc
```
- Function

#### Matrix
- Calling Module
```python
import CNum.martix.Matrix as mat
```
- Function

## Demo
