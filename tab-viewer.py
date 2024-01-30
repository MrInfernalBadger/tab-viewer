# tab = input("Please enter tab")
# song_name = input("Please enter song name")
file_name = "Little lion  man - Mumford and Sons.txt"


with open(file_name) as file:
    tab = file.read()



lines = tab.splitlines()


longest_line = 0
screen_length = 40
for line in lines:
    longest_line = len(line) if len(line) > longest_line else longest_line
    
longest_line += 3
     
for line in enumerate(lines):
    line_padding = longest_line - len(line[1].rstrip())
    lines[line[0]] = line[1].rstrip() + (" " * line_padding) + "|   "

result = ["" for i in range(screen_length)]
current_line = 0
for line in lines: 
    if current_line >= screen_length:
        current_line = 0
    result[current_line] += line
    
    current_line += 1



with open(file_name, 'w') as f:
    for line in result:
        f.write(line + '\n')
        
        
# COMPLETE input .txt file to edit rather than create entirely new file
# TODO create interface
# TODO vary column line spacing
