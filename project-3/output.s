.data
str_0: .asciiz "test"
str_1: .asciiz "string"
.text
main:
li $t0, 5
li $t2, 4
sgt $t1, $t0, $t2  # t1 = x gt 4
beq $t1, $zero, L1  # if not t1 goto L1
li $v0, 4  # Print string
la $a0, str_0
syscall
j L2  # goto L2
L1:  # Label L1
la $t3, str_1
L2:  # Label L2
li $v0, 10  # Syscall to exit
syscall