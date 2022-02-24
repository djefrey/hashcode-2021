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
    skills = None

    def __init__(self, name):
        self.name = name
        self.skills = []

    def addSkill(self, role):
        self.skills.append(role)

    def __repr__(self):
        ret = f"Contributor: {self.name}\n"
        for skill in self.skills:
            ret += skill.__repr__() + "\n"
        return ret

    def canFulfillRole(self, role):
        for skill in self.skills:
            if skill.name == role.name and skill.level >= role.level:
                return True
        return False

    def doneJob(self, role):
        for skill in self.skills:
            if skill.name == role.name:
                if skill.level <= role.level:
                    skill.level += 1
                return

    def getLevelForRole(self, role):
        for skill in self.skills:
            if skill.name == role.name:
                return skill.level

    def canBeMentored(self, role):
        return self.getLevelForRole(role) == role.level - 1

    def canBeAMentor(self, role):
        level = self.getLevelForRole(role)
        if level == None:
            return False
        return level >= role.level

    def countCanMentor(self, roles):
        count = 0

        for role in roles:
            if self.canBeAMentor(role):
                count += 1
        return count

class Project:
    name = ""
    duration = 0
    score = 0
    bestBefore = 0
    roles = None

    def __init__(self, name, duration, score, bestBefore):
        self.name = name
        self.duration = duration
        self.score = score
        self.bestBefore = bestBefore
        self.roles = []

    def addRole(self, skill):
        self.roles.append(skill)

    def __repr__(self):
        ret = f"Project: {self.name}\nDuration: {self.duration}\nScore: {self.score}\nBest before: {self.bestBefore}\n"
        for role in self.roles:
            ret += role.__repr__() + "\n"
        return ret

class Work:
    name = ""
    workers = None

    def __init__(self, name, workers):
        self.name = name
        self.workers = workers

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

def dummyAssignments(contributors, projects, works):
    todo = projects
    loops = 0

    while len(todo) > 0 and loops < 10:
        loops += 1

        for project in todo:
            assignments = {}
            innerContinue = False

            for i in range(len(project.roles)):
                bestForTheJob = None
                isAJunior = False
                canMentor = 0

                role = project.roles[i]
                nextRoles = project.roles[i + 1:]

                for contributor in contributors:
                    for assigned in assignments.values():
                        if assigned == contributor:
                            innerContinue = True
                            break

                    if innerContinue:
                        innerContinue = False
                        continue

                    if (bestForTheJob == None or isAJunior == False) and contributor.canFulfillRole(role):
                        if bestForTheJob == None:
                            bestForTheJob = contributor
                            canMentor = contributor.countCanMentor(nextRoles)
                        else:
                            actualCanMentor = contributor.countCanMentor(nextRoles)
                            if actualCanMentor > canMentor:
                                bestForTheJob = contributor
                                canMentor = actualCanMentor
                            elif actualCanMentor == canMentor and contributor.getLevelForRole(role) < bestForTheJob.getLevelForRole(role):
                                bestForTheJob = contributor

                    if contributor.canBeMentored(role):
                        for mentor in assignments.values():
                            if mentor.canBeAMentor(role):
                                if bestForTheJob == None or isAJunior == False:
                                    bestForTheJob = contributor
                                    canMentor = contributor.countCanMentor(nextRoles)
                                    isAJunior = True
                                else:
                                    actualCanMentor = contributor.countCanMentor(nextRoles)
                                    if actualCanMentor > canMentor:
                                        bestForTheJob = contributor
                                        canMentor = actualCanMentor
                                break

                if bestForTheJob == None:
                    break

                assignments[role] = bestForTheJob

        if len(assignments) == len(project.roles):
            addWork(works, project, assignments)
            todo.remove(project)

def addWork(works, project, assignments):
    workers = []

    for role in project.roles:
        assignments[role].doneJob(role)
        workers.append(assignments[role])
    works.append(Work(project.name, workers))

# Open file, fill lists, run simulation
def main(path):
    contributors = []
    projets = []
    works = []

    file = open(path)
    read_file(file, contributors, projets)

    projets.sort(key=lambda project: project.bestBefore)

    dummyAssignments(contributors, projets, works)

    print(len(works))
    for work in works:
        workers = work.workers

        print(work.name)
        for i in range(0, len(workers)):
            if i > 0:
                print(f" {workers[i].name}", end='')
            else:
                print(workers[i].name, end='')
        print()

if __name__ == "__main__":
    main(sys.argv[1])
