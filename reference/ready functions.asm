	
	bne $t1, $t2 do_something  	# if $t1 != $t2 -> do_something | else -> next line
					# if $t1 == $t2 -> next line | else -> do_something
	
	beq $t1, $t2 do_something 	# if $t1 == $t2 -> do_something | else -> nxet line
					# if $t1 != $t2 -> next line | else -> do_something
	
	bgt $t1, $t2, do_something 	# if $t1 > $t2 -> do_something | else -> next line
					# if $t1 < $t2 -> next line | else -> do_something
	
	blt $t1, $t2, do_something	# if $t1 > $t2 -> next line | else -> do_something
					# if $t1 < $t2 -> do_something | else -> next line
	

	
	srl $a0,$a0,4 			# shift right logic 4 the value of $a0 and sve it at $a0
					        # example: $a0 = 0xc52 = 1100 0101 0010
						   $a0    >>>> 	 1100 0101      = 0xc5
						   $a0 = 0xc5



					
	and $t3,$a0,$t1  		# examle: $a0 = 0xc52 = 1100 0101 0010
						  $t1 = 0xc43 = 1100 0100 0011
						  $a0 and $t1 = 1100 0100 0010 = 0xc42
						  $t3 = 0x42
	

	or $t3,$a0,$t1  		# examle: $a0 = 0xc52 = 1100 0101 0010
						  $t1 = 0xc43 = 1100 0100 0011
						  $a0 or $t1  = 1100 0101 0011 = 0xc53
						  $t3 = 0x53
		



	jal do_something		# jump to do_something
	
	jr $ra				# jump back to next line afrer last jal
	
	



	# ------------------------------------------------------------------------------------
	
	
	
	work with arrays:

	(1) load the address of the array:		la $a0, myArray

	(2) read from the array:			lw, $t1, 0($a0)		$t1 = myArray[0]
							lw, $t1, 4($a0)		$t1 = myArray[1]
							lw, $t1, 8($a0)		$t1 = myArray[2]
	
	(3) write to the array:				sw, $t1, 0($a0)		myArray[0] = $t1
							sw, $t1, 4($a0)		myArray[4] = $t1
							sw, $t1, 8($a0)		myArray[8] = $t1

	



	# ------------------------------------------------------------------------------------

	

	work with .asciiz (string):

	(1) load the address of the string:		la $a0, myString	$a0 = adrress of myString

	(2) read char from the string			lw $t4, ($a0)		$t4 = myString	
							lbu $t1($a0)		$t1 = myString[0]
							srl $t4, $t4, 4		$t4 = myString >> 4
							sw $t4, ($a0)		$a0 = my string
							lbu $t1($a0)		$t1 = myString[1]




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
		
		
		
		
		