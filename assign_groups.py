#!/usr/bin/env python
from __future__ import print_function

import csv
import random
import sys

DEFAULT_GROUP_SIZE = 2

HEADERS = ["Your name and username", "Partner 1", "Partner 2"]
GROUP_PATTERN = "G%02d"
HELP_WANTED = "=Please find me someone to work with="

if __name__ ==  "__main__":
    if len(sys.argv) < 3:
        msg = "The first argument should be csv file from Google Spreadsheet.\n"
        msg += "The second argument should be csv file form SAFE with student list."
        sys.exit(msg)

    # read in usernames downloaded form SAFE
    students = []
    uids = []
    with open(sys.argv[2], "r") as usernames:
        u = csv.reader(usernames)
        for i in u:
            if not i:
                continue
            students.append(i)
    students.reverse()

    header = students.pop()
    if "Username" in header:
        uid_index = header.index("Username")
    elif "User" in header:
        uid_index = header.index("User")
    else:
        sys.exit("Neither Username nor User found in the student list CSV header.")

    for i in students:
        uids.append(i[uid_index].lower().strip())

    choices = []
    with open(sys.argv[1], "r") as csvfile:
        choices_csv = csv.reader(csvfile)
        for row in choices_csv:
            if not row:
                continue
            choices.append(row)
    choices.reverse()

    header = choices.pop()
    uid_index = []
    for i in HEADERS:
        if i in header:
            uid_index.append(header.index(i))

    groups = []
    seen = []
    pair_me_up = []
    for i in choices:
        gr = []
        visited = False
        pair_up = False
        for j in uid_index:
            if HELP_WANTED == i[j]:
                pair_up = True
                continue

            k = i[j].split("-")
            for ki in k:
                kis = ki.strip()
                if kis in uids and kis not in gr:
                    gr.append(kis)
                    if kis in seen:
                        visited = True
                    else:
                        seen.append(kis)
        gr = list(set(gr))
        gr.sort()

        assert len(gr) > 0, "A group should always have at least one person -- the one submitting the form."
        if pair_up and len(gr) != 1:
            print(gr, " are already paired but still look for a partner. Ignoring...")
        elif pair_up:
            assert len(gr) == 1, "Only single people should request pairing up."

            # Check whether this person has already been assign -- corresponds to "Check for duplicates" from down below
            duplicate_msg = ""
            for x in groups:
                for y in x:
                    if y in gr:
                        duplicate_msg = gr[0] + " is already assigned to a group " + str(x) + " and requested pairing. Ignoring..."
                        break
            if duplicate_msg:
                print(duplicate_msg)
            else:
                pair_me_up.append(gr[0])
            continue

        # Check for duplicates
        if gr not in groups and visited:
            repeated_groups = []
            for x in groups:
                for y in x:
                    if y in gr:
                        repeated_groups.append(x)
                        break
            if len(repeated_groups) > 1:
                sys.exit("Two groups with the same person")
            else:
                groups.remove(repeated_groups[0])
                for z in gr:
                    if z not in repeated_groups[0]:
                        repeated_groups[0].append(z)
                groups.append(repeated_groups[0])
        elif gr not in groups:
            groups.append(gr)

    # Sort out people who requested pairing
    if len(pair_me_up) != len(set(pair_me_up)):
        print("Some people submitted pairing request twice.")
        pair_me_up = list(set(pair_me_up))
    random_groups = []
    while pair_me_up:
        if len(pair_me_up) == 1 and random_groups:
            assert len(pair_me_up) == 1, "This should be the last or only person in this list."
            random_groups[-1].append(pair_me_up[0])
            print("One random group will have 3 people -- odd number of requests: ", random_groups[-1], ".")
            pair_me_up.remove(pair_me_up[0])
        elif len(pair_me_up) == 1 and not random_groups:
            # Only a single person requested pairing -- cannot do anything
            assert len(pair_me_up) == 1, "This should be the last or only person in this list."
            random_groups.append([pair_me_up[0]])
            pair_me_up.remove(pair_me_up[0])
        else:
            rc = random.sample(pair_me_up, DEFAULT_GROUP_SIZE)
            for r in rc:
                pair_me_up.remove(r)
            random_groups.append(rc)

    all_groups = groups + random_groups
    for i in all_groups:
        for j in i:
            try:
                uids.remove(j)
            except:
                print("double response: ", j)
    print("Students without a group submission:")
    print(uids)
    print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")

    print("Too large groups:")
    too_large_groups = []
    for group in groups:
        if len(group) > 3:
            print(group, "group is too large, please assign a group manually.")
            too_large_groups.append(group)
    for group in too_large_groups:
        groups.remove(group)
    print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")

    fen = "Student, Group\n"
    gs = ""
    gc = 1
    for i in groups:
        for j in i:
            fen += j + ", " + GROUP_PATTERN%gc + "\n"
        gc += 1
    for i in uids:
        fen += i + ", " + GROUP_PATTERN%gc + "\n"
        gc += 1

    print("Random groups:")
    for i in random_groups:
        group_info = [GROUP_PATTERN%gc]
        for j in i:
            fen += j + ", " + GROUP_PATTERN%gc + "\n"
            group_info.append('{}@bristol.ac.uk'.format(j))
        print(' '.join(group_info))
        gc += 1
    print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")

    for i in range(1, gc):
        gs += GROUP_PATTERN%i + ", "
    print("Groups assigned so far:")
    print(gs[:-2])
    with open("group_assignment.csv", "w") as ff:
        ff.write(fen)
