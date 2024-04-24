import matplotlib.pyplot as plt
import datetime

class HeartData:
    def __init__(self):
        self.systolic = []
        self.diastolic = []
        self.heartbeats = []
        self.times = []

    def add_data(self, systolic, diastolic, heartbeats, time_str):
        self.times.append(time_str)
        self.systolic.append(systolic)
        self.diastolic.append(diastolic)
        self.heartbeats.append(heartbeats)

    def plot_blood_pressure(self):
        plt.scatter(self.times, self.systolic, label='Systolic', color='red')
        plt.scatter(self.times, self.diastolic, label='Diastolic', color='blue')
        plt.plot(self.times, self.systolic, linestyle='-', color='red')  # Connect the dots with a line
        plt.plot(self.times, self.diastolic, linestyle='-', color='blue')  # Connect the dots with a line
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Pressure')
        plt.title('Blood Pressure Over Time')
        plt.legend()
        plt.show()

    def plot_heart_rate(self):
        plt.scatter(self.times, self.heartbeats, label='Heartbeats', color='green')
        plt.plot(self.times, self.heartbeats, linestyle='-', color='green')  # Connect the dots with a line
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Heartbeats')
        plt.title('Heart Rate Over Time')
        plt.legend()
        plt.show()

# Example usage:
heart_data = HeartData()

# Adding some data points
heart_data.add_data(120, 80, 70, "10:00")  # Systolic, Diastolic, Heartbeats, Time
heart_data.add_data(115, 78, 72, "10:15")
heart_data.add_data(125, 82, 68, "10:30")

# Plotting
heart_data.plot_blood_pressure()
heart_data.plot_heart_rate()
