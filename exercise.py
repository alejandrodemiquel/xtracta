import pandas as pd

def read_invoice(invoice_path=None):
    """
    Read the file with the relevant information about the invoice. That
    information is stored in the file given by invoice_path. The file has to be
    a jsonl file.
    If no input is specicfied, the function will read the file given for the
    exercise.
    """
    if invoice_path==None:
        return pd.read_json("preprocessed_files/invoice.jsonl", lines=True)
    else:
        return pd.read_json(invoice_path)
        
def read_supplier_names(suppliers_path=None):
    """
    Read the file that lists the supplier names. The file is stored in the 
    file given by suppliers_path. The file has to be a csv file.
    If no input is specicfied, the function will read the file given for the
    exercise.
    """
    if suppliers_path==None:
        return pd.read_csv("preprocessed_files/suppliernames.csv")
    else:
        return pd.read_csv(suppliers_path)

def get_supplier_from_invoice(invoice, supplier_names):
    """
    Given a list of suppliers and the information about an invoice, this
    function returns the name of the supplier appearing in the invoice.
    ...
    Parameters
    ----------
    invoice: pandas.DataFrame
        An object containing all the information about the words appearing in 
        the invoice. It has to contain the columns "page_id", "line_id",
        "pos_id" and "word".
    supplier_names: pandas.DataFrame
        An object containing all the possible supplier names. It has to contain
        the column "SupplierName".
    ...
    Returns
    -------
    str: The supplier name that appears in the invoice. If no supplier name is
    found, the function returns None.
    """
    # Set of the words that appear in the invoice
    word_set = set(invoice.word.values)

    # For every supplier, check whether its name appears in the invoice by
    # checking that its words appear one after the other, in the correct order.     
    for supplier in supplier_names.SupplierName.values:
        words = supplier.split()
        if set(words).issubset(word_set):
            # Create a dataframe for every word in the supplier's name encoding
            # the information about all its appearances in the invoice.
            word_df = []
            for word in words:
                word_df.append(invoice.loc[invoice['word'] == word])
            
            # For every time that the first word of the supplier name appears
            # in the invoice, check if the rest comes right after it.
            for index, row in word_df[0].iterrows():
                page = row.page_id
                line = row.line_id
                position = row.pos_id
                match_found = True
                for i in range(1, len(words)):
                    if word_df[i].loc[(word_df[i].page_id == page) & \
                                      (word_df[i].line_id == line) & \
                                      (word_df[i].pos_id == position+i)].empty:
                        match_found = False
                        break
                # If we found a match, we can return the supplier name
                if match_found:
                    return supplier
    return None