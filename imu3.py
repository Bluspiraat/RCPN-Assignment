import os
import numpy as np
from pathlib import Path
import pandas as pd

# Constants
# g = 9.80665
g = 9.8126
gyro_scaling = 2 * 0.0042 * np.sin(0.9117)  # Adjusted for latitude of Enschede

def extract_information(file):
    x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro = [], [], [], [], [], []

    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line and line[0].isdigit():
                split_line = line.split()
                numeric_values = [float(entry) for entry in split_line[2:]]
                z_acc.append(numeric_values[2])
                z_gyro.append(numeric_values[5])
                y_acc.append(numeric_values[1])
                y_gyro.append(numeric_values[4])
                x_acc.append(numeric_values[0])
                x_gyro.append(numeric_values[3])
    return [x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro]

def calc_average(file):
    data = extract_information(file)
    return {
        'x_acc': np.mean(data[0]),
        'y_acc': np.mean(data[1]),
        'z_acc': np.mean(data[2]),
        'x_gyro': np.mean(data[3]),
        'y_gyro': np.mean(data[4]),
        'z_gyro': np.mean(data[5])
    }

if __name__ == '__main__':
    data_folder = Path(__file__).parent.joinpath("data")
    files = list(data_folder.glob("MT_*.txt"))

    # Calculate averages for all files
    all_averages = {file.name[3:-4]: calc_average(file) for file in files}  # Removing MT_ and .txt

    # ACC Calibration
    b_acc_x_1 = (all_averages['XP1']['x_acc'] + all_averages['XN1']['x_acc']) / 2
    b_acc_y_1 = (all_averages['YP1']['y_acc'] + all_averages['YN1']['y_acc']) / 2
    b_acc_z_1 = (all_averages['ZP1']['z_acc'] + all_averages['ZN1']['z_acc']) / 2
    b_acc_x_2 = (all_averages['XP2']['x_acc'] + all_averages['XN2']['x_acc']) / 2
    b_acc_y_2 = (all_averages['YP2']['y_acc'] + all_averages['YN2']['y_acc']) / 2
    b_acc_z_2 = (all_averages['ZP2']['z_acc'] + all_averages['ZN2']['z_acc']) / 2
    b_acc_x_3 = (all_averages['XP3']['x_acc'] + all_averages['XN3']['x_acc']) / 2
    b_acc_y_3 = (all_averages['YP3']['y_acc'] + all_averages['YN3']['y_acc']) / 2
    b_acc_z_3 = (all_averages['ZP3']['z_acc'] + all_averages['ZN3']['z_acc']) / 2

    s_acc_x_1 = (all_averages['XP1']['x_acc'] - all_averages['XN1']['x_acc'] - 2*g) / (2*g)
    s_acc_y_1 = (all_averages['YP1']['y_acc'] - all_averages['YN1']['y_acc'] - 2*g) / (2*g)
    s_acc_z_1 = (all_averages['ZP1']['z_acc'] - all_averages['ZN1']['z_acc'] - 2*g) / (2*g)
    s_acc_x_2 = (all_averages['XP2']['x_acc'] - all_averages['XN2']['x_acc'] - 2*g) / (2*g)
    s_acc_y_2 = (all_averages['YP2']['y_acc'] - all_averages['YN2']['y_acc'] - 2*g) / (2*g)
    s_acc_z_2 = (all_averages['ZP2']['z_acc'] - all_averages['ZN2']['z_acc'] - 2*g) / (2*g)
    s_acc_x_3 = (all_averages['XP3']['x_acc'] - all_averages['XN3']['x_acc'] - 2*g) / (2*g)
    s_acc_y_3 = (all_averages['YP3']['y_acc'] - all_averages['YN3']['y_acc'] - 2*g) / (2*g)
    s_acc_z_3 = (all_averages['ZP3']['z_acc'] - all_averages['ZN3']['z_acc'] - 2*g) / (2*g)

    # Gyro Calibration
    b_gyro_x_1 = (all_averages['XP1']['x_gyro'] + all_averages['XN1']['x_gyro']) / 2
    b_gyro_y_1 = (all_averages['YP1']['y_gyro'] + all_averages['YN1']['y_gyro']) / 2
    b_gyro_z_1 = (all_averages['ZP1']['z_gyro'] + all_averages['ZN1']['z_gyro']) / 2
    b_gyro_x_2 = (all_averages['XP2']['x_gyro'] + all_averages['XN2']['x_gyro']) / 2
    b_gyro_y_2 = (all_averages['YP2']['y_gyro'] + all_averages['YN2']['y_gyro']) / 2
    b_gyro_z_2 = (all_averages['ZP2']['z_gyro'] + all_averages['ZN2']['z_gyro']) / 2
    b_gyro_x_3 = (all_averages['XP3']['x_gyro'] + all_averages['XN3']['x_gyro']) / 2
    b_gyro_y_3 = (all_averages['YP3']['y_gyro'] + all_averages['YN3']['y_gyro']) / 2
    b_gyro_z_3 = (all_averages['ZP3']['z_gyro'] + all_averages['ZN3']['z_gyro']) / 2

    s_gyro_x_1 = (all_averages['XP1']['x_gyro'] - all_averages['XN1']['x_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_y_1 = (all_averages['YP1']['y_gyro'] - all_averages['YN1']['y_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_z_1 = (all_averages['ZP1']['z_gyro'] - all_averages['ZN1']['z_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_x_2 = (all_averages['XP2']['x_gyro'] - all_averages['XN2']['x_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_y_2 = (all_averages['YP2']['y_gyro'] - all_averages['YN2']['y_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_z_2 = (all_averages['ZP2']['z_gyro'] - all_averages['ZN2']['z_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_x_3 = (all_averages['XP3']['x_gyro'] - all_averages['XN3']['x_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_y_3 = (all_averages['YP3']['y_gyro'] - all_averages['YN3']['y_gyro'] - gyro_scaling) / gyro_scaling
    s_gyro_z_3 = (all_averages['ZP3']['z_gyro'] - all_averages['ZN3']['z_gyro'] - gyro_scaling) / gyro_scaling

    # Data Summary
    data = {
        "Sensor_Axis": ["Acc_X", "Acc_Y", "Acc_Z", "Gyro_X", "Gyro_Y", "Gyro_Z"],
        "Bias_Run_1": [b_acc_x_1, b_acc_y_1, b_acc_z_1, b_gyro_x_1, b_gyro_y_1, b_gyro_z_1],
        "Scale_Run_1": [s_acc_x_1, s_acc_y_1, s_acc_z_1, s_gyro_x_1, s_gyro_y_1, s_gyro_z_1],
        "Bias_Run_2": [b_acc_x_2, b_acc_y_2, b_acc_z_2, b_gyro_x_2, b_gyro_y_2, b_gyro_z_2],
        "Scale_Run_2": [s_acc_x_2, s_acc_y_2, s_acc_z_2, s_gyro_x_2, s_gyro_y_2, s_gyro_z_2],
        "Bias_Run_3": [b_acc_x_3, b_acc_y_3, b_acc_z_3, b_gyro_x_3, b_gyro_y_3, b_gyro_z_3],
        "Scale_Run_3": [s_acc_x_3, s_acc_y_3, s_acc_z_3, s_gyro_x_3, s_gyro_y_3, s_gyro_z_3],
    }

    # Create DataFrame and Calculate Averages
    df = pd.DataFrame(data)
    df["Bias_Average"] = np.mean(df[["Bias_Run_1", "Bias_Run_2", "Bias_Run_3"]], axis=1)
    df["Scale_Average"] = np.mean(df[["Scale_Run_1", "Scale_Run_2", "Scale_Run_3"]], axis=1)

    # Rearrange columns for clarity
    df_summary = df[[
        "Sensor_Axis",
        "Bias_Run_1", "Scale_Run_1",
        "Bias_Run_2", "Scale_Run_2",
        "Bias_Run_3", "Scale_Run_3",
        "Bias_Average", "Scale_Average",
    ]]

    # Save summaries to CSV
    df_summary.to_csv("imu_bias_scale_summary.csv", index=False)
    df_summary[["Sensor_Axis", "Bias_Average", "Scale_Average"]].to_csv("imu_bias_scale_averages_only.csv", index=False)

    print(df_summary)
    
    # Transpose the dataframe
    
    df_summary_transposed = df_summary.transpose()
    df_summary_transposed.insert(0, 'Column_Title', df_summary_transposed.index)

    # Round to 7 decimal places
    df_summary_transposed = df_summary_transposed.map(lambda x: round(x, 7) if isinstance(x, (int, float)) else x)

    # Write to CSV
    df_summary_transposed.to_csv('summary_transposed.csv', float_format='%.7f', index=False)
    
    
    print('Done')
    
    
    print(all_averages['XP1']['x_gyro'])
    print(all_averages['YP1']['y_gyro'])
    print(all_averages['ZP1']['z_gyro'])
    
    print(all_averages['XN1']['x_gyro'])
    print(all_averages['YN1']['y_gyro'])
    print(all_averages['ZN1']['z_gyro'])
