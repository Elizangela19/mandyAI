import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity

# Load the Universal Sentence Encoder model locally
def load_model():
    print("Loading Universal Sentence Encoder model...")
    model = tf.saved_model.load("./model/universal-sentence-encoder")
    print("Model loaded successfully.")
    return model

# Get the embeddings for the given sentences
def get_embeddings(model, sentences):
    return model(sentences)

# Function to return the best response based on user input
def get_best_response(model, user_input, responses):
    # Generate embeddings for the user input and predefined responses
    user_embedding = get_embeddings(model, [user_input])
    response_embeddings = get_embeddings(model, responses)

    # Calculate similarity
    similarities = cosine_similarity(user_embedding, response_embeddings)
    best_response_index = similarities.argmax(axis=1)[0]  # Best match index

    return responses[best_response_index]
