.data
str_0: .asciiz "string"
.text
main:
la $t0, str_0
li $v0, 10  # Syscall to exit
syscall
L1:  # Procedure L1
L2:  # Procedure L2