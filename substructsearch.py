import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
import base64
from io import BytesIO

# Function to draw a molecule with highlighted substructure and return SVG as a string
def draw_molecule(smiles, smarts):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:  # Check if the SMILES string is valid
        return "Invalid SMILES string.", False
    patt = Chem.MolFromSmarts(smarts)
    if not mol.HasSubstructMatch(patt):  # Check if the substructure is found
        return "Substructure not found in molecule.", False
    hit_atoms = list(mol.GetSubstructMatch(patt))
    d = rdMolDraw2D.MolDraw2DSVG(400, 400)
    rdMolDraw2D.PrepareAndDrawMolecule(d, mol, highlightAtoms=hit_atoms)
    d.FinishDrawing()
    svg = d.GetDrawingText()
    svg = svg.replace('svg:', '')  # Remove 'svg:' prefix if present
    return svg, True

# Function to encode SVG content for HTML display
def svg_to_base64(svg_content):
    encoded = base64.b64encode(svg_content.encode('utf-8')).decode("utf-8")
    return f"data:image/svg+xml;base64,{encoded}"

# Streamlit UI
st.title('SMARTS Substructure Search in Molecules')
smiles_input = st.text_input('Enter SMILES:', 'c1ccccc1O')
smarts_input = st.text_input('Enter SMARTS:', '[OH]')

if smiles_input and smarts_input:
    svg_content, success = draw_molecule(smiles_input, smarts_input)
    if success:
        base64_data = svg_to_base64(svg_content)
        st.markdown(f'<img src="{base64_data}" alt="Molecule" style="max-width: 100%; height: auto;">', unsafe_allow_html=True)
    else:
        st.error(svg_content)
else:
    st.write("Please enter both SMILES and SMARTS patterns.")
