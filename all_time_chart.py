import matplotlib.pyplot as plt
from shutil import copyfile

try:
    all_time_minutes = []
    dates = []
    with open("data.txt", "r") as f:
        file_chunks = f.read().split("\n")
        for line in file_chunks:
            data_info = line.split(", ")
            all_time_minutes.append(int(data_info[0]))
            dates.append(data_info[1])
    plt.figure()
    plt.plot(dates, all_time_minutes)

    plt.xlabel("Date")
    plt.ylabel("Exercise Minutes")
    plt.title("All Time Data")

    plt.savefig('all_time_chart.png')
except:
    copyfile("no_data.png", "all_time_chart.png")