# IF-ELIF-ELSE
from pyscript import display, document

# FIRST EXAMPLE---------------------------

# def julias_answer(e):
#     document.getElementById('output').innerHTML = ' '
#     response = document.getElementById('input1').value.lower() # or .upper()so its not case sensitive anymore

    
#     if response == 'yes': 
#         display(f'Kian will be her valentine!', target='output')

#     elif response == 'no':
#         display(f'Kian will try again.', target='output')

#     elif response == 'maybe':
#         display(f'Do not give up!', target='output')

#     else: 
#         display(f'Invalid', target='output')

# SECOND EXAMPLE--------------------------

def students_classification(e):
    document.getElementById('output').innerHTML = ' '

    classification = float(document.getElementById('number1').value)

    if classification >= 95:
        display(f'Bergamo I', target='output')
    
    elif classification >= 91:
        display(f'Bergamo II', target='output')

    elif classification >= 86:
        display(f'Bergamo III', target='output')
    
    elif classification >= 75:
        display(f'Perugia I', target='output')
    
    elif classification >= 65:
        display(f'Perugia II', target='output')

    elif classification < 65:
        display(f'Type an appropriate number!', target='output')

    elif classification > 100:
        display(f'Type an appropriate number!', target='output')

    else:
        display(f'Invalid number', target='output')

    



