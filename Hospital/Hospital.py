class Patient(object):
    def __init__(self,id_number,patient_name,allergies,bed_number):
        self.id_number = id_number
        self.patient_name = patient_name
        self.allergies = allergies
        self.bed_number = bed_number

    def display(self):
        print " "
        print "Id Number:", self.id_number
        print "Patient Name:", self.patient_name
        print "Allergies:", self.allergies
        print "Bed Number:", self.bed_number
        print " "
        return self

patient1 = Patient(001,"Reginald Wallace","Mangostein and Durian","001")
patient2 = Patient(002,"Sean Connery","Alex Trebec","002")
patient3 = Patient(003,"Frank Sinatra","Rats","003")
patient4 = Patient(004,"Ricky Bobby","Going Slow","004")

class Hospital(object):
    def __init__(self,hosp_name,max_capacity):
        self.patients = []
        self.hosp_name = hosp_name 
        self.max_capacity = max_capacity
        self.capacity = 0
    
    def Admit(self,patient):
        if self.capacity > self.max_capacity:
            return self
        self.patients.append(patient)
        self.capacity += 1
        return self

    def Discharge(self,discharged):
        self.discharged = discharged
        self.patients.remove(discharged)
        return self

    def Display(self):
        for i in self.patients:
            i.display()
        return self

hospital1 = Hospital("JSON Hospital",15)
hospital1.Admit(patient1).Admit(patient2).Admit(patient3).Admit(patient4).Display()
# hosp_name.admit(patient1).admit(patient2).admit(patient3).admit(patient4).Display().Discharge(patient1).Display()