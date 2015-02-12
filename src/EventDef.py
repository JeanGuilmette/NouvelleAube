import Events

evt_available_list = []

##################################
# Epidemie
##################################
desc = "Un terrifiant fléau vient de s'abattre sur nos têtes. Une maladie qui a pris de tel proportion dans le secteur qu'elle en est devenu une épidémie et menace désormais de se répandre sur le reste de l'île. Cette maladie est extrêmement dangereuse et fait déjà plusieurs dizaines de victimes. Que faire?"
choix_A=("Bouclez le secteur, je ne veux personne qui puisse en entrer  ou en sortir.")
effect_A = ["MultiplyPop=0.5", "panic=7", "influence=-10"]
result_A = "La mise en quarantaine du secteur à certainement empêché la maladie de se répandre sur le reste de l'île, mais malheureusement, le manque d'aide accordé aux malades a fait en sorte que beaucoup on perdu la vie. Les survivants et les habitants des autres secteurs sont bien sûr heureux d'avoir survécu, cependant ils se demandent à quel point ils peuvent s'attendre à recevoir votre aide advenant qu'une catastrophe leur arrive à eux...  "
choix_B=("Envoyez des équipes collecter les malades et enfermez-les dans n'importe quel édifice dont ils ne pouront pas sortir. À partir de là soignez-les au mieux possible.")
effect_B = ["MultiplyPop=0.9", "panic=5"]
result_B ="Tout est bien qui fini bien. Grâce aux soins prodigué par vos équipes, la majorité des malades ont survécu et la maladie ne s'est pas répandu partout sur l'île. Les gens parlent désormais de vous avec plus de considération."
choix_C=("Par conséquent, envoyez des équipes collecter les malades et emprisonnez-les dans un édifice quelconque et peu important, puis mettez-y feu. Il faut absolument éviter que la maladie se répandent encore plus.")
effect_C = ["MultiplyPop=0.7", "panic=25", "influence=-16", "bonheur=-7"]
result_C ="Malheureusement, la chasse aux malades s'est très mal déroulée. Dès que la rumeur d'équipes de nettoyages envoyée par vos soins pour brûler vifs les contaminés s'est répandu, une vague de terreur s'est emparée de tous et chacun. Beaucoup ont tenté, et souvent avec succès, de cacher leur proches pour éviter qu'ils soient capturer. Par ailleurs, les équipes ont énormément usé des informations transmissent par des voisins inquiets et autres, sauf qu'au final, nous avons probablement ainsi aussi bien réglé des querelles qu'empêcher la maladie de se répandre, car plusieurs de ces dénonciations, ont le sait maintenant, étaient fausse. Au final,  la confiance des habitants du secteur sera longue à regagner, car notre remède aura été bien pire que le mal. "
choix_D=("Une maladie à déjà faillit détruire notre monde et je ne laisserai pas cela ce reproduire! Bombarder le secteur infecté jusqu'à ce qu'il ne puisse avoir aucun survivant.")
effect_D = ["MultiplyPop=0", "popMax=150", "MultiplyResStock=0"]#, "WasteLand=1"#conduit à LA Révolution
result_D = "Une vague de stupeur s'est répandu sur tout Man'ana'toura dès que la première bombe a explosée. Personne ne voulait croire que vous aviez vraiment fait ça. Mais alors qu'un abominable silence s'installait, une fois le massacre terminé, les gens sont sortis de leur maison, une bougie à la mains dans la noirceur de la nuit, pour rendre hommage à vos victimes. Cette nuit, mue par la tristesse et l'horreur, le peuple chanta un air funèbre et tragique. Les mémoires resteront à jamais marquée par cet acte et peu voudront dorénavant vivre dans le secteur."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_epidemie = Events.Event("now", "Epidemie", desc, options)
evt_available_list.append(("0.001", evt_epidemie))

#####################################  

##################################
# Tremblement de terre
##################################
desc = "Aujourd'hui, une terrible catastrophe à frapper l'île. Alors que tous vivaient leur vie, la terre s'est mise à trembler! L'île a été frappé par des secousses sismiques si importantes que de nombreux bâtiments se sont écroulés, provoquant plusieurs centaines de mort et détruisant de précieuses réserves de ressources! Les citoyents demandent de l'aide pour la reconstruction de leurs maison. Que dois-je leur répondre?"
choix_A=("Que bien sûr, je vais les aider, c'est ma responsabilité! Prennez les ressources nécessaires dans nos réserves les plus proches.")
effect_A = ["MultiplyPop=0.8", "panic=15", "influence=10", "sante=-7","bonheur=-7", "MultiplyResStock=0.5"]
result_A = "Les gens vous sont très reconnaissant et si les travaux vont assez bien, tout devrait être reconstruit prochainement"
choix_B=("Les aider? Dites-leurs que j'ai malheureusement autre chose à faire, désolé.")
effect_B = ["MultiplyPop=0.7", "panic=25", "influence=-10", "sante=-14","bonheur=-14","MultiplyResStock=0.1"]
result_B = "Votre décision n'a pas fait que des mécontants, elle à également causé plusieurs morts par la faim, la soif ou encore la maladie. Les gens se sont arrangé comme ils le pouvaient pour se reconstruire les infrastructures nécessaire à leurs vie, mais ça va prendre du temps pour que tout redeviennent à la normale."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))


evt_seisme = Events.Event("now", "Séisme", desc, options)
evt_available_list.append(("0.001", evt_seisme))

