import Events

##################################
# Epidemie
##################################
desc = "Un terrifiant fléau vient de s'abattre sur nos têtes. Une maladie qui a pris de tel proportion dans le secteur qu'elle en est devenu une épidémie et menace désormais de se répandre sur le reste de l'île. Cette maladie est extrêmement dangereuse et fait déjà plusieurs dizaines de victimes. Que faire?"
choix_A=("Bouclez le secteur, je ne veux personne qui puisse en entrer  ou en sortir.")
effect_A = ["MultiplyPop=0.5", "panic=12"]
result_A = "La mise en quarantaine du secteur à certainement empêché la maladie de se répandre sur le reste de l'île, mais malheureusement, le manque d'aide accordé aux malades a fait en sorte que beaucoup on perdu la vie. Les survivants et les habitants des autres secteurs sont bien sûr heureux d'avoir survécu, cependant ils se demandent à quel point ils peuvent s'attendre à recevoir votre aide advenant qu'une catastrophe leur arrive à eux...  "
choix_B=("Envoyez des équipes collecter les malades et enfermez-les dans n'importe quel édifice dont ils ne pouront pas sortir. À partir de là soignez-les au mieux possible.")
effect_B = ["MultiplyPop=0.1", "panic=12"]
result_B ="Tout est bien qui fini bien. Grâce aux soins prodigué par vos équipes, la majorité des malades ont survécu et la maladie ne s'est pas répandu partout sur l'île. Les gens parlent désormais de vous avec plus de considération."
choix_C=("Par conséquent, envoyez des équipes collecter les malades et emprisonnez-les dans un édifice quelconque et peu important, puis mettez-y feu. Il faut absolument éviter que la maladie se répandent encore plus.")
effect_C = ["MultiplyPop=0.3", "panic=35"]
result_C ="Malheureusement, la chasse aux malades s'est très mal déroulée. Dès que la rumeur d'équipes de nettoyages envoyée par vos soins pour brûler vifs les contaminés s'est répandu, une vague de terreur s'est emparée de tous et chacun. Beaucoup ont tenté, et souvent avec succès, de cacher leur proches pour éviter qu'ils soient capturer. Par ailleurs, les équipes ont énormément usé des informations transmissent par des voisins inquiets et autres, sauf qu'au final, nous avons probablement ainsi aussi bien réglé des querelles qu'empêcher la maladie de se répandre, car plusieurs de ces dénonciations, ont le sait maintenant, étaient fausse. Au final,  la confiance des habitants du secteur sera longue à regagner, car notre remède aura été bien pire que le mal. "
choix_D=("Une maladie à déjà faillit détruire notre monde et je ne laisserai pas cela ce reproduire! Bombarder le secteur infecté jusqu'à ce qu'il ne puisse avoir aucun survivant.")
effect_D = ["Exterminate=0"]
result_D = "Une vague de stupeur s'est répandu sur tout Man'ana'toura dès que la première bombe a explosée. Personne ne voulait croire que vous aviez vraiment fait ça. Mais alors qu'un abominable silence s'installait, une fois le massacre terminé, les gens sont sortis de leur maison, une bougie à la mains dans la noirceur de la nuit, pour rendre hommage à vos victimes. Cette nuit, mue par la tristesse et l'horreur, le peuple chanta un air funèbre et tragique. Les conséquences de cet acte seront graves."

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_epidemie = Events.Event("now", "Epidemie", desc, options)
#####################################  

