'''
Project Name: Library of Congress
Author: John Hawker
Due Date: 07/28/2023
Course: CS1400-X02

This program will take an unsorted file and sort it into two files. The first
file will be a summary of the information in the first file. The second will be
the sorted information form the unsorted file.
'''
import sys



def parse_line(line):
    parts = line.strip("\n").split("|")
    text = parts[0]
    pg_num = int(parts[1])
    code = parts[2]
    return {"text": text, "pg_num": pg_num, "code": code}

def parse_lines(lines):
    text_list = []
    for line in lines:
        parsed_line = parse_line(line)
        text_list.append(parsed_line)
    return text_list

def get_code(entry):
    return entry.get('code')

def get_text(entry):
    return entry.get('text')

def group_entries(entries):
    # start with an empty dictionary
    groups = {}
    # iterate through entries
    for entry in entries:
        code = entry["code"]
        if code in groups:
            groups[code].append(entry)
        else:
            groups[code] = [entry]
    return groups
    # find code
    # if no group create group
    # add entries to groups

def library_of_congress(lines):
    parsed = parse_lines(lines)
    sorted_lines = sorted(parsed, key = get_code)
    groups = group_entries(sorted_lines)
    for group in groups.values():
        group.sort(key = get_pg_num)
    return groups

def display_results(groups):
    string = ""
    for code, group in groups.items():
        string += display_group(code, group) + "\n"
    return string

def display_group(code, entries):
    longest = find_longest(entries)
    shortest = find_shortest(entries)
    average = find_average(entries)
    return f"""{code}
Longest line ({longest['pg_num']}): {longest['text']}
Shortest line ({shortest['pg_num']}): {shortest['text']}
Average length: {average}
"""

def display_novels(groups):
    return "-----\n".join([display_novel(code, group) for code, group in groups.items()])
    # for code, group in groups.items():
    #     string += display_novel(code, group) + "-----\n"
    # return string

def display_novel(code, entries):
    string = code + "\n"
    for entry in entries:
        string += entry['text'] + "\n"
    return string

def get_pg_num(entry):
    return entry.get('pg_num')

def find_longest(list_of_entries):
    longest_length = None
    for entry in list_of_entries:
        length_of_text = len(entry['text'])
        if longest_length is None or length_of_text > longest_length:
            longest_entry = entry
            longest_length = length_of_text
        elif length_of_text == longest_length and entry['pg_num'] > longest_entry['pg_num']:
            longest_entry = entry
            longest_length = length_of_text
    return longest_entry

def find_shortest(list_of_entries):
    shortest_length = None
    for entry in list_of_entries:
        length_of_text = len(entry['text'])
        if shortest_length is None or length_of_text < shortest_length:
            shortest_entry = entry
            shortest_length = length_of_text
        elif length_of_text == shortest_length and entry['pg_num'] < shortest_entry['pg_num']:
            shortest_entry = entry
            shortest_length = length_of_text
    return shortest_entry

def find_average(list_of_entries):
    length_of_entry = 0
    for entry in list_of_entries:
        length_of_entry = len(entry['text']) + length_of_entry
    average = length_of_entry / (len(list_of_entries))
    average = round(average)
    return average

def main():
    text_file = sys.argv[1]
    with open(text_file, "r") as file:
        lines = file.readlines()
        groups = library_of_congress(lines)
        with open('novel_summary.txt', "w") as summary_output:
            summary_output.write(display_results(groups))
        with open('novel_text.txt', 'w') as text_output:
            text_output.write(display_novels(groups))

main()