#####################################
# Eruption volcanique
##################################
desc = "Des secousses sismiques vont prochainement provoquées, selon mes capteurs, l'éruption du volcan au centre de l'île! Il faut faire quelque chose, mais il ne nous reste que fort peu de temps pour le faire!"
choix_A=("Alors faisons au mieux; prévenez ma famille, mes amis et les gens importants de l'île qu'il faut impérativement trouver refuge sur l'une des deux îles secondaires car le volcan va rentré en éruption! Aussi, assurez-vous de mettre en sécurité le plus de ressources possibles.")
effect_A = ["MultiplyPop=0"]
result_A = "Aux côtés de quelques priviligiés et des plus chanceux de la population de Man'ana'toura, vous assistez à la destruction de la principale partie de Man'ana'toura alors que la lave se met à l'engloutir. Il n'y a, malheureusement, aucune chance que malgré votre égoïsme quelqu'un là-bas ait pu survivre."
choix_B=("Le volcan n'est pas entré en éruption depuis au moins un millénaire... Je pense que votre source essai simplement de faire quitté l'île à tout le monde pour pouvoir ainsi plus aisément en prendre contrôle.")
effect_B = ["MultiplyPop=0"]
result_B = "Vous aviez tord, mais votre côté paranoïaque vous a au moins sauvé, car alors que le volcan déversait de la lave sur toute l'île principale, vous étiez paisiblement en train de dormir chez vous; dans un bunker ultra sécurisé qui vous a permis d'échapper aux flammes. Flammes qui, infortunément, ont consummés la vies de tout les gens de l'île principale, ainsi que les bâtiments et les entrpôts contenant vos ressources."
choix_C=("Organisez du mieux que vous le pouvez l'évacuation de la population pour l'ammener le plus loins possible du volcan.")
effect_C = ["MultiplyPop=0"]
result_C = "Malgré toute votre bonne volonté, malgré vos plus grands efforts, pratiquement personne n'a pu être sauvé, même chose pour les biens matérielles. C'est malheureux, mais dites-vous qu'au moins, vous avez essayé, que c'est l'intention qui compte et que... hum... c'est ça."
choix_D=("ISaveTheWorld, sans trop vouloir te vexer... il t'arrive plutôt régulièrement de faire des erreurs, non? Pour ma part, je me rappel de notre voyage jusqu'ici et d'une famine à bord causé par l'un de tes bugs. Il est très peu probable que le volcan entre en éruption, inutile d'alarmer tout le monde.")
effect_D = ["MultiplyPop=0"]
result_D = "... (Votre ISaveTheWorld garde le silence, vexé par votre manque de confiance qui a provoqué la destruction de toute l'île principale. Heureusement pour vous, votre ISaveTheWorld a veillé sur vous en vous convaincant avant l'éruption d'aller inspecter une installation quelconque sur une île secondaire.)"
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))

evt_Eruption = Events.Event("now", "Éruption volcanique", desc, options)
#####################################
# Fausse Eruption volcanique
##################################
desc = "Des secousses sismiques vont prochainement provoquées, selon mes capteurs, l'éruption du volcan au centre de l'île! Il faut faire quelque chose, mais il ne nous reste que fort peu de temps pour le faire!"
choix_A=("Alors faisons au mieux; prévenez ma famille, mes amis et les gens importants de l'île qu'il faut impérativement trouver refuge sur l'une des deux îles secondaires car le volcan va rentré en éruption! Aussi, assurez-vous de mettre en sécurité le plus de ressources possibles.")
effect_A = [ "panic=5","Déplacement de ressources=0.5", "Influence=-7" ]
result_A ="Oups... Je viens de réaliser qu'en fait, ce que mes capteur un prient pour des secousses sismiques annonciatrices d'une éruption n'était finalement que plusieurs envolées de canard. Nous venons de gaspiller des ressources sur une fausse alerte, mais ne vaut-il pas mieux prévenir que guérir?"
choix_B=("Le volcan n'est pas entré en éruption depuis au moins un millénaire... Je pense que votre source essai simplement de faire quitté l'île à tout le monde pour pouvoir ainsi plus aisément en prendre contrôle.")
effect_B = ["panic=0" ]
choix_C=("Organisez du mieux que vous le pouvez l'évacuation de la population pour l'ammener le plus loins possible du volcan.")
effect_C = [ "panic=55","Déplacement de ressources=0.1", "Influence=-15" ]
choix_D=("ISaveTheWorld, sans trop vouloir te vexer... il t'arrive plutôt régulièrement de faire des erreurs, non? Pour ma part, je me rappel de notre voyage jusqu'ici et d'une famine à bord causé par l'un de tes bugs. Il est très peu probable que le volcan entre en éruption, inutile d'alarmer tout le monde.")
effect_D = [ "panic=-20", "Influence=27" ]
result_D ="(Votre ISaveTheWorld grade en silence vexé alors que vous réalisez que ce qu'il a prit pour des secousses sismiques allant déclencher une éruption volcanique ne sont en fait que de légères secousses que pratiquement personne ne sentit. Il s'était totalement trompé.)"
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_A))
options.append(("Option C", choix_C, effect_C, result_A))
options.append(("Option D", choix_D, effect_D, result_D))

