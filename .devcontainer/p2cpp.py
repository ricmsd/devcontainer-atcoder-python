import os
import subprocess
import sys
import openai

# TODO:
# - Corresponding to the latest models
# - Improve log output
# - Error handling

input_py = sys.argv[1]
output_cpp = sys.argv[2]

openai.api_key = os.environ['OPENAI_API_KEY']
print(f'[INFO] read python file: {input_py}')
with open(input_py, "r") as file:
    python_code = file.read()

model = "text-davinci-003"
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

print(f'[INFO] write C++ file: {output_cpp}')
cpp_code = response.choices[0].text.strip()
with open(output_cpp, "w") as file:
    file.write(cpp_code)

print(f'[INFO] compile {output_cpp} by g++')
result = subprocess.run(f"g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE -o ./a.out {output_cpp}".split())
if result.returncode != 0:
    print(f'[ERROR] compile failed: g++ exit status={result.returncode}')
    exit(1)

print(f'[INFO] output execution file: a.out')
