'''employee_data = :{ 
"priya":{ 
"location" 
}, 
"mahi": { 
: "Hyderabad" "joining_date": "05/09/2022" 
"location" : "Bangalore" 
"joining_date":"20/02/2023" 
}, 
"raja": { 
"location" 
"Hyderabad" 
"joining_date": "14/10/2022" 
}, 
"prabhu":{ 
"location" 
: "Bangalore" 
"joining_date": "02/01/2023” 
} 
} '''

empIoyee_data = {"priya":{"location" : "Hyderabad","joining_date" : "05/09/2022"},
                    "mahi":{"location" : "Bangalore","joining_date": "20/02/2023"},
                    "raja":{"location" : "Hyderabad","joining_date": "14/10/2022"},
                    "prabhu":{"location" : "Bangalore","joining_date": "02/01/2023"}
                }

for employee_name, employee_details in empIoyee_data.items():
    if employee_details["location"]=="Hyderabad" and employee_details["joining_date"] > "02/09/2022":
        print(employee_name)