evt_Fausse_Eruption = Events.Event("now", "Éruption volcanique", desc, options)
#####################################
# Tsunami
##################################
desc = "Une vague mortelle de terreur vient de déferler sur Man'ana'toura. On déplore aujourd'hui la mort d'un abonominable nombre de personne. Il est clair que l'on vit de terribles épreuves, mais il nous faut se ressaisir et se redresser."
choix_A=("Envoyer des équipes de sauvetage pour secourir la population.")
effect_A = ["MultiplyPop=0.85", "panic=7","influence=7", "bonheur=7", "MultiplyResStock=0.5"]
result_A ="La population acclamera, une fois une majorité de gens sauvé, votre brillante initiative qui aura sauvé énormément de vies. Cependant, alors que vos équipes de spécialistes des situations d'urgences sauvaient tout le monde, l'eau du tsunamie à causé l'effondrement de quelques bâtiments, mais à surtout réussi à aller gâcher d'importantes réserves de ressources."
choix_B=("Envoyer des équipes pour récupérer le plus de ressources posible et limité les dégâts à nos infrastructures.")
effect_B = ["MultiplyPop=0.7", "panic=14","influence=-10", "bonheur=-15", "MultiplyResStock=0.85"]
result_B ="Votre initiative a heureusement permise de sauvé énormément de ressources, qui allaient être d'une manière ou d'une autre rendu impropre à l'utilisation. Cependant, alors que vos équipes d'urgences sauvaient les biens matériels de la nation, de très nombreux membres de cette dernière trouvèrent la mort, faute de secours bien organisés."
choix_C=("Génial!Je n'aurai pas à faire remplir ma nouvelle piscine!")
effect_C = ["MultiplyPop=0.7", "panic=14","influence=-45", "bonheur=-25", "MultiplyResStock=0.5"]
result_C ="Dans l'esprit de votre altruisme et votre largeur de conscience totalement incroyablement développé, vous sortez vous baigner alors qu'hors de votre propriété votre population souffre et meurs. L'information, par un moyen inconnu, vint aux oreilles la-dite population, qui enragée, déferla lors de manifestations monstrueuses un peu partout sur les propriétés de l'état, anéantissant et pillant ressources et bâtiments. "
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))


evt_Tsunami = Events.Event("now", "Tsunami", desc, options)
#####################################
#Tornade
##################################
desc = "Une petite tornade a balayée le secteur. Plusieurs de nos infrastructures ont été affectées et de nombreuses familles risque de pleurer leurs proches disparues."
choix_A=("Malheureusement, on ne peut pas faire beaucoup mieux qu'envoyer des équipes de sauvetage pour secourir les blessés et d'autres équipes réparer nos infrastructures.")
effect_A = ["MultiplyPop=0.98", "panic=3","influence=5"]
result_A ="C'est toutefois déjà bien, au final, il n'y a qu'un faible pourcentage de la population qui a été blessé ou tué et les pertes du côté des resources sont minimes."
choix_B=("Nous n'avons malheureusement pas les ressources pour gérer ça. Ou je n'est pas particulièrement envie de les fournir. En vérité, ça revient au même.")
effect_B = ["MultiplyPop=0.94", "panic=6","influence=-5"]
result_B ="Et  dans un cas comme dans l'autre, les gens se débrouillent pour s'en sortir, vous tenant quand même un peu rigueur du fait que vous les laissiez le faire seul."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))


evt_Tornade = Events.Event("now", "Tornade", desc, options)
#####################################
#Revolte
##################################
desc = "Dans le secteur, la vie n'est pas facile. À un tel point que les habitants commence à ce sentir délaissé et pensent pouvoir, une idée de plus en plus répandue, plus facilement survivre et se développer en se gérant tout seul que sous votre contrôle. Un mouvement de pensées plus radicales, plus violentes, commence même à se répandre: Vous feriez exprès de les laisser dans la misère! Des manifestations de moins en moins pacifiques se déclenche un peu partout dans la zone et nous risquons de rapidement perdre absolument tout contrôle sur celle-ci, comment réagirons-nous?"
choix_A=("Faites exécuter publiquement tout les meneurs de ce mouvement, ce sont des traîtres et nous montrerons ce qu'on fait des traîtres!")
effect_A = ["population=-175", "influence=100"] #conduit à LA Révolution
result_A = "Cet acte provoque beaucoup d'émoi dans la population du secteur, qui a de façon visible effacé toutes idées de rebellions de leurs esprit. Mais honnêtement, Commandant, cela semble trop facile, il y a, je pense, quelque chose derrière cette apparente soumission. "
choix_B=("Bombardez la zone! Une fois que tout le monde sera mort, je peuplerai ce secteur de gens qui me sont loyaux.")
effect_B = ["MultiplyPop=0", "popMax=150", "MultiplyResStock=0"]#, "WasteLand=1",#conduit à LA Révolution
result_B ="Une vague de stupeur s'est répandue sur tout Man'ana'toura dès que la première bombe a explosée. Personne ne voulait croire que vous aviez vraiment fait ça. Mais alors qu'un abominable silence s'installait, une fois le massacre terminé, les gens sont sortis de leur maison, une bougie à la mains dans la noirceur de la nuit, pour rendre hommage à vos victimes. Cette nuit, mue par la tristesse et l'horreur, le peuple chanta un air funèbre et tragique. Les mémoires resteront à jamais marquée par cet acte et peu voudront dorénavant vivre dans le secteur."
choix_C=("Emprisonnez les protestataires les plus criminels, puis demandez aux plus pacifiques de nommez un porte-parole. J'écouterai ses plaintes et nous parviendrons à un arrangement.")
effect_C = ["influence=20", "bonheur=12","MultiplyResStock=0.8" ]
result_C ="Vous parvenez à désamorcer la situation par la voie de la diplomatie et de la loi, ce qui vous vaut un regain d'influence auprès de ceux qui pensaient que vous les délaissiez. Par ailleurs, vous vous êtes engagé à fournir les ressources pour la construction de diverses infrastructures jugées nécessaire par la population."
choix_D=("… En fait, ils n'ont pas une mauvaise idée. Empêchez quiconque de sortir ou de rentrer dans les zones affectées par les manifestations et coupez leurs toutes arrivées de nourritures. Maintenant, ils vont savoir ce que c'est quand je décide vraiment de les laisser dans la misère. Peut-être reviendront-ils à la raison? Ou pas, c'est tout aussi drôle.")
choix_E=("Eh bien... ils manquent de quoi? Envoyez-en comme nécessaires. Il suffisait simplement de demander...")
effect_E = ["influence=15", "bonheur=18","MultiplyResStock=0.65" ]
result_E ="Les gens sont stupéfait de la réponse que vous leurs faites... Mais ils tâches dans profiter au mieux et la situation semble s'arranger."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_A, result_A))
options.append(("Option E", choix_E, effect_E, result_E))

