charToArray = {
    " " : [[0,0],[0,0],[0,0]],
    "a" : [
            [1,0],
            [0,0],
            [0,0]
        ],
    "b" : [
            [1,0],
            [1,0],
            [0,0]
        ],
    "c" : [
            [1,1],
            [0,0],
            [0,0]
        ],
    "d" : [
            [1,1],
            [0,1],
            [0,0]
        ],
    "e" : [
            [1,0],
            [0,1],
            [0,0]
        ],
    "f" : [
            [1,1],
            [1,0],
            [0,0]
        ],
    "g" : [
            [1,1],
            [1,1],
            [0,0]
        ],
    "h" : [
            [1,0],
            [1,1],
            [0,0]
        ],
    "i" : [
            [0,1],
            [1,0],
            [0,0]
        ],
    "j" : [
            [0,1],
            [1,1],
            [0,0]
        ],
    "k" : [
            [1,0],
            [0,0],
            [1,0]
        ],
    "l" : [
            [1,0],
            [1,0],
            [1,0]
        ],
    "m" : [
            [1,1],
            [0,0],
            [1,0]
        ],
    "n" : [
            [1,1],
            [0,1],
            [1,0]
        ],
    "o" : [
            [1,0],
            [0,1],
            [1,0]
        ],
    "p" : [
            [1,1],
            [1,0],
            [1,0]
        ],
    "q" : [
            [1,1],
            [1,1],
            [1,0]
        ],
    "r" : [
            [1,0],
            [1,1],
            [1,0]
        ],
    "s" : [
            [0,1],
            [1,0],
            [1,0]
        ],
    "t" : [
            [0,1],
            [1,1],
            [1,0]
        ],
    "u" : [
            [1,0],
            [0,0],
            [1,1]
        ],
    "v" : [
            [1,0],
            [1,0],
            [1,1]
        ],
    "w" : [
            [0,1],
            [1,1],
            [0,1]
        ],
    "x" : [
            [1,1],
            [0,0],
            [1,1]
        ],
    "y" : [
            [1,1],
            [0,1],
            [1,1]
        ],
    "z" : [
            [1,0],
            [0,1],
            [1,1]
        ],
    
    
}


num_to_array = {
    
    "1" : [
            [1,0],
            [0,0],
            [0,0]
        ],
    "2" : [
            [1,0],
            [1,0],
            [0,0]
        ],
    "3" : [
            [1,1],
            [0,0],
            [0,0]
        ],
    "4" : [
            [1,1],
            [0,1],
            [0,0]
        ],
    "5" : [
            [1,0],
            [0,1],
            [0,0]
        ],
    "6" : [
            [1,1],
            [1,0],
            [0,0]
        ],
    "7" : [
            [1,1],
            [1,1],
            [0,0]
        ],
    "8" : [
            [1,0],
            [1,1],
            [0,0]
        ],
    "9" : [
            [0,1],
            [1,0],
            [0,0]
        ],
    "0" : [
            [0,1],
            [1,1],
            [0,0]
        ],
    
    }


special_to_array = {
    
    
    "Cap" : [
            [0,0],
            [0,0],
            [0,1]
        ],
    
    "Dec" : [
            [0,1],
            [0,0],
            [0,1]
        ],
    
    "Num" : [
            [0,1],
            [0,1],
            [1,1]
        ], 
    
    }

punc_to_array = {
    
    "." : [
            [0,0],
            [1,1],
            [0,1]
        ],
    
    "," : [
            [0,0],
            [1,0],
            [0,0]
        ],
    
    "?" : [
            [0,0],
            [1,0],
            [1,1]
        ],
    
    "!" : [
            [0,0],
            [1,1],
            [1,0]
        ],
    
    ":" : [
            [0,0],
            [1,1],
            [0,0]
        ],
    
    ";" : [
            [0,0],
            [1,0],
            [1,0]
        ],
    
    "-" : [
            [0,0],
            [0,0],
            [1,1]
        ],
    
    "/" : [
            [0,1],
            [0,0],
            [1,0]
        ],
    
    "<" : [
            [0,1],
            [1,0],
            [0,1]
        ],
    
    ">" : [
            [1,0],
            [0,1],
            [1,0]
        ],
    
    "(" : [[1,0],
           [1,0],
           [0,1]],
    
    ")" : [[0,1],
           [0,1],
           [1,0]],

    }


def eng_to_braille_matrix(string):
    string_array = list(string)
    
    
    braille_matrices = []
    
    numeric = False
    
    for i in range(len(string_array)):
        
        
        if string_array[i] == " ": #space
            
            braille_matrices.append(charToArray[" "])
            numeric = False
            
        elif string_array[i].isalpha(): #letter
            
            if string_array[i].isupper(): #capital
                braille_matrices.append(special_to_array["Cap"])
                
            braille_matrices.append(charToArray[string_array[i].lower()])
        
        elif string_array[i].isnumeric(): #digit
        
            if numeric == False:
                braille_matrices.append(special_to_array["Num"])
        
            braille_matrices.append(num_to_array[string_array[i]])
            numeric = True
        
        elif (i < len(string_array) - 1) and string_array[i+1].isnumeric and string_array[i] == ".": #decimal point
            
            braille_matrices.append(special_to_array["Dec"])
            
        
        else: #punctuation
            braille_matrices.append(punc_to_array[string_array[i]])
            
    return braille_matrices

def braille_matrix_to_flat_string(braille_matrix):
    
    flattened = [elem for sublist1 in braille_matrix for sublist2 in sublist1 for elem in sublist2]
    
    string = ""
    
    #print(flattened)
    
    
    for i in range(len(flattened)):
        if flattened[i] == 0:
            string += "."
        else:
            string += "O"
            
    return string

def single_mat_to_string(braille_matrix):
    string = ""
    for row in braille_matrix:
        for column in row:
            if column == 0:
                string += "."
            else:
                string += "O"
            
    return string


def switch_kv (d):
    
    new_dict = {}
    
    for key in d:
        new_dict[single_mat_to_string(d[key])] = key
    return new_dict

arr_to_char = switch_kv(charToArray)
arr_to_num = switch_kv(num_to_array)
arr_to_special = switch_kv(special_to_array)
arr_to_punc = switch_kv(punc_to_array)

def braille_to_eng(string):
    
    chars = []
    char = ""
    start = 0
    for i in range (len(string) // 6):
        
        char = string[start : (i+1) * 6 ]
        chars.append(char)
        
        
        start = 6 * (i + 1)
        
    #print(chars)
    
    string = ""
    cap = False
    num = False
    for char in chars:
        if(char == ".....O"): #capital
            cap = True
        
        elif (cap):
            string += arr_to_char[char].upper()
            cap = False
            
        elif (char == ".O.OOO"): #num
            num = True
            
        elif (num and char != ".O...O"):
            string += arr_to_num[char]
            
        elif (char == "......"): #space
            string += " "
            num = False
            
        elif (char == ".O...O"): #decimal
            string += "."
        
        else:
            string += arr_to_char[char]
        
        
    return string

def is_braille(string):
    for i in range(len(string)):
        if string[i] != "." and string[i] != "O":
            return False
        
    return True


if __name__ == "__main__":
    user_input = input()
    
    if(is_braille(user_input)):
        print(braille_to_eng(user_input))
    
    else:
        print(braille_matrix_to_flat_string(eng_to_braille_matrix(user_input)))
        
        
