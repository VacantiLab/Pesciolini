def TextToCM(text,CM):
    #This function reads information on CM from a string of text
    #The notation of the text is provided in the example file and is as follows:
    #    O[7 2.4 8; 9 4 2; 2 0 6], N[7 2.4 8; 9 4 2; 2 0 6], C[7 2.4 8; 9 4 2; 2 0 6]
    #    Will be read as a dictionary with keys for 'O', 'N', and 'C'
    #        The correction matrices will be numpy arrays with multiple rows separated by the semicolons

    import numpy as np
    import pandas
    from pdb import set_trace

    text_split = text.split(',')
    n_entries = len(text_split)

    for entry in text_split:
        entry = entry.strip()
        atom = entry[0]
        matrix = entry[2:-1]
        rows = matrix.split(';')
        dict_placeholder = dict()
        i = 1
        for row in rows:
            row = row.strip()
            dict_placeholder[i] = np.fromstring(row,sep=' ')
            i = i+1
        CM[atom] = pandas.DataFrame(dict_placeholder)
        CM[atom] = pandas.DataFrame.transpose(CM[atom])
        CM[atom] = np.asarray(CM[atom])

    return(CM)
