from Repo.repositoryN import TemaRepo
from service.ServiceT import TemeService
from validator.teme_valid import TemeValidator
from service.serviceS import studservice
from Repo.repositoryS import StudRepo
from validator.stud_valid import StudValid
from Repo.repositoryP import ProbRepo
from validator.prob_valid import ProbValid
from service.serviceP import probservice
from ui.consola import console
from Repo.repofile import RepofromFile
from service.ServiceSF import serv
# repos
rep = StudRepo()
# rep = RepofromFile('date.txt')
repp = ProbRepo()
repoteme = TemaRepo()
# vali
vali = StudValid()
valip = ProbValid()
valit = TemeValidator()
# services
Se = studservice(rep, vali)
# Se = serv(rep,vali)
servP = probservice(repp, valip)
service_teme = TemeService(repoteme, valit, rep, repp)

yep = console(Se, servP, service_teme)
yep.ui()