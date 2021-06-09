import unittest
import script


class TestScript(unittest.TestCase):

    def test_result_contains_overweight_count(self):
        """ 
            To test that the output contains overweight count data
        """
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        result = script.add_bmi_data(data)
        self.assertIn('no_of_overweight', result)

    def test_result_contains_bmi(self):
        '''
            To test that the output contains bmi data
        '''
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        result = script.add_bmi_data(data)
        self.assertIn('BMI', result['data'][0])

    def test_bmi_calculation(self):
        '''
            To test that the output contains bmi data
        '''
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        calculated_bmi = data[0]['WeightKg']/(data[0]['HeightCm']/100)
        result = script.add_bmi_data(data)
        self.assertEqual(calculated_bmi, result['data'][0]['BMI'])

    def test_result_contains_bmi_category(self):
        '''
            To test that the output contains bmi data
        '''
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        result = script.add_bmi_data(data)
        self.assertIn('BMI_Category', result['data'][0])

    def test_result_contains_health_risk(self):
        '''
            To test that the output contains bmi data
        '''
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        result = script.add_bmi_data(data)
        self.assertIn('Health_Risk', result['data'][0])

    def test_corresponding_health_risk(self):
        '''
            To test that the output contains bmi data
        '''
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        result = script.add_bmi_data(data)
        self.assertIn('Very High Risk', result['data'][0]['Health_Risk'])

    def test_corresponding_bmi_category(self):
        '''
            To test that the output contains bmi data
        '''
        data = [{
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96
        }]
        result = script.add_bmi_data(data)
        self.assertIn('Very Severely Obese', result['data'][0]['BMI_Category'])


if __name__ == '__main__':
    unittest.main()
