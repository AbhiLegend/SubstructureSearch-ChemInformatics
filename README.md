## The Full Flow

Streamlit application to demonstrate the functionality of substructure search within molecules using SMILES (Simplified Molecular Input Line Entry System) strings and SMARTS (SMiles ARbitrary Target Specification) patterns. Here's a step-by-step breakdown of what the code does:

Imports Necessary Libraries:

streamlit for creating the web application interface.
rdkit.Chem and related modules for chemical informatics functions, including molecule rendering.
base64 and io.BytesIO for encoding the generated molecule images into a format that can be displayed in the web app.
Defines a Function to Draw a Molecule with Highlighted Substructure:

draw_molecule(smiles, smarts) takes two arguments: a SMILES string representing the molecule and a SMARTS pattern representing the substructure to search for within the molecule.
It first converts the SMILES string to a molecular object. If the SMILES string is invalid, it returns an error message.
It then checks if the molecule contains the substructure defined by the SMARTS pattern. If not, it returns a message indicating the substructure wasn't found.
If the substructure is found, it highlights the matching atoms in the molecule and renders the molecule as an SVG (Scalable Vector Graphics) image.
Defines a Function to Encode SVG Content for HTML Display:

svg_to_base64(svg_content) converts the SVG string of the drawn molecule into a base64-encoded string. This encoding is necessary to embed the SVG directly into the HTML of the Streamlit app for display.
Sets Up the Streamlit User Interface:

Displays a title for the web app.
Provides text input fields for users to enter a SMILES string and a SMARTS pattern.
When both inputs are provided, it attempts to draw the molecule with the specified substructure highlighted. If successful, it displays the image in the app. If there's an error (e.g., invalid SMILES or the substructure is not found), it displays an appropriate error message.
Display Logic:

If the drawing is successful, the SVG content is converted to base64 and embedded in an <img> tag, which is then displayed in the Streamlit app using st.markdown() with the option unsafe_allow_html=True to allow HTML content.
If the inputs are not valid or the substructure is not found, it displays an error message using st.error().
Overall, this code provides an interactive way for users to visualize molecules and substructures directly within a web application, leveraging the powerful cheminformatics capabilities of RDKit and the user-friendly interface of Streamlit.