evt_Revolte = Events.Event("now", "Révolte", desc, options)
#####################################
#Arnaque
##################################
desc = "Bonjour... euh... Commandant... vous savez, à propos de la dernière contruction commandée dans le secteur... Il se trouve que nous avons été arnaqué. Totalement. Toutes les ressources que nous avons envoyées pour sa constructions ont été volées par les travailleurs, qui se sont évanouie dans la nature avec leur butin. Comment réagirons-nous?"
choix_A=("Lancez les forces de police à leur trousse et récupérez nos ressources.")
effect_A = ["criminalite=-20"]
result_A ="Relativement rapidement, la majorité des coupables ont été retrouvé. Cela, contrairement aux ressources qui auraient apparemment déjà été vendu à une organisation criminelle inquiétante. Nous poursuivons les recherches et si elles aboutissent, je vous en reparlerai."
choix_B=("Nous avons d'autres choses à s'occuper. Laissez-les aller, ne passons pas nos ressources sur cela.")
effect_B = ["criminalite=20"]
result_B ="Divers criminels prennent courage et augmentent leur activités en voyant un groupe des leurs réussir à arnaquer l'État sans subir l'ombre d'une conséquence."
choix_C=("Mettez une prime sur leur têtes. Je les veux morts ou vifs, avec les ressources qu'ils ont volées! Ce crime ne restera pas impuni.")
effect_C = ["population=-300", "criminalite=-10"]
choix_D=("Je veux un rapport complet sur la situation; QUI a permis à ces arnaqueurs d'agir, comment et pourquoi. Nous corrigerons notre système bureaucratique en conséquence pour que ce genre d'événement ne se reproduisent plus.")
effect_D = ["criminalite=-20"]
result_D ="Après une enquête approfondie, vos forces d'investigations ont réussient à retrouver les responsables et les causes, qui ont été corrigées. Malheureusemnt nos ressources auraient apparemment déjà été vendu à une organisation criminelle inquiétante. Nous poursuivons les recherches et si elles aboutissent, je vous en reparlerai."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_A))
options.append(("Option D", choix_D, effect_D, result_D))


evt_Arnaque = Events.Event("now", "Arnaque", desc, options)
#####################################
#Désertification
##################################
desc = "Vous vous rappelez, je vous avais parlé de l'épuisement des sols, de la surproduction et d'autres sujets d'actualité dans le secteur... eh bien, peut-être auriez-vous dû les prendre en compte. La zone commence déjà à ce désertifier. Après trois phases de désertification, la zone deviendra un désert et perdra énormément de son intérêt et de sa capacité de production de ressources."
choix_A=("ISaveTheWorld... tu ne m'en a jamais parlé...")
effect_A = ["bonheur=-10"] # Perte de ressources
result_A ="Oups... peut-être un autre bug... En tout cas, vous le saurez pour la prochaine fois."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Désertification = Events.Event("now", "Désertification", desc, options)
#####################################
#Surpopulation
##################################
desc = "Commandant! Du secteur montent plusieurs plaintes à propos du manque d'espace pour vivre, de la surpopulation des lieux! Si cela continu comme ça, les conditions de vie des habitants du secteur vont rapidement se dégrader. La meilleure solution serait d'effectuer un transfert de population."
choix_A=("Très bien, j'ordonnerai un tranfers de population.")
effect_A = ["bonheur=-10","sante=-7"]
result_A ="Ce sera probablement très apprécié... mais n'oubliez pas."
choix_B=("C'est bien parfait, j'ordonne un transfers de population... vers l'océan!")
effect_B = ["MultiplyPop=0.75", "bonheur=-15", "influence=-20"]#conduit à LA Révolution
result_B ="Les plus mal en point de secteur on été transférés... dans l'océan. Les habitants du secteur ne trouve pas votre décision cruelle. Pas du tout."
choix_C=("C'est triste, mais c'est partout comme ça, on ne peut pas effectuer de transfer!")
effect_C = ["bonheur=-5","sante=-7"]
result_C ="Avez-vous envisagé la construction de secteurs résidentielles? Ils permettent de mieux gérer la quantité de gens et la place qu'ils prennent pour vivre."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))


