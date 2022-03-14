```


	
	bne $t1, $t2 do_something  	# if $t1 != $t2 -> do_something | else -> next line
					# if $t1 == $t2 -> next line | else -> do_something
	
	beq $t1, $t2 do_something 	# if $t1 == $t2 -> do_something | else -> nxet line
					# if $t1 != $t2 -> next line | else -> do_something
	
	bgt $t1, $t2, do_something 	# if $t1 > $t2 -> do_something | else -> next line
					# if $t1 < $t2 -> next line | else -> do_something
	
	blt $t1, $t2, do_something	# if $t1 > $t2 -> next line | else -> do_something
					# if $t1 < $t2 -> do_something | else -> next line
	
	
	and $a0, $t1, $t2		# if $t1 == t2 -> $a0 = $t1 | else $a0 = 0
	
	or $a0, $t1, $t2		# if 
	
	
	
	jal do_something		# jump to do_something
	
	jr $ra				# jump back to next line afrer last jal
	
	
	# ------------------------------------------------------------------------------------
	
	
	
	exit_program:		# exit the program
		li $v0, 10
		syscall
	
	print_int:		# print intager 
		addi $a0, $zero, 5
		li $v0, 1
		syscall
	
	print_char:		# print char 
		add $a0, $zero, $s3
		li $v0, 11
		syscall
		
	print_char:		# print char 2 
		lw $a0, char
		li $v0, 4
		syscall
	
	print_asciiz:		# print string
		lw $a0, text
		li $v0, 4
		syscall
		
	
	# -------------------------------------------------------------------------------------------------
	


	
	# make up latter case
	upper:
		bgt $a0, 0x60, print_upper 	# if $a0 > 0x60 -> print_upper		
	
	print_upper:
		addi $a0, $a0 -32	# set $a0 = $a0 -32
		li $v0, 11		# load 11 for charcter
		syscall			# print
	
	
	
	
	#---------------------------------------------------------------------------------------------------
	
	# for loop
	main:
		li $s1, 0	# set i varibale
		li $s2, 10	# set range
		jal loop
	
	loop:
		beq $s1, $s2 exit	# if $a0 != $s3 -> next line | else -> jump to exit
		
		
		
		
		
		
		
		
	
		
```