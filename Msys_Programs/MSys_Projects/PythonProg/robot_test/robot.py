class Robot:
    def __init__(self, name, battery, skills=[]):
        self.name = name
        self.battery = battery
        self.skills = skills

    def charge(self):
        self.battery = 100
        return self
    
    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"BEEP BOOP BEEP BOOP. I AM {self.name.upper()}"
        return "Low power. Please charge and try again"
    
    def learn_skil(self, new_skills, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.skills.append(new_skills)
            return f"WHAH. I KNOW {NEW_SKILL.upper()}"
        return "Insufficient battery. Please charge and try again"