def hospital_expert_system():
    print("Welcome to the Hospital Department Expert System")
    print("Please answer the following questions with yes or no.\n")

    age_group = input("Are you under 12 years old? (yes/no) ").lower() == "yes"
    fever = input("Do you have a fever? ").lower() == "yes"
    cough = input("Do you have a cough? ").lower() == "yes"
    sore_throat = input("Do you have a sore throat? ").lower() == "yes"
    ear_pain = input("Do you have ear pain? ").lower() == "yes"
    chest_pain = input("Do you have chest pain? ").lower() == "yes"
    stomach_pain = input("Do you have stomach pain or diarrhea? ").lower() == "yes"
    skin_rash = input("Do you have any skin rash or itching? ").lower() == "yes"
    joint_pain = input("Do you have joint or bone pain? ").lower() == "yes"
    headache = input("Do you have a headache or dizziness? ").lower() == "yes"
    pregnant = input("Are you pregnant or facing menstrual issues? ").lower() == "yes"
    anxiety = input("Are you feeling anxious or depressed? ").lower() == "yes"
    blood_check = input("Check the Blood Group and assign lab").lower() == "yes"

    print("\n--- Suggested Department ---")

    if age_group:
        print("Suggested Department: Pediatrics")
    elif fever and cough and sore_throat:
        print("Suggested Department: General Medicine")
    elif ear_pain or sore_throat:
        print("Suggested Department: ENT (Ear, Nose, Throat)")
    elif chest_pain:
        print("Suggested Department: Cardiology")
    elif stomach_pain:
        print("Suggested Department: Gastroenterology")
    elif skin_rash:
        print("Suggested Department: Dermatology")
    elif joint_pain:
        print("Suggested Department: Orthopedics")
    elif headache:
        print("Suggested Department: Neurology")
    elif pregnant:
        print("Suggested Department: Gynecology")
    elif anxiety:
        print("Suggested Department: Psychiatry")
    else:
        print("Symptoms do not match a specific department.")
        print("Suggested Department: General OPD")

    print("\nThank you for using the Hospital Department Expert System.")

# Run the expert system
hospital_expert_system()
