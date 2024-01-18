import csv

def read_last_column(csv_file_path):
	with open(csv_file_path, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		plus = 0
		minus = 0
		for row in reader:
			# Check if the line does not start with '!'
			if not row or not row[0].strip().startswith('!'):
				# Print the last column if the condition is met
				if row:
					val = float(row[-1].replace(',', '.').replace(' ', ''))
					if val > 0:
						plus += val
						print(row)
					else:
						minus += val
	return plus, minus


# Replace 'your_csv_file.csv' with the path to your CSV file
csv_file_path = 'r.csv'
p, m = read_last_column(csv_file_path)

print(f"p = {p}, m = {m}")
