#!/usr/bin/env python3

import sys

class Skill:
    name = ""
    level = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Skill: {self.name} {self.level}"

class Contributor:
    name = ""
    skills = []

    def __init__(self, name):
        self.name = name

    def addSkill(self, role):
        self.skills.append(role)

    def __repr__(self):
        ret = f"Contributor: {self.name}"
        for skill in self.skills:
            ret += skill.__repr__() + "\n"
        return ret

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

    def addRole(self, skill):
        self.roles.append(skill)

    def __repr__(self):
        ret = f"Project: {self.name}\nDuration: {self.duration}\nScore: {self.score}\nBest before: {self.bestBefore}\n"
        for role in self.roles:
            ret += role.__repr__() + "\n"
        return ret

# Fill contributors and projets
def read_file(file, contributors, projets):
    firstLine = file.readline().split(' ')
    nbContributors = int(firstLine[0])
    nbProjets = int(firstLine[1])

    for _ in range(0, nbContributors):
        contributorLine = file.readline().split(' ')
        contributor = Contributor(contributorLine[0])
        nbSkills = int(contributorLine[1])

        for _ in range(0, nbSkills):
            skillLine = file.readline().split(' ')
            contributor.addSkill(Skill(skillLine[0], int(skillLine[1])))
        contributors.append(contributor)

    for _ in range(0, nbProjets):
        projectLine = file.readline().split(' ')
        project = Project(projectLine[0], int(projectLine[1]), int(projectLine[2]), int(projectLine[3]))
        nbRoles = int(projectLine[4])

        for _ in range(0, nbRoles):
            skillLine = file.readline().split(' ')
            project.addRole(Skill(skillLine[0], int(skillLine[1])))
        projets.append(project)

# Open file, fill lists, run simulation
def main(path):
    contributors = []
    projets = []

    file = open(path)
    read_file(file, contributors, projets)

    for contributor in contributors:
        print(contributor)
    for project in projets:
        print(project)

if __name__ == "__main__":
    main(sys.argv[1])
