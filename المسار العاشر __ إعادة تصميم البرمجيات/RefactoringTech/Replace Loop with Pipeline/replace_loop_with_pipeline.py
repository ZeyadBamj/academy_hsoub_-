data = """office, country, telephone
Chicago, USA, +1 312 373 1000
Beijing, China, +86 4008 900 505
Bangalore, India, +91 80 4064 9570
Porto Alegre, Brazil, +55 51 3079 3550
Chennai, India, +91 44 660 44766"""

def acquire_data(inp):
    lines = inp.split('\n')
    loop_items = lines[1:]
    loop_items = filter(lambda line: line.strip() != "", loop_items)
    loop_items = map(lambda line: line.split(','), loop_items)
    loop_items = filter(lambda record: record[1].strip() == 'India', loop_items)
    loop_items = map(lambda record: {'city': record[0].strip(), 'phone': record[2].strip()}, loop_items)

    result = list(loop_items)
    return result

if __name__ == "__main__":
    print(acquire_data(data))