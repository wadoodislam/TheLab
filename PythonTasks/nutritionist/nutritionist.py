
def height_in_meters(feet, inches):
    f = float(feet)*0.305
    i = float(inches)*0.0254
    meters = f+i
    return meters


def weight_in_kgs(weight):
    w = float(weight)*0.45
    return w


def bmi_calculation( w, meters):
    bmi = w / (meters * meters)
    print("Your BMI is: ",round(bmi,2)," kg/m^2")


def bmr_calculations(gender, w, hcm, age):

    if gender == "female":
        bmr=(10*float(w))+(6.25*float(hcm))-(5*float(age))-161
    else:
        bmr = (10*float(w))+(6.25*float(hcm))-(5*float(age)+5)
    return bmr


def lean_body_mass(w , age, hcm, gender):
    if age < "14":
        ecm = 0.0125*(w**0.6469)*hcm-0.7236
        return ecm
    elif age > "14":

        if gender == "female":
            elbmf = 0.29569*w+0.42*hcm-43.2933
            return elbmf
        else:
            elbmm = 0.32810*w+0.33939*hcm-29.5336
            return elbmm


name = input('Enter your name: ')
age = input('Enter your age: ')
gender = input('Enter your gender (female/male): ')
weight = input('Enter weight in pounds: ')
feet, inch = input('Enter height feet-inches format').split(" ")
print("1: Body mass Index (BMI)\n2: Basal Metabolic rate (BMR)\n3:Lean Body Mass (LBM)\n0: Quit")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        h = height_in_meters(feet, inch)
        w = weight_in_kgs(weight)
        bmi_calculation(w, h)
    elif choice == "2":
        h = height_in_meters(feet, inch)
        hcm = h*100
        w = weight_in_kgs(weight)
        bmr = bmr_calculations(gender, w, hcm, age)
        print("Your BMR is: ", round(bmr, 2), " calories per day")

    elif choice == "3":
        w = weight_in_kgs(weight)
        h = height_in_meters(feet, inch)
        hcm = h * 100
        l = lean_body_mass(w, age, hcm, gender)
        print("your LBM is: ", round(l, 2), " lbs")
    elif choice == "0":
        break
    else:
        print("Not from the list")




