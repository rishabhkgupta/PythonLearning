LETTER_PATH = r"24_Day\part_2\Mail Merge Project Start\Input\Letters\starting_letter.txt"
NAME_PATH = r"24_Day\part_2\Mail Merge Project Start\Input\Names\invited_names.txt"
OUTPUT_LOCATION = r"24_Day\part_2\Mail Merge Project Start\Output\ReadyToSend"
PLACEHOLDER = "[name]"

# open names and save iach in a list called names
with open(NAME_PATH) as file:
    names = [line.rstrip() for line in file.readlines()]

# open the letter and write new letter with names in a new folder
with open(LETTER_PATH) as file:
    letter = file.read()
    for name in names:
        new_letter = letter.replace(PLACEHOLDER , name)
        with open(OUTPUT_LOCATION + f"\letter_for_{name}.txt", mode="w") as file:
            file.write(new_letter)


