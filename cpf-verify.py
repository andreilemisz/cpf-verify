########################################################################################
                        # This code validates an 11 digits CPF number #

user_cpf = "" # User input 11 digits CPF
user_cpf_9_digits = "" # First 9 digits used in the firt part of the verifying process
user_cpf_10_digits = "" # First 10 digits used in the second part of the verifying process
first_last_digit = "" # First digit after "-"
second_last_digit = "" # Second digit after "-"

multiplication_number = 10 # Part of the algorithm, used in a decreasing way, 10 or 11
result_multiplication = 0 # Result of each number multiplied by decreasing 10 or 11

end_result_first = 0 # Added numbers and result from the first operation
end_result_second = 0 # Added numbers and results from the second operation

user_cpf_formatted = 0 # Final number of the CPF formatted with dots and dash

########################################################################################

user_cpf = input("Please input your CPF number: ").replace(".", "").replace("-", "")

if user_cpf.isdigit() and len(user_cpf) == 11:

    # Taking the CPF into pieces to use later
    first_last_digit = user_cpf[-2]
    second_last_digit = user_cpf[-1]
    user_cpf_9_digits = user_cpf[:9]
    user_cpf_10_digits = user_cpf[:10]

    # Taking each digit from the 9 firsts, multiplying by 10 and adding together
    for digit_1 in user_cpf_9_digits:
        result_multiplication += (int(digit_1) * multiplication_number)
        multiplication_number -= 1

    # Part of the algorithm
    end_result_first = (result_multiplication * 10) % 11
    end_result_first = 0 if end_result_first >= 10 else end_result_first

    # Second part of the process: verifying the second digit, same process
    multiplication_number = 11
    end_result_second = 0
    result_multiplication = 0
    for digit_2 in user_cpf_10_digits:
        result_multiplication += int(digit_2) * multiplication_number
        multiplication_number -= 1
    
    end_result_second = (result_multiplication * 10) % 11
    end_result_second = 0 if end_result_second >= 10 else end_result_second
    
    # Formatting the number with dots and dash
    user_cpf_formatted = user_cpf[:3] + "." + user_cpf[3:6] + "." + user_cpf[6:9] + "-" + user_cpf[9:]

    if str(end_result_first) == str(first_last_digit) and str(end_result_second) == str(second_last_digit):
        print(f"The number {user_cpf_formatted} is a valid CPF number.")
        
    else:
        print(f"The number {user_cpf_formatted} is not a valid CPF number.")
    
else:
    print("Invalid number.")