import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Flight Price Predictor')


# Add some introductory text
st.write('This is a simple Streamlit app to get you started.')

# Add a text input widget
user_input = st.text_input('Enter some text:')

# Display the input text
st.write('You entered:', user_input)

# Add a slider widget
slider_value = st.slider('Select a value:', 0, 100, 50)

# Display the slider value
st.write('Slider value:', slider_value)

# Generate some random data
data = np.random.randn(100, 2)
df = pd.DataFrame(data, columns=['x', 'y'])

# Display the dataframe
st.write('Here is a random dataframe:')
st.dataframe(df)

# Create a simple plot
fig, ax = plt.subplots()
ax.scatter(df['x'], df['y'])
ax.set_title('Random Scatter Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Display the plot
st.pyplot(fig)

# Add a button
if st.button('Click me'):
    st.write('Button clicked!')

# Add a checkbox
if st.checkbox('Show more info'):
    st.write('Here is some more information...')

# Add a selectbox
option = st.selectbox(
    'Choose an option:',
    ['Option 1', 'Option 2', 'Option 3']
)

st.write('You selected:', option)
