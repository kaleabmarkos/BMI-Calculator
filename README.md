# BMI-Calculator

BMI (Body Mass Index) calculator implemented using the Tkinter library in Python. Here's a section-by-section description:

Imports:

tkinter: GUI toolkit for creating the application's graphical interface.
PIL (Python Imaging Library): Used for handling images.
Image, ImageTk from PIL: Specifically used to load and display images within the GUI.
Initialization:

Initializes the Tkinter window with specific attributes like title, size, position, and background color.
Creates a function BMI() to calculate BMI based on height and weight input and displays corresponding messages.
GUI Elements:

Sets an icon for the window and displays images (top, boxes, scale) within the application.
Creates sliders using ttk.Scale for inputting height and weight, with corresponding functions to handle slider changes.
Utilizes Entry widgets for users to input height and weight values.
Slider Functionality:

Slider controls are implemented to mimic the height and weight of a figure displayed in an image.
As the user adjusts the sliders, the displayed figure's size changes accordingly to represent the input values.
Button and Labels:

A button labeled "View Report" triggers the BMI calculation function.
Labels are used to display the calculated BMI value, the BMI category (e.g., Underweight, Normal, Overweight, Obese), and a description of the BMI category.

Main Loop:

Starts the main event loop to run the Tkinter application.
The code uses Tkinter's capabilities to create a graphical interface for a BMI calculator, allowing users to 
input their height and weight through sliders or entry boxes. The calculated BMI is displayed, along with a 
corresponding category and description to indicate the user's body weight status. The interface also incorporates
images to visually represent the BMI changes based on the provided inputs.