evt_Surpopulation = Events.Event("now", "Surpopulation", desc, options)
#####################################
#Vague de crime
##################################
desc = "La criminalité est trop élevée et cela ce traduit par une vague de crimes de tout acabi. Des gens meurent, se font voler, arnaquer, etc. Il faut faire refluer cette criminalité, sinon la région tombera définitivement dans le chaos. Une solution serait probablement la construction d'une prison"
choix_A=("C'est noté.")
effect_A = ["MultiplyPop=0,95", "panic=6","bonheur=-12" ]
result_A ="N'oubliez pas, sinon vous recevrez rapidement un autre message du genre."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Vague_de_crime = Events.Event("now", "Vague de crime", desc, options)
#####################################
#Épuisement du pétrole
##################################
desc = "Il n'y a plus de pétrole à exploiter dans la zone!"
choix_A=("Tant pis...")
effect_A = ["population=0"]
result_A ="N'oubliez pas, sans une quantité suffisante de pétrole, vous ne pourez pas envoyer d'expédition lorsqu'il sera temps de vérifier si le monde est purgé de toutes traces de Mort Rouge et il vous sera difficile de réagir face aux catastrophes pouvant survenir d'ici là. Gérez bien ce qu'il nous reste."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Épuisement_du_pétrole = Events.Event("now", "Épuisement du pétrole", desc, options)
#####################################
#Épuisement du gibier
##################################
desc = "Il n'y a plus de gibier à chasser dans la zone!"
choix_A=("J'aurais sûrement dû le prévoir...")
effect_A = ["bonheur=-15"]
result_A ="Très probablement. Maintenant que la faune à disparue de cette partie du l'île, vous devrez faire avec une autre source de nourriture... par ailleurs, les gens risques de s'ennuyer de manger de la viande rouge et cela va paraître sur le moral."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Épuisement_du_gibier = Events.Event("now", "Épuisement du gibier", desc, options)
#####################################
#Déforestation totale
##################################
desc = "Il n'y a plus de forêt à exploiter dans la zone!"
choix_A=("Dommage...")
effect_A = ["bonheur=-15"]
result_A ="Vive le développement durable... dans la gigantesque plaine qu'est maintenant le secteur, les gens vont s'ennuyer de la belle verdure d'autrefois, qui servait d'ailleurs égalemement de poumon à l'endroit."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Déforestation_totale = Events.Event("now", "Déforestation totale", desc, options)
######################################
# Épuisement de la faune aquatique
##################################
desc = "Il n'y a plus de poisson à pêcher dans la zone!"
choix_A=("C'est malheureux...")
effect_A = ["bonheur=-15"]
result_A ="Certainement. Maintenant que la faune marine à disparue de cette partie du l'île, vous devrez faire avec une autre source de nourriture... par ailleurs, les gens risques de s'ennuyer de manger de cette sorte de produit et cela va paraître sur le moral."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Épuisement_de_la_faune_aquatique = Events.Event("now", "Épuisement de la faune aquatique", desc, options)
#####################################
# Épuisement des minerais
##################################
desc = "Il n'y a plus de minerais à exploiter dans la zone!"
choix_A=("Triste...")
effect_A = ["bonheur=-15"]
result_A ="Sans minerais, il va être plus ardu de construire des bâtiments."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))


evt_Épuisement_des_minerais = Events.Event("now", "Épuisement des minerais", desc, options)
#####################################
#Feu de forêt
##################################
desc = "Un feu vient de se déclarer dans la principale forêt du secteur! Déjà, il prend une ampleur exponentielle et se répand un peu partout, dévastant la ressources et faisant fuir tout les animaux! Nos scieries ont même commencé à se faire affecter par les flammes."
choix_A=("Envoyer un hydravion, c'est pas mal tout ce qu'on peut faire...")
effect_A = ["population=-100", "panic=12"]
result_A ="Heureusement, ce fût suffisant, l'incendie à pût être controllé avant que la forêt ne brûle en entier. Malheureusement, la majorité de nos réserves de bois ont été touchées et détruites par les flammes avant qu'elles ne soient éteintes. "
choix_B=("Envoyer un hydravion et envoyez aussi des pompiers pour pour protéger les scieries qu'il nous reste.")
effect_B = ["population=-200", "panic=12"]
result_B ="Nos réserves de bois ont été touché, mais que légèrement. Même chose pour la forêt, qui devrait rapidement se remettre de l'incendie."
choix_C=("Pourquoi gaspiller des ressources pour sauver la vie d'un arbre?!?")
effect_C = ["population=-300", "panic=12"]
result_C ="Parce que l'on parlait ici de ce qui était la pincipale forêt du secteur, c'est-à-dire que maintenant qu'elle a brûlé, il ne reste plus tant de bois à exploiter dans la zone."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))



evt_Feu_de_forêt = Events.Event("now", "Feu de forêt", desc, options)
#####################################
#Aleksei Vasilev
##################################
desc = "Bonjour, camarade! Il se trouve que je mène un commerce plutôt important ici et que mes moyens de production sont très élevé. Cependant, pour accroître la puissance de mon entreprise, il me faudrait trouver une plus vaste clientèle... comme l'État lui-même! Une association serait extrêmement profitable pour nos deux parties. Donc voilà le marché : je fais construire à mes frais l'une de mes usines dans le secteur de votre choix et je la met à votre disposition, ce qui va permettre de grandement augmenter le rendement de tout les bâtiments produisant des ressources dans le secteur. En échange, nous serions prioritaire quand viendrait le temps de faire construire quelque chose par l'État. Qu'est-ce que vous en dites?"
choix_A=("C'est bien parfait, nous avons un accord!")
effect_A = ["criminalite=15"] #re-émergeance crime organisé
result_A ="Tant mieux, j'en ferai commencer la construction très prochainement camarade."
choix_B=("Nous merci cher monsieur, j'ai déjà tout ce qu'il me faut.")
effect_B = ["population=0"]#re-émergeance crime organisé
result_B ="C'est bien dommage... Vous venez de manquer une si belle opportunité commerciale!"

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))



