""" Read and Write to a file using Python """

""" Reads file containing names """
with open("../Day 23 Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.read().splitlines()


""" Reads letter template """
with open("../Day 23 Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letters_file:
    letters = letters_file.read()


""" Replaces each names in the template and creates new output.txt file """
for name in names:
    final_letters = letters.replace("[name]", name)

    with open(f"../Day 23 Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as output_file:
        output_file.write(final_letters)
