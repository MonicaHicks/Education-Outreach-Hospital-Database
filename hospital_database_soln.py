import math 

AGE = 0
SEX = 1
DOB = 2
DISEASE = 3
DASHES = "--------------------------------------------"
WELCOME = "Welcome to the Hospital Database!"
MENU = "Add, Lookup, or Delete a patient? (type 'q' to quit): "

def add_patient(hospital_database):
   # // add someone
   name = input("Full name of patient:\n")
   age = input("Age:\n")
   sex = input("Sex:\n")
   dob = input("Date of birth: (MM/DD/YYYY):\n")
   disease = diagnose()
   patient_profile = [age, sex, dob, disease]
   hospital_database[name] = patient_profile

   print("\n" + name + " has been added to the database!")
   print("Current patients on file:")
   for patient in hospital_database.keys():
       print(patient)
   print("\n")


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

def delete_patient():
    #   //remove patient
    pass


def diagnose():
    symptoms = ["Bloating", "Coughing", "Diarrhea", "Dizziness", \
                "Fatigue", "Fever", "Headache", "Muscle Cramp", \
                "Nausea", "Throat Irritation"]
    medical_profile = []

    print("Begin confirming the patient's symptoms:")
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
        control = input(MENU)
        if control == "q":
            break
        elif control == "Lookup":
            lookup_patient(hospital_databse)
        elif control == "Add":
            add_patient(hospital_database)

#//    while(True):
 # //      print(DASHES)
  #  //    print(MENU)

main()
