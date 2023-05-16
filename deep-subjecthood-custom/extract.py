import pandas as pd

## This function takes a .conllu file as a string and prints
## out each bert layer

def print_layers(file):

    with open(file, "r", encoding="utf-8") as file:
        read_file = file.readlines()

    df = pd.DataFrame([sub.split(",") for sub in read_file])

    ## save the first row, select everything else, set columns to saved first row
    new_titles = df.iloc[0]
    df = df[1:]
    df.columns = new_titles
    df.rename(columns = {'source_test_accuracy_O\n': 'source_test_accuracy_O'}, inplace=True)
    df = df.replace(r'\n','', regex=True) 

    ## Print out each layer (12 at top) and append to a list

    results = []

    df_layer = df.loc[df['layer'] == '12']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_12 = list_layer[0]
    results.append(res_12)
    #print(f'Layer 12: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '11']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_11 = list_layer[0]
    results.append(res_11)
    #print(f'Layer 11: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '10']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_10 = list_layer[0]
    results.append(res_10)
    #print(f'Layer 10: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '9']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_9 = list_layer[0]
    results.append(res_9)
    #print(f'Layer 9: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '8']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_8 = list_layer[0]
    results.append(res_8)
    #print(f'Layer 8: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '7']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_7 = list_layer[0]
    results.append(res_7)
    #print(f'Layer 7: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '6']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_6 = list_layer[0]
    results.append(res_6)
    #print(f'Layer 6: {list_layer[0]}')


    df_layer = df.loc[df['layer'] == '5']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_5 = list_layer[0]
    results.append(res_5)
    #print(f'Layer 5: {list_layer[0]}')


    df_layer = df.loc[df['layer'] == '4']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_4 = list_layer[0]
    results.append(res_4)
    #print(f'Layer 4: {list_layer[0]}')


    df_layer = df.loc[df['layer'] == '3']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_3 = list_layer[0]
    results.append(res_3)
    #print(f'Layer 3: {list_layer[0]}')


    df_layer = df.loc[df['layer'] == '2']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_2 = list_layer[0]
    results.append(res_2)
    #print(f'Layer 2: {list_layer[0]}')

    df_layer = df.loc[df['layer'] == '1']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_1 = list_layer[0]
    results.append(res_1)
    #print(f'Layer 1: {list_layer[0]}')


    df_layer = df.loc[df['layer'] == '0']
    layer_values = df_layer[['source_test_accuracy_A', 'source_test_accuracy_O']]
    list_layer = layer_values.values.tolist()
    res_0 = list_layer[0]
    results.append(res_0)
    #print(f'Layer 0: {list_layer[0]}')

    return results


### Makes df to look at baseline, can be used with Prob_A and Prob_O
### for analyzing similarities

# Get 3 languages ready with prior function, for example:
#df_layers = pd.DataFrame(index=[0], columns=['English','German','French'])


#Making function where, once an empty dataframe is made, you can pass it
# and you'll be able to plot it

def add_to_df(dataframe_name,list_of_layers, column_name):
    
    dataframe_name.loc[0, column_name] = list_of_layers[12]
    dataframe_name.loc[1, column_name] = list_of_layers[11]
    dataframe_name.loc[2, column_name] = list_of_layers[10]
    dataframe_name.loc[3, column_name] = list_of_layers[9]
    dataframe_name.loc[4, column_name] = list_of_layers[8]
    dataframe_name.loc[5, column_name] = list_of_layers[7]
    dataframe_name.loc[6, column_name] = list_of_layers[6]
    dataframe_name.loc[7, column_name] = list_of_layers[5]
    dataframe_name.loc[8, column_name] = list_of_layers[4]
    dataframe_name.loc[9, column_name] = list_of_layers[3]
    dataframe_name.loc[10, column_name] = list_of_layers[2]
    dataframe_name.loc[11, column_name] = list_of_layers[1]
    dataframe_name.loc[12, column_name] = list_of_layers[0]

    return dataframe_name


##Need to change titles

def plot_given_df(dataframe,lang1x,lang1y,lang2x,lang2y,lang3x,lang3y):
    # Separate values to make it easier to plot
    sep_values = pd.concat((pd.DataFrame(dataframe[col].tolist()) for col in dataframe), axis=1)
    #Now that the columns are created they need to be renamed
    sep_values.columns = [lang1x, lang1y, lang2x, lang2y, lang3x, lang3y]
    #convert to numeric for plotting
    sep_values[sep_values.columns[0:]] = sep_values[sep_values.columns[0:]].apply(pd.to_numeric, errors = 'coerce')
    #Print out plot of data
    ax1 = sep_values.plot.bar(x=lang1x,y=lang1y, rot=45,color='y',figsize=(10, 6), title='Classifier')
    ax1.set_xlabel("Layers")
    ax1.set_ylabel("Classifier Accuracy")
    ax2 = sep_values.plot.bar(x=lang2x,y=lang2y, rot=45, color='m',figsize=(10, 6), title='Classifier')
    ax2.set_xlabel("Layers")
    ax2.set_ylabel("Classifier Accuracy")
    ax3 = sep_values.plot.bar(x=lang3x,y=lang3y, rot=45, color='c',figsize=(10, 6), title='Classifier')
    ax3.set_xlabel("Layers")
    ax3.set_ylabel("Classifier Accuracy")
    return ax1,ax2,ax3 
