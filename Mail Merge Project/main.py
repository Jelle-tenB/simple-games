# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
letter = []

with open(r"Mail Merge Project Start\Input\Names\invited_names.txt") as i:
    new_names = i.readlines()

for _ in new_names:
    name = _.strip("\n")
    names.append(name)

with open(r"\\RT-NAS\home\jbroeke\Desktop\python code\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode="r") as f:
    starting_letter = f.readlines()
    for t in names:
        with open(rf"\\RT-NAS\home\jbroeke\Desktop\python code\Mail Merge Project Start\Output\ReadyToSend\letter_for_{t}.txt", mode="w") as ready:
            for i in starting_letter:
                stuff = i.replace("[name]", f"{t}")
                ready.write(stuff)
