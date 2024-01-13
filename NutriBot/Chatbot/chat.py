
import openai
from apikey import APIKEY
openai.api_key = APIKEY

question = input()
output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "system", "content": "You are a medical expert, who is professional in providing suggestions in mental health, diet and exercise."},
      {"role": "user", "content": "Give me a detailed advice, including analysis of data, diet improvements, exercise suggestions and other additional deductions based on given information point vice- Patient Information : Heart Rate at the moment: 90 BPM Average Heart Rate from the Week: 95 BPM Time of Highest Heart Rate: 110 BPM(4:00 AM) Weight: 90 kg Age: 20 years Medical History: Asthma Glucose Level : 105 Sp O2 : 99"}]
)
# Get the output text only
print(output['choices'][0]['message']['content'])