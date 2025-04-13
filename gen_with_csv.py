import matplotlib.pyplot as plt
import numpy as np
import os
import csv

def draw_clock(hour, minute, save_path):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.axis('off')

    # Clock face
    circle = plt.Circle((0, 0), 1, fill=False, linewidth=4)
    ax.add_artist(circle)

    for i in range(60):
        angle = np.deg2rad(6 * i)
        x_out, y_out = np.cos(angle), np.sin(angle)
        if i % 5 == 0:
            x_in, y_in = 0.85 * x_out, 0.85 * y_out
            lw = 2
        else:
            x_in, y_in = 0.92 * x_out, 0.92 * y_out
            lw = 1
        ax.plot([x_in, x_out], [y_in, y_out], color='black', lw=lw)

    minute_angle = np.deg2rad(90 - 6 * minute)
    ax.plot([0, 0.85 * np.cos(minute_angle)],
            [0, 0.85 * np.sin(minute_angle)], color='blue', lw=2)

    hour_angle = np.deg2rad(90 - 30 * (hour % 12) - 0.5 * minute)
    ax.plot([0, 0.5 * np.cos(hour_angle)],
            [0, 0.5 * np.sin(hour_angle)], color='black', lw=4)

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')

    filename = f'clock_{hour:02d}_{minute:02d}.png'
    filepath = os.path.join(save_path, filename)
    fig.savefig(filepath, bbox_inches='tight')
    plt.close()

    return filename, f'{hour:02d}:{minute:02d}'  # 👈 For CSV

def generate_all_clocks(output_folder='clocks', csv_file='analog_clock.csv'):
    os.makedirs(output_folder, exist_ok=True)
    rows = []

    for hour in range(12):
        for minute in range(60):
            img_filename, time_label = draw_clock(hour, minute, output_folder)
            img_tag = f'<img src="{img_filename}">'
            rows.append([img_tag, time_label])

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Front', 'Back'])  # Optional header
        writer.writerows(rows)

    print(f'All clock images saved to "{output_folder}/"')
    print(f'CSV saved as "{csv_file}" with {len(rows)} cards')

generate_all_clocks()