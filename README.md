# Agentic-AI-project
In this project I have developed a single agent based system using langchain and pydantic.
The project takes user query as input through the terminal and uses provided tools like duckduckgo search engine and wikipedia for gaining information about the inputted topic. 
It lists the tools used and also sources like websites surfed for the task.
the output is formatted using a parser made available by Pydanctic's one of many libraries.
I have used langchain's many easy to use available functions to create my agent(like create_tool_calling_agent and AgentExecutor).

How to use/run locally:
1. Download all the files that I have uploaded in one same folder.
2. Open the folder using any IDE (I used VScode).
3. Create a .env file in the same folder and create a variable API_KEY = "your_api_key"(Enter key for whichever api you use, I used OpenAI's GPT-4o model)
4. As per the LLM selection change name of model in the main.py file.
5. I suggest creating a virtual environement to run it, as you will donwloading many libraries which are in the requirements file.
6. Once everything above is set up, run file in terminal and enter your query.

   For suggestions contact me at email: omkar1572003@gmail.com

If anyone is interested in adding newers tools and functionalities to this code, you can communicate and I will happy to add your changes/updates to the main branch after review of the code.

Thank you!
