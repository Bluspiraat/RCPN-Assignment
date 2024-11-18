import os

def find_files(directory_path):
    file_paths = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_paths.append(os.path.join(directory_path, filename))
    return file_paths

def extract_information(files):
    variable = 0
    run = 0
    x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro = [], [], [], [], [], []
    for file in files:
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line and line[0].isdigit():
                    split_line = line.split()
                    numeric_values = [float(entry) for entry in split_line[2:]]
                    if variable == 0:
                        z_acc.append(numeric_values[2])
                        z_gyro.append(numeric_values[5])
                    elif variable == 1:
                        y_acc.append(numeric_values[1])
                        y_gyro.append(numeric_values[4])
                    elif variable == 2:
                        x_acc.append(numeric_values[0])
                        x_gyro.append(numeric_values[3])
        run = run + 1
        if run > 1:
            run = 0
            variable = variable + 1
            if variable > 2:
                variable = 0
    return [x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro]

def calculate_averages(dataset):
    means = []
    for data in dataset:
        means.append(sum(data) / len(data))
    return means


if __name__ == "__main__":
    path = ("2024 RPCN imu calibration/")
    # measurement_order = ['z', 'y', 'x']
    files = find_files(path)
    data = extract_information(files)
    averages = calculate_averages(data)
    print("Done")

