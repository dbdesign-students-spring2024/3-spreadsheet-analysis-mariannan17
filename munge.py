def clean_data(raw_data):
    cleaned_data = []
    for line in raw_data:
        row = line.strip().split(',')
        cleaned_row = [value if value != "(null)" else "-1" for value in row]
        beginning_columns = cleaned_row[:-6]
        edited_columns = cleaned_row[-6:-5] + cleaned_row[-3:-1]
        cleaned_row = beginning_columns + edited_columns
        cleaned_data.append(cleaned_row)
    return cleaned_data

def main():
    with open("data/readme.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()
    
    cleaned_data = clean_data(raw_data)

    with open("data/clean_data.csv", "w", encoding="utf-8") as file:
        for row in cleaned_data:
            file.write(','.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()
