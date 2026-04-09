data = """office, country, telephone
Chicago, USA, +1 312 373 1000
Beijing, China, +86 4008 900 505
Bangalore, India, +91 80 4064 9570
Porto Alegre, Brazil, +55 51 3079 3550
Chennai, India, +91 44 660 44766"""

def acquire_data(input):
    lines = input.split('\n')
    first_line = True
    result = [] # المجمع
    for line in lines:
        if first_line:
            first_line = False
            continue
        if line.strip() == "":
            continue

        record = line.split(',')
        if record[1].strip() == 'India':
            result.append(
                {'city': record[0].strip(), 'phone': record[2].strip()}
            )

    return result

if __name__ == "__main__":
    print(acquire_data(data))