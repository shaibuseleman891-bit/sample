numbers = [1,2,3,4,5]
def added_ten(n):
    return n + 10
results = list(map(added_ten, numbers))
print(results)


names = ['juma', 'saidi', 'habiba', 'mwajuma']
names_upper = list(map(str.upper, names))
print(names_upper)


numbers = [2,3,4,5]
def squared_number(n):
    return n**2
numbers_squared = list(map(squared_number, numbers))
print(numbers_squared)


numbers = [1,2,3,4,5]
def converted(n):
    return str(n)
print(list(map(converted, numbers)))


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
def combined(x,y):
    return x +y
matokeo = list(map(combined, list1, list2))
print(matokeo)


words = ['python', 'programmng', 'map']
majibu = list(map(str.__len__, words))
for name, count in zip(words, majibu):
    print(f'{name} = {count}')
    

fahreiheit = [50,60,70,80,90]
def converted(temp):
    return f'{((temp - 32) * 5/9):.2f}'
converted_temp = list(map(converted, fahreiheit))
print(converted_temp) 

    
    
my_list = [' hello ', ' word ' ,' python ']
new = list(map(str.strip, my_list))
print(new)

students_scores = [(80, 90, 100), (70,85,90), (60, 75, 80)]
def total(scores):
    return  sum(scores)
results = list(map(total, students_scores))
print(results)

numbers = [-2, 0, 5, 10,-7]
def datatype(n):
    if n > 0:
        return True
    else:
        return False
datatypes = list(map(datatype, numbers))
print(datatypes)



import re

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
    }
    return constraints

def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)
print(find_invalid_records(**medical_records[0]))    
    

   
    