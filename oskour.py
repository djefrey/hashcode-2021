#!/usr/bin/env python3

class Role:
    name = ""
    level = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

class Contributor:
    name = ""
    skills = []

    def __init__(self, name):
        self.name = name

    def addSkill(role):
        self.skills.append(role)

class Project:
    name = ""
    duration = 0
    score = 0
    bestBefore = 0
    roles = []

    def __init__(self, name, duration, score, bestBefore):
        self.name = name
        self.duration = duration
        self.score = score
        self.bestBefore = bestBefore

    def addRole(role):
        self.roles.append(role)

# Fill contributors and projets
def read_file(file, contributors, projets):
    return

# Open file, fill lists, run simulation
def main(path):
    contributors = []
    projets = []

if __name__ == "__main__":
    main(sys.argv[1])