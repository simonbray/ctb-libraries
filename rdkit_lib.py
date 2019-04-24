from rdkit.Chem.rdmolfiles import MolFromMolFile, MolFromMol2File, MolFromSmiles, MolFromPDBFile, SDMolSupplier, SmilesMolSupplier

def mol_supplier(filename, ext):
    """
    Based on the file extension, use the appropriate RDKit function to
    load a chemical data file (SMILES or SDF) containing multiple molecules
    and return a list of RDKit Mol objects
    """
    Supplier = {'smi': SmilesMolSupplier, 'sdf': SDMolSupplier}
    return [n for n in Supplier(filename)]

def load_file_to_mol(filename, ext):
    """
    Based on the file extension, use the appropriate RDKit function to load
    a chemical data file containing a single molecule as a RDKit Mol object
    """
    MolFrom = {'smi': MolFromSmiles, 'mol': MolFromMolFile, 'mol2': MolFromMol2File, 'pdb': MolFromPDBFile}
    if ext == 'sdf':
        return mol_supplier(filename, 'sdf')[0]
    return MolFrom[ext](filename)