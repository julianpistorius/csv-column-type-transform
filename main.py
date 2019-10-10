import segFunctions

if __name__ == '__main__':
    # creates csv for LexTALE Spanish lists
    segFunctions.csv_from_excel(
        './data/green/Lexical_Access_Experimental_Item_Setup.xlsx',
        'LexTaleEsp',
        './data/processed_data/exp_files/lexTaleListEsp.csv')

    # Fixes incorrect type/formatting issues in CSV file
    segFunctions.fix_csv(
        './data/processed_data/exp_files/lexTaleListEsp.csv',
        './data/processed_data/exp_files/lexTaleListEsp_fixed.csv',
        {
            'Order': lambda x: int(float(x)),
            'corrAnsEspV': lambda x: int(float(x))
        }
    )
