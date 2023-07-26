import streamlit as st

if 'openai_api_key' not in st.session_state:
	st.session_state.openai_api_key = ""
st.session_state.openai_api_key = st.secrets.openai.OPENAI_API_KEY

if 'serper_api_key' not in st.session_state:
	st.session_state.serper_api_key = ""
st.session_state.serper_api_key = st.secrets.serper.SERPER_API_KEY

st.set_page_config(page_title="AlmyAI", page_icon="🤖📝")
st.title("Welcome to :violet[AlmyAI]! 👋")
st.subheader("Meet Almy")
st.markdown(
  """
  Introducing [AlmyAI] 🚀! First of its kind, organizational tool designed to put the power of AI right in your hands 🔥! 
  AlmyAI is an autonomous AI agent built on top of existing LLM such as OpenAI. It is able to not only provide information but can complete tasks. 
  The initial rollout focuses on Salesforce commands.
  
    """
)
st.markdown(
  """
  **🔑 Links and Resources: [Salesforce](https://almalasers.my.salesforce.com)    |     [ShowPad](https://almalasers.showpad.biz)     |     [Other](https://google.com)**   
    
    """
)
st.divider()
st.header("Pages and Tools")
st.subheader("Agent 🤖📝")
st.markdown(
  """
  
  * Entrust your tasks to our autonomous AI agent! From executing simple requests to handling Salesforce commands and updates, our Task Agent is at your service. Let AI simplify your work!
  * References: [Salesforce](https://almalasers.my.salesforce.com)
  
  
  
  """
)
st.divider()
st.subheader("Web Search 🌐🔍")
st.markdown(
  """
  
  * Unleash the power of information with web search queries on any topic. Your gateway to the global knowledge base is right here! 
    
  
  """
)
st.divider()
st.subheader("Webscrape 🔗🌎")
st.markdown(
  """
  
  * Get to the heart of any web page content with our URL summarizer. Extract essential information from URLs in a snap!
  
  """
)
st.divider()
st.subheader("Text Q&A 📑🔖")
st.markdown(
  """
  
  * Turn lengthy text blurbs into concise summaries. Make sense of vast information with a glance using our text summarizer!
  
  """
)
st.divider()
st.subheader("Document Q&A 📄📊")
st.markdown(
  """
  
  * Upload and distill the essence of any document with our Document Summarizer. Never miss the key points again!

"""
)
st.divider()
st.subheader("Playground 🚀⚙️")
st.markdown(
  """
  
  * Take advantage of a tesing and development environment to identify any features! New experiemental featuers will be rolled out here. 
 
  """
)
st.divider()
#st.write("---")
