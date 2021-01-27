import matplotlib.pyplot as plt
from shutil import copyfile

try:
    weekly_minutes = []
    dates = []
    with open("data.txt", "r") as f:
        file_chunks = f.read().split("\n")
        if len(file_chunks) <= 7:
            for line in file_chunks:
                data_info = line.split(", ")
                weekly_minutes.append(int(data_info[0]))
                dates.append(data_info[1])
        else:
            for line in file_chunks[:-7]:
                data_info = line.split(", ")
                weekly_minutes.append(int(data_info[0]))
                dates.append(data_info[1])
    plt.figure()
    plt.plot(dates, weekly_minutes)

    plt.xlabel("Date")
    plt.ylabel("Excercise Minutes")
    plt.title("Weekly Data")

    plt.savefig('weekly_chart.png')
except:
    copyfile("no_data.png", "weekly_chart.png")