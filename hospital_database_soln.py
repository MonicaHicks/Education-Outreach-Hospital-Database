import math 

AGE = 0
SEX = 1
DOB = 2
DISEASE = 3
DASHES = "--------------------------------------------"
WELCOME = "Welcome to the Hospital Database!"
MENU = "Add, Lookup, or Delete a patient? (type 'q' to quit): "

# This function will add a patient
def add_patient(hospital_database):

    # Obtain info on patient
   name = input("Full name of patient: ")
   age = input("Age: ")
   sex = input("Sex: ")
   dob = input("Date of birth: (MM/DD/YYYY): ")

   # The diagnose function will return a disease diagnosis
   # based on reported symptoms.
   # To ignore, comment out this line and uncomment line 25
   disease = diagnose()

   # disease = "None"

   # Put all patient info in to a list. This list will be 
   # accessed using constants AGE(0), SEX(1), DOB(2), 
   # and DISEASE(3). For that reason, order matters.
   patient_profile = [age, sex, dob, disease]

   # The hospital database is a dictionary where the 
   # patient's name is the key and the value is the list 
   # associated with their patient profile
   hospital_database[name] = patient_profile

   # Print success message
   print("\n" + name + " has been added to the database!")

   # Print list of all patients currently in the database
   print("Current patients on file:")
   for patient in hospital_database.keys():
       print(patient)
   print("\n")


# This code will take in the name of a patients and if
# found, print their name, age, sex, DOB, diagnosis
# Otherwise, it will print a not found message
def lookup_patient(hospital_database):
    patient = input("Name of the person you'd like to look up?\n")
    if patient in hospital_database.keys():
        profile = hospital_database[patient]
        print("Name: " + patient)
        print("Age: " + profile[AGE])
        print("Sex: " + profile[SEX])
        print("Date of birth: " + profile[DOB])
        print("Disease: " + profile[DISEASE])
    else:
        print("This patient doesn't exist")

# This code removes a patient from the hospital database
# or prints an error message if not found
def delete_patient(hospital_database):
    #   //remove patient
    patient = input("Name of the person you'd like to delete? ")
    if patient in hospital_database.keys():
        del hospital_database[patient]
        print(patient + " has been removed from the hospital database")
    else:
        print(patient + " is not in the hospital database")


def diagnose():
    symptoms = ["Bloating", "Coughing", "Diarrhea", "Dizziness", \
                "Fatigue", "Fever", "Headache", "Muscle Cramp", \
                "Nausea", "Throat Irritation"]
    medical_profile = []

    print("Begin confirming the patient's symptoms (1 for yes, 0 for no):")
    for i in range(len(symptoms)):
        print("Symptom " + str(i + 1) + ": " + symptoms[i])
        medical_profile.append(input("Experiencing symptom " + str(i + 1) + "? "))
    
    medical_profile = str_to_int(medical_profile)

    disease = evaluate_symptoms(medical_profile)

    return disease


def str_to_int(list):
    int_list = []
    for elem in list:
        int_list.append(int(elem))

    return int_list


def evaluate_symptoms(medical_profile):

    diagnosis = None
    my_dict = {}
    with open("disease_list.txt", 'r') as file:
        for line in file:
            line = line.strip()
            tokens = line.split(" - ")
            my_list = list(tokens[1].split(" "))
            my_list = str_to_int(my_list)
            my_dict[tokens[0]] = my_list

    closest = -1
    for key in my_dict.keys():
        result = cosine_sim(my_dict[key], medical_profile)
        if result > closest:
            diagnosis = key
            closest = result

    return diagnosis


def cosine_sim(disease, patient_info):
    
    numerator = 0

    for i in range(len(disease)):
        numerator += disease[i] * patient_info[i]

    disease_squared = [num ** 2 for num in disease]
    patient_info_squared = [num ** 2 for num in patient_info]

    denom = math.sqrt(sum(disease_squared)) * math.sqrt(sum(patient_info_squared))

    # you can assume there will be at least one symptom
    return numerator / denom



def main():
    
    hospital_database = {}
    print(WELCOME)
    while True:
        print(DASHES)
        control = input(MENU).upper()
        if control == "Q":
            return
        elif control == "LOOKUP":
            lookup_patient(hospital_database)
        elif control == "ADD":
            add_patient(hospital_database)
        elif control == "DELETE":
            delete_patient(hospital_database)

main()