evt_Aleksei_Vasilev = Events.Event("2015-10-27", "Aleksei Vasilev", desc, options)
#evt_Aleksei_Vasilev = Events.Event("now", "Aleksei Vasilev", desc, options)
#####################################
#(Ré-)Émergence du crime organisé
##################################
desc = "Malheureusement, parmi les gens que nous avons amené avec nous, il se trouve qu'il y avait certains membres de la Bradva, une organisation criminelle russe, qui ont trouvé le moyen de passer à travers ma vigilance lors de la sélection des passagers. Ils ont renforcé dans l'ombre leur pouvoir, et sont sur le point d'avoir totalement rebâtie leur organisation, en convertissant et soudoyant! Que faire?"
choix_A=("Faites-en venir le membre le plus puissant possible.")
effect_A = ["population=0", "Nego=1"] #Négociation avec la Bradva
result_A ="Je vais faire mon possible, mais ils risquent d'être méfiant..."
choix_B=("Ignorons-les, je n'ai pas le temps de m'en occuper.")
effect_B = ["criminallite=30"]# Coup d'État
result_B ="Hum... c'est votre choix..."
choix_C=("Envoyez tout nos effectifs contre ces criminelles, nous les traduirons en justice et par la vérité et la loi, ils tomberont. Faites convoquer une conférence de presse, je ferai un discours sur le courage, la justice et les responsabilité à la population, qui va devoir nous aider.")
effect_C = ["influence=30", "MultiplyPop=0.85","criminallite=-100"] # Ère de justice
result_C ="Tout le monde est fort impressionné par votre discours et répond à l'appel que vous lancez contre le crime, votre déclaration de guerre à la Bradva. Un à un, les criminels tombent, mort ou emprisonné. Un règne de justice s'instaure, et perdurera pour un temps, cependant au prix fort de la vie de nombreuses bonnes personnes ayant lutté contre le monde du crime."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))



evt_Emergence_du_crime_organise = Events.Event("2016-6-03", "(Ré-)Émergence du crime organisé", desc, options)
#evt_Emergence_du_crime_organise = Events.Event("2015-01-01", "(Ré-)Émergence du crime organisé", desc, options)
#####################################
#Négociation avec la Bradva
##################################
desc = "Commandant, surprenament,la Bradva vous envoie l'un de ses membres les plus influent pour initier le dialogue. « Bonjour, camarade! Qu'est-ce que l'on peut faire pour vous? »"
choix_A=("J'ai eu vent de vos activité de plus en plus criminelles et de votre puissance grandissante : Je veux pouvoir en profiter et pour cela, j'aimerais que nous passions un marché, pour la seconde fois. (Après plusieurs heures de négociation, vous acceptez de fermer les yeux sur leur activités  en échange d'une importante «donation»... c'est à dire l'équivalent de la moitié de chacune de vos réserves de ressources.)")
effect_A = ["population=-100", "criminalite=45","MultiplyResStock=1.5" ] #mène à coup d'état
result_A ="Vous recevrez donc ce fameux don... Cependant, au fil du temps qui passe, la criminalité va augmenter de façon exponentielle, comme la Bradva prendra de la puissance."
choix_B=("Je vous ais fait venir pour pouvoir voir à quoi ressemble un puissant de la Bradva qui se fait capturer et qui deviendra la cause de la chute de son organisation. Arrêtez-le.")
effect_B = ["criminalite=-18", "War=1"]#Guerre contre la Bradva
result_B =" Aleksei:«Je vous promet que cette traitrise ne restera pas impunie! Vous risquez un beau matin de vous réveiller mort, un couteau dans le dos!» ISaveTheWorld «... mais pouvons nous vraiment nous réveiller mort? Peu importe, votre acte a fait de vous un ennemi de la Bradva, leur a en fait déclaré la guerre.»  "
choix_C=("Un criminel tel que vous ne mérite pas de vivre. Faites-le exécuter.")
effect_C = ["criminalite=-5", "War=1"]#Guerre contre la Bradva
result_C ="Un meurtre pour faire régner la justice? C'est... Étrange? Par contre, je doute que ses amis en soit très heureux... vous venez en fait de déclarer plutôt clairement la guerre à la Bradva."
choix_D=("Pour continuer à exister, il va falloir me payer : vous avez amenez ce que je vous ais demandé? Oui, parfait. (Vous vous assurez que les chargements de ressources amené par Aleksei comme pot-de-vin ont été déchargés.) Je dois vous avouer qu'honnêtement, j'ai menti. Arrêtez ce criminel, et torturer-le si nécessaire pour obtenir toutes les informations qu'il possède.")
effect_D = ["criminalite=5", "War=1"]#Guerre contre la Bradva
result_D ="Pardonnez moi, mais est-ce cela votre idée de la justice, de la lutte contre le crime? C'est... machéavélique et probablement criminel, mais c'est vous le Commandant. Cependant, je doute que ses amis en soit très heureux... vous venez en fait de clairement déclarer la guerre à la Bradva. "
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_Negociation = Events.Event("2016-06-04", "Négociation avec la Bradva", desc, options)
#evt_Negociation = Events.Event("2015-01-03", "Négociation avec la Bradva", desc, options)
#####################################
#Guerre contre la Bradva
##################################
desc = "Vous venez de déclarer la guerre à la Bradva et par la même occasion, à tout le crime organisé qui s'est établit sur l'île. Les criminels se rassemblent et montent leur sinistre projets, manœuvrant dans l'ombre pour prendre le contrôle total de Man'ana'toura, par l'intimidation et la corruption, dans le but de plonger votre œuvre dans le chaos et la peur."
choix_A=("Lutter contre la Bradva.")
effect_A = ["MultiplyPop=0.8",  "MultiplyResStock=0,9",  "criminalite=0"]
result_A ="Après moult confrontations entre les forces de l'ordre et celles du crime, un commando d'élite réussi à capturer ou tuer tout les grands chefs. Après bien des tracas et une grande quantité d'enquêtes, la police à pour sa part réussi a totalement démonter le réseau criminel. Tout cela se traduit par la disparition de la criminalité sur l'île... pour le moment."
choix_B=("Lui faire des excuses publiquement et lui garantir la non-ingérence de l'état dans leur affaires.")
effect_B = ["MultiplyPop=0.6", "panic=100", "influence=-90", "bonheur=-70","sante=-35", "MultiplyResStock=0,1",  "criminalite=100"]
result_B ="Après votre discours, la population, déjà terrifié, sombre dans la panique la plus totale. Ayant permis aux criminels de faire ce qu'ils veulent, ceux-ci se jette sur l'occasion et par la même occasion, sur d'honnêtes gens. Alors que Man'ana'toura se baigne dans le sang de ses citoyens, plusieurs milices d'auto-défense voient le jour, provoquant malheureusement une sanglante escalade de violence, achevant de noyer l'île sous une mer de sang, de terreur et d'anarchie. Peut-être tout cela va-t-il se calmer avec le temps. Du moins, il faut l’espérer."
choix_C=("Ignorer la Bradva.")
effect_C = ["MultiplyPop=0.8", "panic=80", "influence=-50", "bonheur=-50","sante=-25", "MultiplyResStock=0,7",  "criminalite=100"]
result_C ="Devant votre inaction, la population, déjà terrifié par les activités de l'organisation, sombre dans la panique la plus totale. Ayant permis aux criminels de faire ce qu'ils veulent, ceux-ci se jette sur l'occasion et par le fait même, sur d'honnêtes gens. Alors que Man'ana'toura se baigne dans le sang de ses citoyens, plusieurs milices d'auto-défense voient le jour, provoquant malheureusement une sanglante escalade de violence, achevant de noyer l'île sous une mer de sang, de terreur et d'anarchie. Peut-être tout cela va-t-il se calmer avec le temps. Du moins, il faut l’espérer."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))