##################################
# Tremblement de terre
##################################
desc = "Aujourd'hui, une terrible catastrophe à frapper l'île. Alors que tous vivaient leur vie, la terre s'est mise à trembler! L'île a été frappé par des secousses sismiques si importantes que de nombreux bâtiments se sont écroulés, provoquant plusieurs centaines de mort et détruisant de précieuses réserves de ressources! Quel malheur..."
# choix_A=("Je pense de ce fait qu'une mise en quarantaine des malades est tout à fait justifiée; ainsi la maladie ne devrait plus se répandre.")
# effect_A = ["population=-400", "panic=12"]
# choix_B=("J'ai donc décidé que tout les passagers pouvant offrir de leurs temps pour le soins des malades se devront de le faire. La maladie sera ainsi enrayée grâce aux petits soins que prodigueront les autres passagers.")
# effect_B = ["population=-400", "panic=12"]
# choix_C=("Par conséquent, pour éviter de créer des perturbations au seins de l'équipage et nuire à son efficacité, ainsi qu'au moral de la population, à cause de rumeurs sur ce qui ne semble qu'être que des rhumes des plus banals, il faudra étouffer les rumeurs et rassuré tout le monde.")
# effect_C = ["population=-400", "panic=12"]
# choix_D=("Ce qui réduirait à néant toutes chances de re-bâtir notre monde! C'est inadmissible. Pour le bien du plus grand nombre et pour éviter tout risques, nous lancerons par dessus bord tout individu suspecté de maladie, discrètement, bien sûr.")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_seisme = Events.Event("now", "Séisme", desc, options)

