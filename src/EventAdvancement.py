__author__ = 'Jean-Alexandre'
import pygame
BradvaNegociation = False
BradvaWar = False

SchoolAtSleep = False
STEP3000 = False
SerumUtopia = False

KarmaVesuve= False


wait = False
daynumber=0


TheListAgriculture = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]
TheListPetrole = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]
TheListChasse = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]
TheListBois = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]
TheListPeche = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]
TheListMinerais = ["RegionA","RegionB","RegionC", "RegionD","RegionE","RegionF","RegionG", "RegionH","RegionI","RegionJ","RegionK", "RegionL"]

#################################

PremiereValeur=""
DeuxiemeValeur=""
ValeurDeveloppe=""

Ending_Bonheur = ""
Ending_Influence= ""
Ending_Sante= ""
Ending_Education = ""
Ending_Criminalite = ""
Ending_Population = ""
Ending_Pollution = ""
Ending_Panique = ""

##################################
Fin_SAS = "L'humanité s'est, avec courage, remise de sa presque extinction. Les humains, dotés pour la majorité de par leur SchoolAtSleep de connaissances incroyables et d'une performance intellectuelle supérieure, réussirent à rapidement reconstruire leur monde. Au gré des années, de superbes choses furent permissent par la science : la colonisation de la Lune et de Mars, l'invention du vaccin universel, l'extraction d'énergie venant directement du Soleil, etc. Cependant, il y a une chose contre quoi l'Homme ne pu lutter, malgré ses efforts. Sa puissance intellectuel, sa capacité à développer des technologies qui avant ne faisait que le faire rêver et les connaissances infinies dont  il profitait grâce aux SAS et ses dérivés l'on tellement enivré que même alors qu'il s'est aperçu que l'engin affectait de plus en plus sa raison, il n'a pas voulu arrêter son utilisation et de se départir de ce qui lui permettait de si bien percer les secrets de l'Univers. Chaque génération, toujours plus riche de toutes les connaissances des précédentes,  fut également beaucoup plus affecté par la folie que semble provoquer l'usage des SAS. Aujourd'hui, pratiquement aucun être humain n'est capable de totalement garder les deux pieds dans la réalité et notre espèce est en voie d'extinction. Parce que plus personne ne réalise leur utilité, ou  n'est en mesure d'en parler, aucuns jeunes de notre génération n'a jamais usé d'un SAS, mais la majorité sont quand même gravement affecté par toute une variété de problèmes mentaux graves. La majorité ne survivra pas à leur vingtième année de vie. Apparemment, tout ça, c'est à cause d'un nouveau gène apparue dans notre ADN, qu'on a appelé le gène SAS et qui transmet notre démence d'une génération à l'autre, de façon toujours plus forte. "
Fin_Sameness = "L'humanité s'est, fort vaillamment, remise du fléau de la Mort Rouge. Désormais une espèce libéré des préjugés, de la colère et des émotions négatives, l'Homme à reconstruit une civilisation avec d'étonnantes infrastructure sociale, dans le but que jamais personne ne manque de rien. Au fil du temps, au fils des ajouts à notre complexe système social et au fur et à mesure que les nouvelles générations se sont fait inoculer les sérums Utopia, notre ADN s'est mise subtilement à se transformer. Peu à peu, l'Homme se mit à perdre la vision des couleurs, qui «marque trop de différence entre les choses». Ensuite, nous perdîmes graduellement nos émotions, par la bio-accumulation du sérum au sein de notre espèce. Par après, une fois tout sentiment éteint en nos cœur, une fois chacune des couleurs transformées à nos yeux en un gris aux nuances ténues, après que la seule chose différenciant encore deux individus soit leurs identifiant numérique, mais alors qu'il nous restait encore juste assez de créativité pour inventer, nous conçûmes l'«Overmind», un ordinateur-administrateur sur lequel on connecta tout le monde, pour réunir les pensées de tout le monde en un tout qu'il contrôle, dans le but de parfaire l'efficacité de tout le monde et de guider l'humanité, se définissant dès lors comme l'«Overmind», dans son évolution vers l'efficacité et la précision parfaite d'un système mécanique, sans émotions ou différences. Mais honnêtement, est-ce vraiment au mieux? L'union dans l'acceptation et la compréhension de nos différences et idées divergentes aurait-elle pu nous offrir un plus belle avenir? Probablement."
Fin_Etat_Policier = "L'humanité s'est, avec bravoure, remise de la presque extinction. Elle reconstruisit son monde sur un modèle de Justice totale : bien qu'il y ait encore des criminelles, ils sont rapidement trouvé et enfermé. La corruption n'est plus qu'un vague souvenir du passé, tout comme le crime financier qui appartient lui aussi au passé. Pendant longtemps, l'humanité, grâce au système satellite STEP3000, ne connu plus le crime et vécu en louant les vertus de la Justice, cherchant toujours à se rapprocher de la perfection de ce côté, qui était devenu le plus beau des idéaux à atteindre. Ainsi, l'on commença par remplacer les représentants de la lois par des robots, incorruptible et performant, ne commettant pas d'impairs, n'y de vice de procédure. Pour les mêmes raisons, la majorité des infrastructures furent également laissé à la gestion de robot. Cependant, ces robots si bien programmés et puissants ne tardèrent pas à eux-même créer des règles pour ce qui leur semblaient être le bien de la société. Malheureusement, ils se trompèrent lourdement et à force d'en édicter des nouvelles, les prisons furent rapidement pleines. Pour régler le problème, les robots déclarèrent que la peine de mort serait appliquée systématiquement comme sentence à toutes les infractions. Ainsi, l'Homme se retrouva prisonnier de son propre système de lois, incapable de lutter contre les robots qu'ils avaient placé à la tête de la société. Il y survivra peut-être, mais il est clair que son avenir immédiat est des plus sombre et stricte."
Fin_Inconnue = "Malgré les difficultés, malgré les défis que vous avec dû affronter, vous êtes parvenu à mener les derniers survivants de l'humanité vers un futur plus radieux. L'histoire se rappellera de vous selon le mérite de vos actes et décision et les élèves du futur se devrons d'apprendre un nom supplémentaire : le votre, le nom de celui qui a permis à l'humanité d'affronter et traverser les misères de son crépuscule pour la mener vers une nouvelle aube, une renaissance. Qui la conduira où? Bonne question. La somme des actions de chacun d'entre nous le déterminera."
The_EndingText = Fin_Inconnue

