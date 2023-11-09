import csv

# Ανοιξε το αρχείο εισόδου για ανάγνωση
with open('recipes_by_tag.csv', 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)

    # Ορισε τα ονόματα των στηλών στο νέο αρχείο
    header = ['tag','name', 'submitted', 'average_rating']

    # Διαβασε το πρώτο row ως header
    first_row = next(reader)
    if first_row[0] == 'tag,name,submitted,average_rating':
        # Προσπερασε τον αρχικό header
        first_row = next(reader)
    
    # Ανοιξε το αρχείο εξόδου για εγγραφή
    with open('split_recipes_by_tag.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        
        # Γραψεε το νέο header
        writer.writerow(header)
        
        # Διαβασε τις γραμμές του αρχείου εισόδου και διαχωρισε τα δεδομένα
        for row in reader:
            if len(row) == 4:
                writer.writerow(row)
            else:
                # Αν η γραμμή δεν έχει το αναμενόμενο μήκος, τότε προσθεσε τα δεδομένα της στην τρέχουσα γραμμή
                # με την προηγούμενη
                previous_row[-1] += ' ' + row[0]
                
            # Κρατησε την τρέχουσα γραμμή ως την προηγούμενη
            previous_row = row
