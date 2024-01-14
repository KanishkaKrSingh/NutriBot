from django.shortcuts import render
import openai

openai.api_key = "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"

def generate_response(data):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"You are a medical expert, who is professional in providing suggestions in mental health, diet and exercise. Give me a detailed advice, including analysis of data, diet improvements, exercise suggestions, and other additional deductions based on given information point vice - {data}",
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def chat_view(request):
    if request.method == 'POST':
        # Extract all form inputs
        avg = request.POST.get('avg', '')
        t_high = request.POST.get('t_high', '')
        height = request.POST.get('height', '')
        weight = request.POST.get('weight', '')
        age = request.POST.get('age', '')
        glv = request.POST.get('glv', '')
        spo = request.POST.get('spo', '')
        his = request.POST.get('his', '')

        # Combine all inputs into a single string, separated by space or any character you prefer
        data = f'{avg} {t_high} {height} {weight} {age} {glv} {spo} {his}'

        # Get chat history from the form or initialize if not present
        chat_history = request.POST.get('chat_history', '')

        # Append the new user input to the chat history
        chat_history += f'\nUser: {data}'

        # Generate the response based on the combined data
        response = generate_response(data)

        # Append the response to the chat history
        chat_history += f'\nChatBot: {response}'

        return render(request, 'chatapp/chat.html', {'chat_history': chat_history})

    return render(request, 'chatapp/chat.html', {'chat_history': ''})