evt_Guerre_contre_la_Bradva = Events.Event("now", "Guerre contre la Bradva", desc, options)
#evt_Guerre_contre_la_Bradva = Events.Event("now", "Guerre contre la Bradva", desc, options)
#####################################


#Recherche
##################################
#L'EnergieThermovolcanique
##################################
desc = "Commandant, nos scientifiques, après beaucoup d'efforts, ont découvert un moyen de produire de l'électricité grâce au volcan. Cependant, la technique suscite quelques controverses, assez pour que deux groupes tentent de faire valoir leur position auprès de vous. Dans ce cas-ci, le groupe pour est composé des chercheurs qui ont mis au point la technologie. Voici leur argument: Premièrement, ce serait une source d'énergie inépuisable. Deuxièmement, c'est une source d'énergie propre qui pourrait remplacer avec une seule centrale toute les centrales thermique au pétrole de l'île. Du côté du contre, il s'agit d'un groupe de citoyens qui se sentent concerné par l'installation d'une centrale thermovolcanique sur l'île, qu'ils jugent trop dangereuse pour ceux qui vont y travailler et dont on ne connaît pas vraiment les effets à long terme sur le volcan."
choix_A=("Excellant, faites installer l'un de ces centres thermovolcaniques")
effect_A = ["pollution=-10"]
result_A ="Ce sera fait."
choix_B=("Je préfère ne pas prendre de risque par rapport au volcan.")
effect_B = ["pollution=10"]
result_B ="C'est votre droit."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))

evt_EnergieThermovolcanique = Events.Event("2015-12-30", "L'énergie thermovolcanique", desc, options)
#####################################
# SchoolAtSleep
##################################
desc = "Commandant, un groupe d'étude indépendant de l'île vient de mettre au point une technique d'éducation durant le sommeil totalement révolutionnaire. Ils affirment que grâce à elle, nous n'auront plus besoin d'école pour former des travailleurs, qui seront plus fiables dû à une meilleure connaissance de leur domaine. Par ailleurs, l'appareil, nommé SAS (SchoolAtSleep), permettrait de former les travailleurs plus rapidement que par la scolarisation traditionnelle. Cependant, un groupe de jeunes médecins affirme que l'usage de l'appareil pourrait potentiellement causer divers effets secondaires comme par exemple, une augmentation des chances de souffrir de schizophrénie."
choix_A=("Parfait, commencer la production et la distribution des SAS.")
effect_A = ["bonheur=30", "fin=SAS"]
result_A ="Il se révèlera que les SAS ne sont pas aussi efficaces que prévu. Il reste quelques ajustement à faire, mais dès qu'ils seront au point, nous en ferons la distribution. En attendant, ils sont suffisamment puissant pour permettre aux étudiants d'être meilleur à l'école plus facilement, ce qui augmente de beaucoup leur bonheur."
choix_B=("Je préfère ne pas prendre de risque par rapport à nos cervaux.")
effect_B = ["Population=0"]
result_B ="C'est votre droit."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))

evt_SchoolAtSleep = Events.Event("2017-11-03", "SchoolAtSleep", desc, options)
#####################################
#STEP3000
##################################
desc = "SécurInc. , LA compagnie de service de protection et d'alarmes de l'île, vient de créer un module satellite révolutionnaire! Ils se proposent de nous le vendre pour l'équivalent de 15% de nos réserves de pétrole. Le produit, nommé STEP3000 permettra à notre force policière de faire baisser la criminalité de façon majeure en lui permettant la surveillance de tout les mouvements, toutes les communications, tout les échanges et les relations entretenues par tout le monde sur l'île. Ce qui, bien entendu, ne plaît à pratiquement personne. Le très populaire groupe de musique punk «Uprising» s'est fait porte-parole de la cause et dénonce que ce satellite est le genre d'outil utilisé par une dictature pour rester au pouvoir. Par conséquent, il n'a pas sa place dans une société qui se veut démocratique."
choix_A=("J'en veux un!!! Pour que les forces de police puisse arêter des criminelles, bien entendu.")
effect_A = ["bonheur=-10", "criminalite=-30","influence=10", "fin=ETAT"]
result_A ="J'envoie votre réponse.."
choix_B=("Uprising a raison, on ne sait jamais qui prendra le pouvoir après moi.")
effect_B = ["Population=0"]