#####################################
# Eruption volcanique
##################################
desc = "Des secousses sismiques ont provoqué, comble du malheur, l'éruption du volcan au centre de l'île! La montagne de feu s'est mise a déverser sur nous ses entrailles, des flots de lave en fusion détruisant tout sur son passage! La panique règne en maître sur notre population, même maintenant alors que la lave à arrêté de couler, cependant que les cendres volcaniques brouillent notre atmosphère et suffoque nos concitoyens. La situation est grave, mais malheureusement, seul le temps et une bonne gestion des ressources qu'il nous reste nous permettront de nous relever de cette épreuve cauchemardesque."
#choix_A=("Je pense de ce fait qu'une mise en quarantaine des malades est tout à fait justifiée; ainsi la maladie ne devrait plus se répandre.")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("J'ai donc décidé que tout les passagers pouvant offrir de leurs temps pour le soins des malades se devront de le faire. La maladie sera ainsi enrayée grâce aux petits soins que prodigueront les autres passagers.")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("Par conséquent, pour éviter de créer des perturbations au seins de l'équipage et nuire à son efficacité, ainsi qu'au moral de la population, à cause de rumeurs sur ce qui ne semble qu'être que des rhumes des plus banals, il faudra étouffer les rumeurs et rassuré tout le monde.")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("Ce qui réduirait à néant toutes chances de re-bâtir notre monde! C'est inadmissible. Pour le bien du plus grand nombre et pour éviter tout risques, nous lancerons par dessus bord tout individu suspecté de maladie, discrètement, bien sûr.")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Eruption = Events.Event("now", "Éruption volcaniue", desc, options)
#####################################
# Tsunami
##################################
desc = "Une vague mortelle de terreur vient de déferler sur Man'ana'toura. On déplore aujourd'hui la mort de milliers de personnes. Il est clair que l'on vit de terribles épreuves, mais il nous faut se ressaisir et se redresser."
#choix_A=("")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Tsunami = Events.Event("now", "Tsunami", desc, options)
#####################################
#Tornade
##################################
desc = " Le souffle de la mort est aujourd'hui venu dévaster nos vies. Vers X heures aujourd'hui, une tornade a frappée l'île de plein fouet. Plusieurs de nos infrastructures ont été affectées et de nombreuses familles pleurent leurs proches disparues."
# choix_A=("")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Tornade = Events.Event("now", "Tornade", desc, options)
#####################################
#Revolte
##################################
desc = "Dans le secteur, la vie n'est pas facile. À un tel point que les habitants commence à ce sentir délaissé et pensent pouvoir, une idée de plus en plus répandu, plus facilement survivre et se développer en se gérant tout seul que comme c'est parti maintenant. Un mouvement de pensées plus radicales, plus violentes, commence même à se répandre: Vous feriez exprès de les laisser dans la misère! Des manifestations de moins en moins pacifiques se déclenche un peu partout dans la zone, comment réagirons-nous?"
choix_A=("Faites exécuter publiquement tout les meneurs de ce mouvement, ce sont des traîtres et nous montrerons ce qu'on fait des traîtres!")
effect_A = ["population=-100", "panic=12"]
choix_B=("Bombardez la zone! Une fois que tout le monde sera mort, je peuplerai ce secteur de gens qui me sont loyaux.")
effect_B = ["population=-200", "panic=12"]
choix_C=("Emprisonnez les protestataires les plus criminels, puis demandez aux plus pacifiques de nommez un porte-parole. J'écouterai ses plaintes et nous parviendrons à un arrangement.")
effect_C = ["population=-300", "panic=12"]
choix_D=("… En fait, ils n'ont pas une mauvaise idée. Empêchez quiconque de sortir ou de rentrer dans les zones affectées par les manifestations et coupez leurs toutes arrivées de nourritures. Maintenant, ils vont savoir ce que c'est quand je décide vraiment de les laisser dans la misère. Peut-être reviendront-ils à la raison? Ou pas, c'est tout aussi drôle.")
effect_D = ["population=-400", "panic=12"]
choix_E=("Eh bien... ils manquent de quoi? Envoyez-en comme nécessaires. Il suffisait simplement de demander...")
effect_E = ["population=-200", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "Révolte", desc, options)
#####################################
#Arnaque
##################################
desc = "Bonjour... euh... Commandant... vous savez, à propos de la dernière contruction commandée dans le secteur... Il se trouve que nous avons été arnaqué. Totalement. Toutes les ressources que nous avons envoyées pour sa constructions ont été volées par les travailleurs, qui se sont évanouie dans la nature avec leur butin. Comment réagirons-nous?"
choix_A=("Lancez les forces de police à leur trousse et récupérez nos ressources.")
effect_A = ["population=-100", "panic=12"]
choix_B=("Nous avons d'autres choses à s'occuper. Laissez-les aller, ne passons pas nos ressources sur cela.")
effect_B = ["population=-200", "panic=12"]
choix_C=("Mettez une prime sur leur têtes. Je les veux morts ou vifs, avec les ressources qu'ils ont volées! Ce crime ne restera pas impuni.")
effect_C = ["population=-300", "panic=12"]
choix_D=("Je veux un rapport complet sur la situation; QUI a permis à ces arnaqueurs d'agir, comment et pourquoi. Nous corrigerons notre système bureaucratique en conséquence pour que ce genre d'événement ne se reproduisent plus.")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "Arnaque", desc, options)
#####################################
#Désertification
##################################
desc = "Vous vous rappelez, je vous avais parlé de l'épuisement des sols, de la surproduction et d'autres sujets d'actualité dans le secteur... eh bien, peut-être auriez-vous dû les prendre en compte. La zone commence déjà à ce désertifier. Après trois phases de désertification, la zone deviendra un désert et perdra énormément de son intérêt et de sa capacité de production de ressources."
# choix_A=("")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Désertification = Events.Event("now", "Désertification", desc, options)
#####################################
#Surpopulation
##################################
desc = "Commandant! Du secteur montent plusieurs plaintes à propos du manque d'espace pour vivre, de la surpopulation des lieux! Si cela continu comme ça, les conditions de vie des habitants du secteur vont rapidement se dégrader. La meilleurs solution serait probablement de réglementer la natalité ou encore d'effectuer un transfert de population."
# choix_A=("")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Surpopulation = Events.Event("now", "Surpopulation", desc, options)
#####################################
#Vague de crime
##################################
desc = "La criminalité est trop élevée et cela ce traduit par une vague de crimes de tout acabi. Des gens meurent, ce font volés, arnaquer, etc. Il faut faire refluer cette criminalité, sinon la région tombera définitivement dans le chaos."
# choix_A=("")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Vague_de_crime = Events.Event("now", "Vague de crime", desc, options)
#####################################
#Épuisement du pétrole
##################################
desc = "Il n'y a plus de pétrole à exploiter dans la zone!"
#choix_A=("Il n'y a plus de pétrole à exploiter dans la zone!")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Épuisement_du_pétrole = Events.Event("now", "Épuisement du pétrole", desc, options)
#####################################
#Épuisement du gibier
##################################
desc = "Il n'y a plus de gibier à chasser dans la zone!"
#choix_A=("Il n'y a plus de pétrole à exploiter dans la zone!")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Épuisement_du_gibier = Events.Event("now", "Épuisement du gibier", desc, options)
#####################################
#Déforestation totale
##################################
desc = "Il n'y a plus de forêt à exploiter dans la zone!"
#choix_A=("Il n'y a plus de pétrole à exploiter dans la zone!")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Déforestation_totale = Events.Event("now", "Déforestation totale", desc, options)
######################################
# Épuisement de la faune aquatique
##################################
desc = "Il n'y a plus de poisson à pêcher dans la zone!"
#choix_A=("Il n'y a plus de pétrole à exploiter dans la zone!")
# effect_A = ["population=-100", "panic=12"]
# choix_B=("")
# effect_B = ["population=-200", "panic=12"]
# choix_C=("")
# effect_C = ["population=-300", "panic=12"]
# choix_D=("")
# effect_D = ["population=-400", "panic=12"]
options =[]
# options.append(("Option A", choix_A, effect_A))
# options.append(("Option B", choix_B, effect_B))
# options.append(("Option C", choix_C, effect_C))
# options.append(("Option D", choix_D, effect_D))

