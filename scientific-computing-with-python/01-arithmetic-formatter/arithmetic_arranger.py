# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13

@author: ahmadalabassy
"""
def arithmetic_arranger(problems, display_answer = False):
    error_count = 0
    error_message = ''

    if len(problems) > 5:
        error_count += 1
        error_message = 'Error: Too many problems.'
    else:
        output_line_1 = ''
        output_line_2 = ''
        output_line_3 = ''
        output_line_4 = ''
        for problem in problems:
            items = problem.split()
            try:
                operand1 = int(items[0])
                operator = items[1]
                operand2 = int(items[2])
                result = None
                # operands positive value check
                if operand1 < 0 or operand2 < 0:
                    error_count += 1
                    error_message += 'Error: Numbers must be positive.\n'
                # operands four digit limit check
                if len(str(abs(operand1))) > 4 or len(str(abs(operand2))) > 4:
                    error_count += 1
                    error_message += 'Error: Numbers cannot be more than four digits.\n'
                # operator check
                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                else:
                    error_count += 1
                    error_message += 'Error: Operator must be \'+\' or \'-\'.\n'
                if error_count == 0:
                    len_diff = abs(len(items[0]) - len(items[2]))
                    evener, dashes = '', ''
                    for char in range(len_diff):
                        evener += ' '
                        dashes += '-'
                    for char in range(min(len(items[0]), len(items[2]))):
                        dashes += '-'
                    evener_at_first = bool(len(items[0]) - len(items[2]) <= 0)
                    output_line_1 += '  ' + (evener if evener_at_first else '') + str(operand1) + '    '
                    output_line_2 += ('+' if operator == '+' else '-') + ' ' + (evener if not evener_at_first else '') + str(operand2) + '    '
                    output_line_3 += '--' + dashes + '    '
                    if display_answer:
                        len_diff = 2 + max(len(items[0]), len(items[2])) - len(str(result))
                        evener = ''
                        for char in range(len_diff):
                            evener += ' '
                        output_line_4 += evener + str(result) + '    '
            except:
                error_count += 1
                error_message += 'Error: Numbers must only contain digits.\n'
                if error_count > 5:
                    error_message = 'Error: Too many errors.'
                    break
    
    if error_count > 0:
        return error_message.rstrip()
    else: return output_line_1.rstrip() + '\n' + output_line_2.rstrip() + '\n' + output_line_3.rstrip() + ('\n' + output_line_4.rstrip() if display_answer else '')