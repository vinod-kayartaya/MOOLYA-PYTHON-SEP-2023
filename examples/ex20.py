"""
Convert a CSV file into a JSON file

CSV example:
id,name,email,phone,gender,married
1,Vinod Kumar,vinod@vinod.co,9731424784,Male,true
2,Suma,suma@xmpl.com,929292822,Female,false


JSON Example:
[
    {
        "id": 1,
        "name": "Vinod Kumar",
        "email": "vinod@vinod.co",
        "gender": "Male",
        "married": true
    },
    {
        "id": 2,
        "name": "Suma",
        "email": "suma@xmpl.com",
        "gender": "Female",
        "married": false
    }
]

"""
import time
import json


def main():
    filename = input('Enter CSV filename: ')

    if not filename.endswith('.csv'):
        raise ValueError('Filename must end with .csv')

    new_filename = f'{filename[:-4]}_{time.time()}.json'

    with open(filename, encoding='utf-8') as input_file:
        header = input_file.readline().strip().split(',')
        data = [get_dict(one_line, header) for one_line in input_file]

        with open(new_filename, 'w') as output_file:
            json.dump(data, output_file, indent=3)
            print(f'JSON data stored in file "{new_filename}"')


def get_dict(one_line, header):
    one_line = [int(f) if f.isdigit() else f for f in one_line.strip().split(',')]
    return dict(zip(header, one_line))


if __name__ == '__main__':
    main()
