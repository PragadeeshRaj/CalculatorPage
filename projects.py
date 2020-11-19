def setup():
    name = "P2-Einsteins"
    github = "https://github.com/PragadeeshRaj/Raj-Academy"
    embedbasic = "https://repl.it/@PragadeeshRaj/basiccalc?lite=true"
    embedscientific = "https://repl.it/@aymankazi9/Calc?lite=true" #"https://Calc.aymankazi9.repl.run"
    source = {"name": name, "github": github, "embedbasic": embedbasic, "embedscientific": embedscientific}

    project1 = "Basic Calculator"
    projlinks1 = [
        Link("Calculator", "https://repl.it/@AZPragTeam/ThisIsItBois")
    ]
    project2 = "Scientific Calculator"
    projlinks2 = [
        Link("Calculator", "https://github.com/PragadeeshRaj/Raj-Academy")
    ]

    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)

    projects = Projects(source, [proj1, proj2])
    return projects


class Link():
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href

    def get_btn(self):
        return self.btn

    def get_href(self):
        return self.href


class Project():
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links


class Projects():
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects

    def get_source(self):
        return self.source

    def get_projects(self):
        return self.projects
