import pickle

model=pickle.load(open("model.pkl","rb"))
vectorizer=pickle.load(open("vectorizer.pkl", "rb"))

def generate_prompt(user_input):
    input_vector = vectorizer.transform([user_input])
    return model.predict(input_vector)[0]