import os
import subprocess
import sys
import openai

# TODO:
# - Improve log output
# - Error handling

def chat_completion(model: str, python_code: str) -> str:
    """
    chat completion for gpt-4, gpt-4-0314, gpt-4-32k, gpt-4-32k-0314, gpt-3.5-turbo, gpt-3.5-turbo-0301	
    """
    print(f'[INFO] call openai API and wait response: model={model}')
    prompt = f"Please convert the following Python code to C++ code:\n\n{python_code}\n\nC++ code:\n"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=2000,
    )
    return response.choices[0].message['content'].strip()

def completion(model: str, python_code: str) -> str:
    """
    completion for text-davinci-003, text-davinci-002, text-curie-001, text-babbage-001, text-ada-001, davinci, curie, babbage, ada
    """
    print(f'[INFO] call openai API and wait response: model={model}')
    prompt = f"Please convert the following Python code to C++:\n\n{python_code}\n"
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def convert_python_to_cpp(model: str, python_code: str) -> str:
    if model in ["gpt-4", "gpt-4-0314", "gpt-4-32k", "gpt-4-32k-0314", "gpt-3.5-turbo", "gpt-3.5-turbo-0301"]:
        return chat_completion(model, python_code)
    elif model in ["text-davinci-003", "text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001", "davinci", "curie", "babbage", "ada"]:
        return completion(model, python_code)
    raise Exception(f"unknown model: {model}")

model = sys.argv[1]
input_py = sys.argv[2]
output_cpp = sys.argv[3]

openai.api_key = os.environ['OPENAI_API_KEY']
print(f'[INFO] read python file: {input_py}')
with open(input_py, "r") as file:
    python_code = file.read()

cpp_code = convert_python_to_cpp(model, python_code)
print(f'[INFO] write C++ file: {output_cpp}')
with open(output_cpp, "w") as file:
    file.write(cpp_code)

print(f'[INFO] compile {output_cpp} by g++')
result = subprocess.run(f"g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE -o ./a.out {output_cpp}".split())
if result.returncode != 0:
    print(f'[ERROR] compile failed: g++ exit status={result.returncode}')
    exit(1)

print(f'[INFO] output execution file: a.out')
