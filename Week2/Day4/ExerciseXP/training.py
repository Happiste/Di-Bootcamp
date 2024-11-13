with open('/Users/happiste/Documents/DI-Bootcamp/week2/Day4/ExerciseXP/nameslist.txt', 'r+') as f:
    list_content = f.readlines()
    striped_list = [line.strip() for line in list_content]
    print(striped_list)
    # for line in list_content:
    #     print(line.strip())

    for index, line in enumerate(list_content):
        if index == 4:
            print(f"5th Line >>>{line}")

    txt = "".join(list_content)
    print(txt)
    
    print(txt[:5])

    darth = striped_list.count("Darth")
    luke = striped_list.count("Luke")
    lea = striped_list.count("Lea")
    print(f"occurence: Darth > {darth} /  Luke > {luke} /  Lea > {lea}")
    f.seek(0,2)
    f.write("\nJonathan")

    for line in list_content:
        if line == "Luke":
            line = "Luke SkyWalker"
  






