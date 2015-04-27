'''

Assigment: 
	
 				Stage 2: Submit Automate Your Page

Create a program python program that generates an output HTML Code. 
Once complete make sure to sumbit the following things: 
	1. HTML
	2. CSS
	3. Python file
	
	
	
	
Concepts: 
	
	
	LISTS - can be strings, characters, numbers, and other list
	Ex - stooges = [1,2,3]
	
	NESTED LIST - List within a List
	Ex - [ [1],[2],[3] ]
	
	MUTATION - modify list values 
	Ex - P = ["H","i"]
	     P[0] = "Y"
	     Print P        # P = ["Y","I"] 
	
	Aliasing - Two different ways to refer to that same object
	Ex - P = ["H","i"]
	     Q = P
		 P[0] = "Y"
		
		     Print Q        # Q = ["Y","I"] 
		     Print P        # P = ["Y","I"]
    For Loop - 
       
        for <name> in <list>:
	        <
	          block of code to run
	        > 


'''


# HTML Template to use

def generate_concept_HTML(spacing,title,description):
	

	
	
	html_1 = '''
	<div class = "concept">
	
	     <div class = "concept-title">
	
	     ''' + spacing + title
	html_2 = '''
	     </div>
	
	     <div class = "concept-description">
	
	         '''+ description 
	
	html_3 ='''
	     </div>
	
	</div>
	''' 
	
	full_html = html_1 + html_2 + html_3
	return full_html 
	
	
# FOR LOOP - used to select, extract, and cycle through  variable, 'EXAMPLE_LIST' list information

def generate_all_html(concept_list):
	
	i = '  '  # moved outside of For Loop so it won't get overwritten
	
	for concept in concept_list: 
		
		spacing = concept[0]       # Ex - concept[0] = '      '   
		
		title = concept[1]         # Ex - concept[1] = Python
		
		description = concept[2]   # Ex - concept[2] = Python is a ...
		
		text = generate_concept_HTML(spacing,title,description)  # text = moved string values into generater_concept_HTML 
		
		
		i = i + text  # i = '   ' + text  = '   ' '  ' Python Python is a 
		
	return i 



# Input LIST for program 
EXAMPLE_LIST = [
					['      ','Python:', 'Python is a Programming Language'],
					['      ','For Loop:', 'For Loops allow you to iterate over lists'],
					['      ','List:', 'Can be strings, characters, numbers, and other list'],
					['      ','Nested List: ', 'List within a List']
					
					
					
				]

# Output HTML Code
print generate_all_html (EXAMPLE_LIST)