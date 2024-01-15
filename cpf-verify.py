########################################################################################
                        # This code validates an 11 digits CPF number #

user_cpf = "" # User input 11 digits CPF

multiplication_number = 10 # Part of the algorithm, used in a decreasing way, 10 or 11

end_result_first = 0 # Added numbers and result from the first operation
end_result_second = 0 # Added numbers and results from the second operation

########################################################################################

user_cpf = input("Please input your CPF number: ").replace(".", "").replace("-", "")

# Just to prevent a CPF number like 000.000.000-00
if user_cpf[0] * len(user_cpf) == user_cpf:
    print("Your CPF is invalid. You cannot input a sequence of repeated numbers.")

elif user_cpf.isdigit() and len(user_cpf) == 11:

    # Taking each digit from the 9 firsts, multiplying by 10 and adding together
    for digit_1 in user_cpf[:9]:
        end_result_first += (int(digit_1) * multiplication_number)
        multiplication_number -= 1

    # Part of the algorithm
    end_result_first = (end_result_first * 10) % 11
    end_result_first = 0 if end_result_first >= 10 else end_result_first

    # Second part of the process: verifying the second digit, same process
    multiplication_number = 11
    for digit_2 in user_cpf[:10]:
        end_result_second += int(digit_2) * multiplication_number
        multiplication_number -= 1
    
    end_result_second = (end_result_second * 10) % 11
    end_result_second = 0 if end_result_second >= 10 else end_result_second
    
    # Formatting the number with dots and dash
    user_cpf = user_cpf[:3] + "." + user_cpf[3:6] + "." + user_cpf[6:9] + "-" + user_cpf[9:]

    if str(end_result_first) == str(user_cpf[-2]) and str(end_result_second) == str(user_cpf[-1]):
        print(f"The number {user_cpf} is a valid CPF number.")
        
    else:
        print(f"The number {user_cpf} is not a valid CPF number.")
    
else:
    print("Invalid number. Please add only eleven numbers.")