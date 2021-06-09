import json


def calculate_bmi(height, weight):
    return weight/height


def add_bmi_data(data):
    overweight_counter = 0
    for person_info in data:
        bmi = calculate_bmi(
            person_info['HeightCm']/100, person_info['WeightKg'])
        person_info['BMI'] = bmi
        if bmi < 18.4:
            person_info['BMI_Category'] = 'Underweight'
            person_info['Health_Risk'] = 'Malnutrition Risk'
        elif 18.5 < bmi < 24.9:
            person_info['BMI_Category'] = 'Normal Weight'
            person_info['Health_Risk'] = 'Low Risk'
        elif 25 < bmi < 29.9:
            person_info['BMI_Category'] = 'Overweight'
            person_info['Health_Risk'] = 'Enhanced Risk'
            overweight_counter += 1
        elif 30 < bmi < 34.9:
            person_info['BMI_Category'] = 'Moderately Obese'
            person_info['Health_Risk'] = 'Medium Risk'
        elif 35 < bmi < 39.9:
            person_info['BMI_Category'] = 'Severely Obese'
            person_info['Health_Risk'] = 'High Risk'
        elif bmi >= 40:
            person_info['BMI_Category'] = 'Very Severely Obese'
            person_info['Health_Risk'] = 'Very High Risk'

    output_dict = {
        'data': data,
        'no_of_overweight': overweight_counter
    }
    return output_dict


if __name__ == '__main__':
    output_data = add_bmi_data([
        {
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        },
        {
            "Gender": "Male",
            "HeightCm": 161,
            "WeightKg": 85
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 77
        },
        {
            "Gender": "Female",
            "HeightCm": 166,
            "WeightKg": 62
        },
        {
            "Gender": "Female",
            "HeightCm": 150,
            "WeightKg": 70
        },
        {
            "Gender": "Female",
            "HeightCm": 167,
            "WeightKg": 82
        }
    ])
    print(output_data)
