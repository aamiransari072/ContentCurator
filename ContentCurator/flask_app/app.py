
from flask import Flask, request , jsonify
import os
from ContentCurator.flask_app.utils import get_data , llm_response

# Load environment variables from .env file

app = Flask(__name__)
@app.route('/', methods=['POST'])
def home():
    user_input = request.get_json('num')
    return jsonify({'result':user_input})
@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    # get the data/query from streamlit app
    user_input = request.json.get('query')
    print("Received query: ", user_input)
    
    # Step 1: Search and scrape articles based on the query
    print("Step 1: searching articles")
    retrieve_data = get_data(user_input)
    print(f'Retrived Data: {retrieve_data}')
    

    if not retrieve_data:  # Handle case where no data is retrieved
        return jsonify({"error": "No data found for the query."}), 400
    
    # print(f"Retrieved Data: {retrieve_data}")


    # Step 2: Concatenate content from the scraped articles
    # print("Step 2: concatenating content")

    # Step 2: Generate an answer using the LLM
    print("Step 2: generating answer")
    response = llm_response(data=retrieve_data,query=user_input)

    print(f"LLM's Resposne: {response}")


    # return the jsonified text back to streamlit
    return jsonify({"response":response})

if __name__ == '__main__':
    app.run(debug=True,host='localhost', port=5000)
