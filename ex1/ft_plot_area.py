def ft_plot_area():
    "ft_plot_area that asks for length and width, then calculates and displays the area."
    length = input("Enter length: ")
    length = int(length)
    width = input("Enter width: ")
    width = int(width)
    print("Plot area:", length * width)

ft_plot_area()