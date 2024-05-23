import google.generativeai as genai

# Retrieve the list of available models
models = genai.list_models()

# Filter for the base model that supports 'createTunedModel'
base_model = next((m for m in models if "createTunedModel" in m.supported_generation_methods), None)

# Print the base model details if found
# if base_model:
#     print(base_model)
# else:
#     print("No model supporting 'createTunedModel' found.")

def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_entry = {"text_input": "", "output": ""}
        for line in lines:
            line = line.strip()
            if line.startswith("# Context:"):
                if current_entry["text_input"]:
                    dataset.append(current_entry)
                    current_entry = {"text_input": "", "output": ""}
                current_entry["text_input"] = line.replace("# Context:", "").strip()
            elif line.startswith("# Question:"):
                current_entry["text_input"] += " " + line.replace("# Question:", "").strip()
            elif line.startswith("# Output:"):
                current_entry["output"] = line.replace("# Output:", "").strip()
            elif current_entry["text_input"]:
                current_entry["text_input"] += "\n" + line
        if current_entry["text_input"]:
            dataset.append(current_entry)
    return dataset

# dataset = read_dataset('Backend/Fine_Tune_Gemini/dataset.txt')

name = f'tuned-gemini-model'

# # List available models and select the base model
# models = genai.list_models()
# base_model = next((m for m in models if "createTunedModel" in m.supported_generation_methods), None)

# if base_model:
#     tuned_model = genai.create_tuned_model(
#         source_model=base_model.name,
#         id = name,
#         training_data=dataset,
#         epoch_count=100,
#         batch_size=1,
#         learning_rate=0.001,
#     )
#     print(tuned_model)  # Print the tuned model details
# else:
#     print("No suitable base model found to create a tuned model.")

tuned_model = genai.GenerativeModel(model_name=f'tunedModels/{name}')


# print(tuned_model)
# print(tuned_model.state)

response = tuned_model.generate_content('tell me about the update mapper endpoint and give a sample python code')
print(response.text)