Gagne = "Après plusieurs jours de voyage, qui se passèrent à vrai dire plutôt bien, vous parvenez jusqu'au Québec, dans les ruines de ce qui fût autrefois Montréal. Heureusement, il n'y a en effet plus de trace de Mort Rouge et ainsi, l'humanité pu commencer à reconstruire sa civilisation. Bientôt, des élections auront lieux car maintenant que le projet ARCHE a remplie sa mission, il est temps de retourner à la démocratie et vous, de prendre une pose bien mérité. Félicitation!"
Extinction = "Malheureusement, le chemin que vous avez fait emprunter à l'humanité l'a conduite à sa perte. Pour une raison ou une autre, une catastrophe ou de mauvais choix, elle s'est éteinte. Toute votre population, l'humanité, a péri."
Coup_etat = "Votre nation est tmbé sous la puisaance d'une organisation criminelle d'importance. Malheureusement, la très grande majorité de votre population et des gens de pouvoir sont aujourd'hui sous l'influence de cette organisation. Rien de de bon ne pourra surgir de cela en ce qui concerne le future de l'humanité... n'y le votre. Vous avez déjà reçu la recommendation de prendre une retraite anticipée..."
LaRevolution = "La population en a assez de vous et de votre dictature cruelle les plongeant dans la misère et le tristesse, elle s'est révoltée! Quoi qu'il en soit, il est clair que le future de l'Homme se révèlera mieux sans vous pour le diriger... désolé."
LaRedDeath = "Notre population vie aussi bien que possible... mais on ne l'aide pas vraiment. Nos infrastructures sanitaires et médicales inexistantes ou guère suffisantes ne suffisent pas à maintenir notre population en bonne santé. Cela à été propice à la mutation d'une terrifiante maladie qui à l'origine ne pouvait se développer ici... LA MORT ROUGE VA TOUS NOUS TUEZ!!! Un cas s'est déclaré ce matin, rapidement suivi d'une centaine d'autre. Ce n'est plus qu'une question de heures avant notre fin."
Anarchie = "Man'ana'toura est submergé par un chaos entropique, la panique s'est emparée de tout le monde et vous ne parvenez plus à rien contrôler! C'est dommage, mais tout le monde essait de voler et entreposer le plus de ressources possible pour survivre dans son coin... mais précipite ainsi notre fin, car la coopération était la clé de notre survie."
Vesuve = "Il est minuit alors que de terrible tremblement de terre vous réveille en sursaut. L'esprit encore embrumé par le sommeil, vous aller voir par la fenêtre du centre de votre pouvoir dictatorial et vous y voyez l'éruption du volcan, une éruption terrible et digne de celle du Vésuve du Pompéi de jadis.  L'éruption dévasta toutes l'île et mis fin à la vie de tout ceux qui s'y trouvait, y compris vous.  C'est tragique, mais votre soif de  pouvoir vous a poussé à rester sur une île où les catastrophes naturelles sont plus que commune et il s'adonne que, peut-être une question de karma comme diraient certains,  que peu après votre décision de garder les derniers représentants de l'humanité sur cette île, son volcan explose... réduisant à néant les dernières chances de sauvé notre espèce."

Linkmessage = ""

TrueEnding = False
HappyEnd = False
WIN = False
# TrueEnding = True
# HappyEnd = True
# WIN = True
# The_EndingText = Fin_SAS
# Linkmessage = Gagne


#################################################################
#SONS

sound_validation = pygame.mixer.Sound("Soundtrack/VerificationTone6.ogg")
sound_buttonpassOver = pygame.mixer.Sound("Soundtrack/Signal5.ogg")
sound_Typing = pygame.mixer.Sound("Soundtrack/ButtonClicks10.ogg")
sound_Woosh = pygame.mixer.Sound("Soundtrack/StaticElectric3.ogg")
sound_InvalidChoice = pygame.mixer.Sound("Soundtrack/ErrorTone13.ogg")
sound_ValidChoiceOK = pygame.mixer.Sound("Soundtrack/MusicFXSimple1.ogg")
sound_QuitOrReturn = pygame.mixer.Sound("Soundtrack/MusicFXSimple2.ogg")
sound_BuildingDestroyed = pygame.mixer.Sound("Soundtrack/Explosion.ogg")
sound_BuildingContructed= pygame.mixer.Sound("Soundtrack/BuildingConstruction.ogg")




#######################################################################
ARNAQUED=False
ARNAQUED_SECTOR = ""