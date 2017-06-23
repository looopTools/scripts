#!/usr/bin/env python3

# parse-csv-latex-table
# By: tools
# Status: in development
# This script is used for converting csv file data into a latex table
# in the tabular environment
#
# The idea is that it also later should be used for tabularx
#############################################################
# Current bugs                                              #
# - New line seperators seems to be a problem               #
#                                                           #
#############################################################

centered = True
float_position = 'ht'
label = 'tbl:'
label_text = ''
caption = ''
format_text = ''
tabular = True
input_file = ''
output_file = ''

def generate_row(line):
    line = line.replace(',', ' & ')
    line = '    ' + line + ' \\\\ \\hline \n'
    return line

def generate_table_start():
    head = '\\begin{{table}}[{}]\n'.format(float_position)
    if centered:
        head = head + '\\centering\n'
    return head

def generate_table_tail():
    return '\\caption{{{}}}\n\\label{{{}{}}}\n\\end{{table}}'.format(caption, \
                                                                     label, \
                                                                     label_text)

def generate_tabular_head():
    head = '\\begin{{{}}}{{{}}}\n'.format('tabular', format_text)
    return head

def generate_tabular_tail():
    return '\\end{{{}}}'.format('tabular')

def generate_table():
    i = open(input_file, 'r')
    lines = ''
    for line in i:
        lines = lines + generate_row(line)
    o = open(output_file, 'w')
    o.write(generate_table_start())
    o.write(generate_tabular_head())
    o.write(lines)
    o.write(generate_tabular_tail())
    o.write(generate_table_tail())


float_position = raw_input('Float position: ')
label_text = raw_input('Label text: ')
caption = raw_input('Caption text: ')
format_text = raw_input('Table format: ')

input_file = raw_input('Input file: ')
output_file = raw_input('Output file: ')
generate_table()
