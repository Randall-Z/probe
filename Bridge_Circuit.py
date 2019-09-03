Bridge Circuit
*
VS 1 0 DC 10V
VM 3 5 DC 0;current monitor
R1  1 2 100
R2 2 3 100
R3 2 4 100
R5 4 0 300
R6 4 5 50
.DC VS 0 10 2
.PRINT DC I(VM)
.END