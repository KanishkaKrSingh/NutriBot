import openai

openai.api_key = "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"

def generate_response(avg, t_high, height, weight, age, glv, spo, his):

    data = f'''Patient Information :
            BPM Average Heart Rate from the Week: {avg}
            Time of Highest Heart Rate: {t_high}
            Height: {height}
            Weight: {weight}
            Age: {age}
            Medical History: {his} 
            Glucose Level : {glv}
            Sp O2 : {spo}'''

    response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="You are a medical expert, who is professional in providing suggestions in mental health, diet and exercise.Give me a detailed advice, including analysis of data, diet improvements, exercise suggestions and other additional deductions based on given information point vice- " + data,
    max_tokens=1000,
    temperature=0.7,
    )

    return response.choices[0].text.strip()

generate_response(95, '4:00AM 120 BPM ', 166, 90, 19, 105, 99, 'Asthma', )