options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_A))

evt_STEP3000= Events.Event("2016-07-08", "STEP3000", desc, options)
#####################################
#Le sérum Utopia
##################################
desc = "Un neurologue renommé, l'éminent docteur Lamandre, a créer ce qu'il appel le «sérum Utopia». Selon lui, il procurerait un grand avantage à notre société: l'élimination de tout racisme, sexisme, extrémisme religieux, discrimination religieuse, âgisme et en fait, tout ce qui cause ce genre de dissensions dans la société. Le sérum est également un régulateur émotionnel qui en limiterait ses éclats (entre-autre les crises de rage, ou encore celles de larmes). Grâce au sérum Utopia, il n'y aura plus de mésententes dans la société. D'ailleurs, ce qui est particulier est que personne n'a décidé de s'opposer au projet... peut-être que tout le monde souhaite se faire inoculer le sérum? Peut-être qu'il pourrait vraiment rendre notre société utopique?"
choix_A=("Magnifique! Alors commencez la distribution!")
effect_A = ["criminalite=-30", "sante=15", "bonheur=30", "influence=15", "fin=Sameness"]
result_A ="Le docteur est même tellement convaincu du bien que va procurer le sérum à l'humanité qu'il nous offre le sérum gratuitement. Il ne vous reste plus qu'à donner l'ordre de faire injecter le sérum à la population et ce sera fait (au prix de 350 pétrole, pour la distribution)."
choix_B=("Non.")
effect_B = ["Population=0"]
result_B ="?!?"

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))

evt_serumUtopia = Events.Event("2018-11-24", "Le sérum Utopia", desc, options)

#####################################



#SITUATION DE FIN DE JEU

##################################
#À la reconquête du monde
##################################
desc = "Cela fait déjà cinq ans que nous vivons sur Man'ana'toura, cinq longues et difficiles années marquées par des catastrophes en tout genre. Cinq années, qui heureusement, ont été suffisamment longues pour marquer la fin de notre exil, car comme vous le savez, nos scientifiques ont déterminé que ce laps de temps serait suffisant pour que toute traces de la Mort Rouge soit disparue: Nous pouvons commencer à envisager notre retour au Canada! Qu'en pensez-vous?"
choix_A=("Que c'est merveilleux, avertissez tout le monde, nous allons remonter dans l'ARCHE pour regagner nos foyers!")
effect_A = ["Population=0", "WIN=1"]
result_A ="Dès que vous serez prêt à donner l'ordre du départ, faites le par l'entremise du menu Recherches. Cela provoquera le départ du bateau. Cependant, le bateau aura besoin de pétrole et de nourriture pour effectuer le voyage. Ainsi, en cliquant sur l’icône, vous vous départirez de 7 500  unités de  pétrole, de 10 000 d'agriculture et de 10 000 de pêche. Vous devrez également prévoir 5 750 minerais et la même quantité de bois, pour la reconstruction de notre nation. "
choix_B=("Honnêtement... j'aimerais bien garder le pouvoir. Ne prévenez personne que le retour pourrait être possible! Ainsi, je pourrai rester maître de l'île, étant donné qu'une fois au Canada, alors que le programme ARCHE sera terminé, la population voudra beaucoup trop certainement organiser des élections que je ne gagnerais peut-être pas!")
effect_B = ["Population=0", "Karma=1"]
result_B ="Hum... bien... c'est votre choix."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))



evt_À_la_reconquête_du_monde = Events.Event("2019-11-24", "À la reconquête du monde", desc, options)
#####################################
#Éruption vésuvienne
##################################
desc = "Monsieur, il faut que je vous annonce que mes détecteurs ont relevé une activité sismique formidable dans les tréfonds de notre sol. Selon moi, une terrible éruption volcanique pourrait survenir d'un instant à l'autre."
choix_A=("Pff, ce n'est qu'un moyen très peu subtil pour me forcer à faire quitté l'île et à ramener tout le monde sur le continent. Comme si j'allais m'y laissé prendre! Je pense même que... voilà: commande vocale activée, Dé-initialisation du ISaveTheWorld. Bye-bye, je serais sûrement mieux sans toi.")
effect_A = ["MultiplyPop=0"]
result_A ="..."
options =[]
options.append(("Option A", choix_A, effect_A, result_A))



evt_Éruption_vésuvienne = Events.Event("2019-11-26", "Éruption vésuvienne", desc, options)
#####################################
# #
# ##################################
# desc = ""
# choix_A=("")
# effect_A = ["=","=",  "="]
# result_A =""
# choix_B=("")
# effect_B = ["=", "=", "=", "=","=", "=",  "="]
# result_B =""
# choix_C=("")
# effect_C = ["=", "=", "=", "=","=", "=","="]
# result_C =""
# options =[]
# options.append(("Option A", choix_A, effect_A, result_A))
# options.append(("Option B", choix_B, effect_B, result_B))
# options.append(("Option C", choix_C, effect_C, result_C))
# options.append(("Option D", choix_D, effect_D, result_D))

