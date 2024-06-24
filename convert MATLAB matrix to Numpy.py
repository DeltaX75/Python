def matlab_to_numpy(matlab_str):
    # Remove square brackets and split the string into rows
    matlab_str = matlab_str.strip('[]')
    rows = matlab_str.split(';')
    
    # Process each row to format it correctly for Python
    formatted_rows = []
    for row in rows:
        # Split each row by space and join with commas
        formatted_row = ', '.join(row.split())
        formatted_rows.append('[' + formatted_row + ']')
    
    # Join all formatted rows into a single string
    numpy_str = 'np.array([\n    ' + ',\n    '.join(formatted_rows) + '\n])'
    
    return numpy_str

# Example usage
matlab_input = "[0 2 0; 2 0 -5; 0 5 0]"
numpy_output = matlab_to_numpy(matlab_input)
print(numpy_output)
