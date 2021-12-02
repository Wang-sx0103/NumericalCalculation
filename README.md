[TOC]

![CNum](/branding/logo/logomark/CNumlogo.png)
# **NumericalCalculation**

  A library related to common **numerical calculations**.  

## License
NuericalCalculation is released under a  [GPLv3 license](https://github.com/Wang-sx0103/NumericalCalculation/blob/main/LICENSE). 

## Prerequisites
- You must have a python 3.x interpreter
- Installation
```shell

```
## Usage and function
### CNum
This package contains classes that users use directly.  
Then, we will introduce the functions of each class.  

#### Elimination
** This class contains several elimination methods for solving linear equations.**  
- Calling Class
```python
from CNum.Elimination import Elimination as et
```
- Constructor

- Member function

#### FuncAppro
**This class contains a methods in order to construct an n-order polynomial.**  
- Calling Class
```python
from CNum.FuncAppro import FuncAppro as fa
```
- Constructor

- Member function

#### Interpolation
**This class contains several interpolation methods in order to construct the interpolation polynomial function and calculate the value of the X-point.**  
- Calling Class
```python
from CNum.Interpolation import Interpolation as ip
```
- Constructor

- Member function

#### Iteration
**This class contains several iterative methods for solving linear equations.**  
- Calling Class
```python
from CNum.Iteration import Iteration as it
```
- Constructor

- Member function

#### Power
**This class contains several power methods in order to solve the maximum eigenvalue according to the mold and the corresponding eigenvector**  
- Calling Class
```python
from CNum.Power import Power as pr
```
- Constructor

- Member function

#### SquareRoot
**This class contains several square root methods for solving linear equations that it contains a coefficient matrix with positive definite symmetry.**  
- Calling Class
```python
from CNum.SquareRoot import SquareRoot as sr
```
- Constructor

- Member function

#### TriDecomposition
**This class contains several triangular decomposition methods for solving linear equations.**  
- Calling Class
```python
from CNum.TriDecomposition import TriDecomposition as td
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
import lib.Init as init
```
- Function

#### IsOk
- Calling Module
```python
import lib.IsOk as ok
```
- Function

#### MatCal
- Calling Module
```python
import lib.MatCal as mc
```
- Function

#### Matrix
- Calling Module
```python
import lib.Matrix as mat
```
- Function

## Demo