evt_Épuisement_de_la_faune_aquatique = Events.Event("now", "Épuisement de la faune aquatique", desc, options)
#####################################
#Feu de forêt
##################################
desc = "Un feu vient de se déclarer dans la principale forêt du secteur! Déjà, il prend une ampleur exponentielle et se répand un peu partout, dévastant la ressources et faisant fuir tout les animaux! Nos scieries ont même commencé à se faire affecter par les flammes."
choix_A=("Envoyer un hydravion, c'est pas mal tout ce qu'on peut faire...")
effect_A = ["population=-100", "panic=12"]
choix_B=("Envoyer un hydravion et envoyez aussi des pompiers pour pour protéger les scieries qu'il nous reste.")
effect_B = ["population=-200", "panic=12"]
choix_C=("Pourquoi gaspiller des ressources pour sauver la vie d'un arbre?!?")
effect_C = ["population=-300", "panic=12"]

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))



evt_Feu_de_forêt = Events.Event("now", "Feu de forêt", desc, options)
#####################################
#Aleksei Vasilev
##################################
desc = "Bonjour, camarade! Il se trouve que je mène un commerce plutôt important ici et que mes moyens de production sont très élevé. Cependant, pour accroître la puissance de mon entreprise, il me faudrait trouver une plus vaste clientèle... comme l'état lui-même! Une association serait extrêmement profitable pour nos deux parties. Donc voilà le marché : je fais construire à mes frais l'une de mes usines dans le secteur de votre choix et je la met à votre disposition, ce qui va permettre de grandement augmenter le rendement de tout les bâtiments produisant des ressources dans le secteur. En échange, nous serions prioritaire quand viendrait le temps de faire construire quelque chose par l'État. Qu'est-ce que vous en dites?"
choix_A=("C'est bien parfait, nous avons un accord!")
effect_A = ["population=-100", "panic=12"]
choix_B=("Ce n'est pas très... sportif, voire même légal, par rapport à vos concurrents")
effect_B = ["population=-200", "panic=12"]
choix_C=("Nous merci cher monsieur, j'ai déjà tout ce qu'il me faut.")
effect_C = ["population=-300", "panic=12"]

options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_Aleksei_Vasilev = Events.Event("now", "Aleksei Vasilev", desc, options)
#####################################
#(Ré-)Émergence du crime organisé
##################################
desc = "Malheureusement, parmi les gens que nous avons amené avec nous, il se trouve qu'il y avait certains membres de la Bradva, une organisation criminelle russe, qui ont trouvé le moyen de passer à travers ma vigilance lors de la sélection des passagers. Ils ont renforcé dans l'ombre leur pouvoir, et sont sur le point d'avoir totalement rebâtie leur organisation, en convertissant et soudoyant! Que faire?"
choix_A=("Faites-en venir le membre le plus puissant possible.")
effect_A = ["population=-100", "panic=12"]
choix_B=("Ignorons-les, je n'ai pas le temps de m'en occuper.")
effect_B = ["population=-200", "panic=12"]
choix_C=("Envoyez tout nos effectifs contre ces criminelles, nous les traduirons en justice et par la vérité et la loi, ils tomberont. Faites convoquer une conférence de presse, je ferai un discours sur le courage, la justice et les responsabilité à la population, qui va devoir nous aider.")
effect_C = ["population=-300", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_Émergence_du_crime_organisé = Events.Event("now", "(Ré-)Émergence du crime organisé", desc, options)
#####################################
#Négociation avec la Bradva
##################################
desc = "Commandant, la Bradva vous envoie l'un de ses membres les plus influent pour initier le dialogue. « Bonjour, camarade! Qu'est-ce que l'on peut faire pour vous? »"
choix_A=("J'ai eu vent de vos activité de plus en plus criminelles et de votre puissance grandissante : Je veux pouvoir en profiter et pour cela, j'aimerais que nous passions un marché, pour la seconde fois. (Après plusieurs heures de négociation, vous acceptez de fermer les yeux sur leur activités  en échange d'apport en ressources réguliers.)")
effect_A = ["population=-100", "panic=12"]
choix_B=("2. Je vous ais fait venir pour pouvoir voir un puissant de la Bradva ainsi que pour le capturer et m'en servir pour la faire tomber. Arrêtez-le.")
effect_B = ["population=-200", "panic=12"]
choix_C=("Un criminel tel que vous ne mérite pas de vivre. Faites-le exécuter.")
effect_C = ["population=-300", "panic=12"]
choix_D=("Pour continuer à exister, il va falloir me payer : vous avez amenez ce que je vous ais demandé? Oui, parfait. (Vous vous assurez que les chargements de ressources amené par Aleksei comme pot-de-vin ont été déchargés.) Je dois vous avouer qu'honnêtement, j'ai menti. Arrêtez ce criminel, et torturer-le si nécessaire pour obtenir toutes les informations qu'il possède.")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_Négociation = Events.Event("now", "Négociation avec la Bradva", desc, options)
#####################################
#Guerre contre la Bradva
##################################
desc = "Vous venez de déclarer la guerre à la Bradva et par la même occasion, à tout le crime organisé qui s'est établit sur l'île. Les criminels se rassemblent et montent leur sinistre projets, manœuvrant dans l'ombre pour prendre le contrôle total de Man'ana'toura, par l'intimidation et la corruption, dans le but de plonger votre œuvre dans le chaos et la peur."
choix_A=("Lutter contre la Bradva.")
effect_A = ["population=-100", "panic=12"]
choix_B=("Lui faire des excuses publiquement et lui garantir la non-ingérence de l'état dans leur affaires.")
effect_B = ["population=-200", "panic=12"]
choix_C=("Ignorer la Bradva.")
effect_C = ["population=-300", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_Guerre_contre_la_Bradva = Events.Event("now", "Guerre contre la Bradva", desc, options)
#####################################













# Recherche

#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))

evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
#
##################################
desc = ""
choix_A=("")
effect_A = ["population=-100", "panic=12"]
choix_B=("")
effect_B = ["population=-200", "panic=12"]
choix_C=("")
effect_C = ["population=-300", "panic=12"]
choix_D=("")
effect_D = ["population=-400", "panic=12"]
options =[]
options.append(("Option A", choix_A, effect_A, result_A))
options.append(("Option B", choix_B, effect_B, result_B))
options.append(("Option C", choix_C, effect_C, result_C))
options.append(("Option D", choix_D, effect_D, result_D))


evt_ = Events.Event("now", "", desc, options)
#####################################
