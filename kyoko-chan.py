
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Chat

import os, math, time, random, time, schedule, sys


# Comandi vari:
# if update.message.chat.type == Chat.PRIVATE:			se è vero vuol dire che sei in una chat privata altrimenti sei in un gruppo
# nick = update.message.from_user.username	nick diventa L'USERNAME di chi ha usato il comando o triggerato l'azione
# nick = update.message.from_user.first_name	nick diventa il nome dell'utente
# nick = update.message.from_user.last_name	nick diventa il cognome che può non essere utilizzato


# Comando start, "avvia" il bot in una chat
def start(bot, update):
    nick = update.message.from_user.username
    #update.message.reply_text("*testo*",
     #                         parse_mode="markdown")  # Questo comando invia "testo" in grasseto grazie a "parse_mode="markdown" "
    #print("%s ha usato start" % (
    #nick))  # Questo comando printa nella console l'ora a cui nick ha utilizato questo comando


# Comando help, "avvia" descrive i comandi del bot
def help(bot, update):
    nick = update.message.from_user.username
    #update.message.reply_text("testo",
    #                          quote=False)  # "quote=False" vuol dire che invierà il messaggio non rispondendo all'utente, di default è True nei gruppi e False nelle chat private
    #print("%s ha usato help" % (nick))


    # Qui inizia il reader, il reader legge ogni singolo messaggio che il bot vede

def BenvenutoAddio(bot, update):
    #chat_id = update.message.chat.id
    #chat_name = update.message.chat.title
    #nuovo = update.message.new_chat_members
    #uscito=update.message.left_chat_member
    #reply = update.message.reply_text

    #try:
 
    #    if nuovo!=None:
    #        nome = nuovo[0]['first_name']
    #    if nuovo!=None:
    #        reply("Benvenuto/a " + nome +" in "+chat_name+"\t\nnya~")
    #        print(nome + " è entrato nel gruppo " + chat_name)
    #    if uscito:
    #        nome = nuovo[0]['first_name']
    #    if uscito:
    #        update.message.reply_text("Prima paga e poi esci")
    #        print(nome+ " è uscito dal gruppo " + chat_name)
    #except Exception as err:
    #    print(err)

    try:
        nick = update.message.new_chat_member['first_name']
        chat_name = update.message.chat.title
        text = "Benvenuto/a " + nick +" in "+chat_name+"\t\nnya~"
        update.message.reply_text(text, quote=True)
        print(nick + ' è entrato nel gruppo %d' % chat_name)
        return
    except:
        pass
    try:
        nick = update.message.left_chat_member['first_name']
        chat_name = update.message.chat.title
        text = "Addio " + nick + "\t\nnya~"
        update.message.reply_text(text, quote=True)
        print(nick + ' è uscito dal gruppo %d' % chat_name)
        return
    except:
        pass




def reader(bot, update):
    try:
        cont = update.message.text  # Contenuto del messaggio, è essenziale ovviamente per poterlo analizare
        contLower = cont.lower()  # Questo rende il testo tutto minuscolo
        idg = update.message.chat.id  # ID univoco del gruppo da cui proviene il messaggio
        # l'ID della chat se in privatosarebbe l'ID dell'utente
        idu = update.message.from_user.id  # ID univoco dell'utente da cui proviene il messaggio
        msg = update.message.text.lower()
        reply = update.message.reply_text
        rnq=bot.sendMessage
        name = update.message.from_user.first_name
        chat_id=update.message.chat.id
        user_id=update.message.from_user.id


        if update.message.reply_to_message is not None:
            name2 = update.message.reply_to_message.from_user.first_name
            nick2 = update.message.reply_to_message.from_user.username
            user_id2 = str(update.message.reply_to_message.from_user.id)
        else:
            name2 = None
            nick2 = None
            user_id2 = None
        botname = bot.first_name.lower()
        if " " in botname: botname = botname.split()
        botname =''.join([i for i in botname if i.isalpha])

        trigger = {
                   "interazioni": {
                                    "uccidilo", "uccidila", "abbraccialo", "abbracciala", "headpattalo", "headpattala", "biscotto",
                                    "bestemmia", "impuzzolentiscilo", "impuzzolentiscila", "ciao", "portami fortuna"
                                  },
                   "interazioni2": {
                                    ""
                                   },
                   "interazioni3": {
                                    "bsd","nanbaka","naruto","ft", "rakudai kishi", "shokugeki", "shakunetsu", "kh"
                                    },

                   "equal": {
                              "rip"
                             }
                   }

        risposte = {
                    "ciao": [
                             "Ciao {}".format(name)

                    ],

                    "impuzzolentiscilo": ["Nya~\t\n*butta {} nella spazzatura*\t\nEcco adesso puzza".format(name2)],

                    "impuzzolentiscila": ["Nya~\t\n*butta {} nella spazzatura*\t\nEcco adesso puzza".format(name2)],

                    "uccidilo": [
                                 "*tira fuori gli artigli e uccide {}*".format(name2), "*richiama il Rashoumon Agito e disintegra {}*".format(name2)
                                ],
                    "uccidila": [
                                 "*tira fuori gli artigli e uccide {}*".format(name2), "*richiama il Rasoumon Agito e disintegra {}*".format(name2)
                                ],
                    "abbraccialo": [
                                    "Nya~\t \n*abbraccia {}*".format(name2),"No, non voglio abbracciarlo", "No, {} puzza!".format(name2)
                                    ],
                    "abbracciala": [
                                    "Nya~\t \n*abbraccia {}*".format(name2),"No, non voglio abbracciarla", "No, {} puzza!".format(name2)
                                    ],
                    "biscotto": [
                                 "Certo, tutti i biscotti che vuoi\t \nNya~",
                                 "Subito, *lancia un biscotto a {}*\t \nNya~".format(name),"Non voglio"
                                ],
                    "headpattalo": [
                                    "Nya~ *headpatta {}*".format(name2)
                                    ],
                    "headpattala": [
                                    "Nya~ *headpatta {}*".format(name2)
                                    ],
                    "": [
                         "Eccomi, nya~"
                        ],
                    "bsd": [
                            "<a href='https://68.media.tumblr.com/368aa48890196b6f04cc4b518e68c68a/tumblr_otnqnvSrWp1w2ucj8o1_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/f2986238ca783d0f073ef8b7f5c8dce6/tumblr_otnqnvSrWp1w2ucj8o9_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/8c13d51727e3fc7630909bbc84da475c/tumblr_otnqnvSrWp1w2ucj8o2_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/1a4c642adb4320570a3078ac2d89d09d/tumblr_otnqnvSrWp1w2ucj8o3_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/69f7ff259a551e00bec296c8b5c7c4cf/tumblr_otnqnvSrWp1w2ucj8o5_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/bac36c6e810ab310d41092921830df38/tumblr_otnqnvSrWp1w2ucj8o4_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/cc89a2d310794e8ed894c2e357805e05/tumblr_otjbgzbmWQ1wqyc4yo1_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/28c37184bf5f42592a3514dc45768c2d/tumblr_otgtfwYSqn1w2ucj8o1_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/4643373e9c069247a606a3d56f617e1e/tumblr_otgtfwYSqn1w2ucj8o3_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/dbba4aed080cfa20797e4ba18f944c33/tumblr_otgtfwYSqn1w2ucj8o2_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/103b14637e209dad31b4d87c61738611/tumblr_op6nvwUO7V1wnm2puo1_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/a28a2ec421e57fce2a3c0456058361f6/tumblr_op6nvwUO7V1wnm2puo2_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/a7266b87ebe9c4542eac77b2f5fdabc4/tumblr_op6nvwUO7V1wnm2puo3_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/c41f1de173661cef547677cf00d40404/tumblr_oib0i6W0HF1vl3h3so2_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/b9b761cacdf7ae80af58ea59295fdcbd/tumblr_oiaowlTZY41vl3h3so1_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/6ffa5fb3d55a006fd7549d191e13e8aa/tumblr_oiaowlTZY41vl3h3so2_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/bd89420994252120c2ac4b6fa2dcca61/tumblr_ofylf4RNAI1um42ooo1_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/72a68d7033496ba99da7e46982c444e5/tumblr_ofylf4RNAI1um42ooo8_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/5f38ad737d380af9984f16739333c5fe/tumblr_oesc7iHCj81qg7cgfo1_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/02ff1fe4431a2fd59605479228903ccd/tumblr_oesc7iHCj81qg7cgfo2_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/0e8de893dee50504d23b9e164312e35e/tumblr_oen3huDn1N1v9hzmko1_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/73643fd679042718fc2b3b18c281ce00/tumblr_odx40qmrwf1v9hzmko1_1280.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/9d3a24342a9ff0f8fc21051cb5dd4122/tumblr_ob5dc2vJ7c1v9hzmko1_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/11366bdf0d49d9465ed4b7fd17bd2fd9/tumblr_o9767sidda1vxlcoqo3_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/67634c11258ae853c646afc85ccf99a0/tumblr_o8z67h3rDF1vxlcoqo1_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/591d4d887fc5ad5f36f21a61f5daff73/tumblr_o8klfam9GY1vwdqc3o1_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/fdde355e0f40ec513f7e88ac76be62b4/tumblr_o8gvt9xGjw1s9jnzyo9_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/17046d02b4756cfcde4ef8e48fffab0c/tumblr_o8gvt9xGjw1s9jnzyo10_400.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/1e565ee798839b31caedcd8f19b4f351/tumblr_o5907je1fA1s2o7ljo1_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/1313ba48aa60334a89b7c42ef4b71a04/tumblr_o5907je1fA1s2o7ljo2_540.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/4d9c41c1cfc141a83a3ab743a76a8eff/tumblr_ofylf4RNAI1um42ooo10_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/c8b487a1051bd31274a6f37b454ebed9/tumblr_ofylf4RNAI1um42ooo9_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/2c79697fb57b5b4167cfd378a74c2da3/tumblr_ofylf4RNAI1um42ooo6_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/d7aa8b46a49d54f0d6538891d0e41039/tumblr_ofylf4RNAI1um42ooo5_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/b2629c1262a425b296481ac2f7c7df08/tumblr_ofylf4RNAI1um42ooo4_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/cc16c54a754818d04623a0672280aa70/tumblr_ofylf4RNAI1um42ooo3_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/11a676b94398a4177ecd59e3118add2b/tumblr_ofylf4RNAI1um42ooo2_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/dcc836615afb6ea203d9bc563aa3def5/tumblr_oib0i6W0HF1vl3h3so1_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/6a1b13f107f8881e8700c8cf77eebf56/tumblr_oib0i6W0HF1vl3h3so3_500.gif'>bsd</a>",
                            "<a href='https://68.media.tumblr.com/720d4fca50c73f3847e2f9add0753d58/tumblr_op6nvwUO7V1wnm2puo5_500.gif'>bsd</a>" ],
                    "nanbaka" : [
                                 "<a href='https://68.media.tumblr.com/1888abcd608c07e1069b7969da1eb460/tumblr_okb78lobrB1velul7o1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/ff152f8d2447bfafd225c618ac537dce/tumblr_on6rhf5crA1velul7o1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/6e7eb183be949ecadb26a2c19af5bec6/tumblr_ophnbxj3QG1v30j2so1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/d96b0e303b5521733deb5a786ce91550/tumblr_om45sfQYOS1velul7o1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/230e842304a762f4b5ee1c001a733932/tumblr_omtxs431JV1qlomhno1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/b4375c1aef7db4cad7f942ab5d6c1498/tumblr_on75ufFwkn1vjc1jro1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/d6e2d12c35f51e374f1652e46134f64c/tumblr_ohseypPMWJ1uku9tco1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/3e85902f5180f78e442397a5546c8fbf/tumblr_om40p4gzGI1tqsu3ro1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/5df93f1f5c072490e1da7b3589075d84/tumblr_okb709GT2m1vgfg91o2_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/92aa892495be63490f8fbc12aa0a538f/tumblr_oldxj8SvmP1qg9t1lo1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/697f7ef2f7741a1da1a5979f46ebbe06/tumblr_oiz1gcmGKR1r60zuio1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/44bb25be67cbf2845214d00d35c40cb0/tumblr_on4csiexPm1v30j2so1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/f32232c378e43d9e25c0a49b74144182/tumblr_olwoxtVrp61w58oyno1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/2a08e9464eb7cb11b17d0a1dd3a341d5/tumblr_oja191SrsV1s8gfjqo1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/ca59598d7df18367cb66d9ad030ccee4/tumblr_omwqg6xwxt1v30j2so1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/5a18291389626f04c2b9277e3438a1b4/tumblr_osufpkisui1vgfg91o1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/4644faf927b87c78002399fb637b0adc/tumblr_omy765Hj8G1v30j2so1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/c2669aac95842d2603f09d30e30273ed/tumblr_ohaujoruS11s8gfjqo1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/58c0dc6c6b44ba0f082b5a361526384e/tumblr_oewh07R74T1ri2bgao1_500.gif'>nanbaka</a>",
                                 "<a href='https://68.media.tumblr.com/cbe65de38842f044a0bd0a3eca3635df/tumblr_oh2h8vwG261velul7o1_500.gif'>nanbaka</a>"
                                ],
                    "naruto": [
                                "<a href='https://68.media.tumblr.com/2b83f4b79cf0870ed93f98e619ecf96e/tumblr_ovw0yiDXR51vzjl3fo1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/f31dd7747bbc2944219c5bb85bec81be/tumblr_ovi4etA1GS1qfeem4o1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/14de17b54263e233a50684de69a2c69b/tumblr_ov4a7eVeSn1rddilvo1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/b2187640be59973b1d452991619de812/tumblr_ov2brajjdb1wrm9xio1_250.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/d5294b436fc58a90fda3f481e160bb64/tumblr_ov1tacuckd1wylmu4o1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/8d3b665014ba18f76f68ab4676ee531a/tumblr_ov0hoo7wFt1wya8szo2_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/ab81c43a7c2696585501c2ed391e5925/tumblr_ouy8hqdfDN1wof0cmo1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/2a48a35f06fb4071b6f194b532f12626/tumblr_otzkk233rO1te23s4o1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/d741f1e697e3d44c9a3c8436671f2bcf/tumblr_osydwh8cUR1ui7oe1o3_540.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/47f31149f550364058e91d452ed66f23/tumblr_osydwh8cUR1ui7oe1o4_540.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/7b51e17576b7ec740436a7f0e314370d/tumblr_osydwh8cUR1ui7oe1o1_540.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/f48197f1c143577d58020c4a559f035b/tumblr_oswqkiHSkq1wsjjgbo1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/050a6911c0d23609cf4bd534108cd97d/tumblr_ostd4g1aBO1wnugwfo2_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/73a3f63dafece1c0c0508676daabce45/tumblr_ostd4g1aBO1wnugwfo5_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/841c39ea93cca61a4768e26628db79a2/tumblr_ostd4g1aBO1wnugwfo6_400.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/a56520a3ca120e45558ee1fa256bdd93/tumblr_ostd4g1aBO1wnugwfo8_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/d31927b7626042eb762b66f048bd49c1/tumblr_ostd4g1aBO1wnugwfo10_500.gif'>naruto</a>",
                                "<a href='http://68.media.tumblr.com/17656941d66d0b552c5c86a21f396d39/tumblr_osfpwqIofM1rqe0rbo1_540.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/19ce894fb7bfd6eb9170d7f780d0a58f/tumblr_orxfdzpTRW1vh89pzo1_500.gif'>naruto</a>",
                                "<a href='https://68.media.tumblr.com/9666036b48b6564b1935c6758f82a1ad/tumblr_ora1ncworb1qfeem4o3_500.gif'>naruto</a>"
                                ],
                    "ft": [
                            "<a href='https://68.media.tumblr.com/a91a79f02febe4ae443a97820769ae41/tumblr_ouoapa9MOU1unnwwto2_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/20f7e78d238b7099b97b5e5669256b57/tumblr_ouoapa9MOU1unnwwto3_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/43b4a717afec6c072b2c77287a5b0a5d/tumblr_ouoapa9MOU1unnwwto4_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/84ea11d3631162d2f702033039fa0ac8/tumblr_ouoapa9MOU1unnwwto5_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/d4af93b9e9e5dc3f35e3a0f7033c4fb1/tumblr_ouoapa9MOU1unnwwto6_540.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/f0c1a28dbf606ce3b059cc410d658179/tumblr_ouoapa9MOU1unnwwto8_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/ad4221b21c7ad358273e4e44f64881d6/tumblr_ouoapa9MOU1unnwwto9_540.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/1948c46462e9cc3cecc89742c958f6c0/tumblr_othzn7rWPL1taoarbo1_400.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/5ca92466cd9f5137331ed382b2dc0a45/tumblr_othzn7rWPL1taoarbo8_400.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/2c22eef6bfd43041d98456d4dc0692bf/tumblr_othz64xGrn1taoarbo6_400.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/1f7b9f8d501caccf98f3fd97e8d13298/tumblr_othz64xGrn1taoarbo2_400.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/93cbb2d7b0b44586b5cac8d4d673e5fa/tumblr_othz64xGrn1taoarbo7_400.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/a3c76857d4a20809035c6878ba0c9423/tumblr_othz64xGrn1taoarbo5_400.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/76f915e702621c49fcd58c4d3f90c66b/tumblr_os266bAaSL1unnwwto3_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/54fc4c4487a878d4b7c7a71df5291f33/tumblr_orzuxvfxrp1unnwwto1_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/c9443a0b776dfacb9ee1e61e3bc9ef08/tumblr_or71dmqrZK1uiz4mko3_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/b12ebced507a47fcf964a97171a76e79/tumblr_or71dmqrZK1uiz4mko5_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/d69c9d475f1292120d5522d3af8d24bd/tumblr_oqzy16h5w21uiz4mko4_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/5527ae07418e0759fafd6e4389162f48/tumblr_oqzy16h5w21uiz4mko3_500.gif'>ft</a>",
                            "<a href='https://68.media.tumblr.com/5f206f30802bf8aefc01fb60112c388e/tumblr_omvdy8ly1w1rjf4f5o1_500.gif'>ft</a>"],
                    "rakudai kishi" : [
                                        "<a href='http://68.media.tumblr.com/e092c6421f7c1a06325e60e5ac3e3c9b/tumblr_nxkocnlR6H1unbsixo1_540.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='http://68.media.tumblr.com/0a340fa186c68c5580339c00459c287a/tumblr_nxknazWYyI1unbsixo1_540.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/98024745bd68e96edc0922b5f24e255c/tumblr_nzmik9NfpN1qimk8ao3_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/e145706e668a00aab79f13dac6f564d2/tumblr_nxc0nx0PZL1tydz8to1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/681b88865885f36d016bedb402c8823e/tumblr_ol185zIZZv1uvxchjo4_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/6273e82719026046e6fbce9c738547b5/tumblr_nw0puiq7tv1s3dw0xo1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/a619ec0fd70a048644932d522624848d/tumblr_ny6s4zZsru1u0tkulo1_r2_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/cb2d9b43bcd7afb493b022a481c31afb/tumblr_nxboz95lWt1so2t73o1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/46ac9362b8e5e08480ea2b50aec46425/tumblr_nzn4dlwkVT1uq3u3ko2_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/1393d5f3218a3466f8d6323540ef9853/tumblr_nwdwdjDchr1ttu8odo1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/f020c3508fab3316da36585ef7e6dca7/tumblr_nzoflbEjPJ1s21xzoo1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/1efb66c07ce1fdf5aef5e5bba30cded1/tumblr_nx3j22CCSU1ttu8odo1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/57f08ef9b3f91cc15f368c923bdc14bf/tumblr_nwjov49t9i1smmps3o2_r1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/7da47846c8fb60190f28406eaa27cc02/tumblr_o6f62iFGR31snbyiqo3_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/136abd36fe7de45b57b25388c88f08ad/tumblr_nwz332rZGI1tydz8to1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/21ad799678dd1e0d7ad64dfe19e7c111/tumblr_nwqidiBVCJ1ttu8odo1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/17805ede69551301eb5e75ee09610e13/tumblr_nz11zfjLP21qekr89o1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/14a5b1683870c111c784a2595789c242/tumblr_o0z8b71cCx1uli1i6o1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/96099444b0db1ae9a63ac458da547600/tumblr_nwskb86GlG1tydz8to1_500.gif'>rakudai kishi no cavalry</a>",
                                        "<a href='https://68.media.tumblr.com/a05bc7fc4832892a33299cb4c1a708d3/tumblr_nz9f5gzxlO1rd6sdio1_500.gif-'>rakudai kishi no cavalry</a>"],
                    "shokugeki": [
                                    "<a href='https://68.media.tumblr.com/4ff996131e9c9416b6b4ddade2b0e225/tumblr_ofof83nDNG1vi5fvdo1_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/c6b4646e08f252c147cbda4addfda6a4/tumblr_o7hqdcSkkR1vq4578o1_540.gif'>shokugeki no soma</a>",
                                    "<a href='http://68.media.tumblr.com/a02f496c695c710d1163eb1450d95beb/tumblr_nyp8o2XQu31src42wo1_540.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/de8d6a55b414b219f7bcbfdf1204a788/tumblr_nv92kcVxxA1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/ca1c6ee7ade81b7b009d5eb9ffaa515a/tumblr_nsgqpdTNEV1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/9b4ef8cef5998d4bb35a7bde79fbfb78/tumblr_nrosuqaQGB1uoves2o1_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/682cccf8963660ea4feb95db338fe384/tumblr_nqxkhtj7Z71uoves2o1_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/042a46475fae0aa0ba2dea30d232cf49/tumblr_nqxkcwHENE1uoves2o1_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/cf43daa9b41dc152b5e5ca3478796a83/tumblr_nqb3rzY4rH1tw9r1lo1_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/dd987307f124ea56d0e4c90ddf758282/tumblr_npv6ygGJEU1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/3ab126a426d5f3fea6785f04a4cf39e3/tumblr_nputlnSvCh1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/c5ed358164cbb591cbbc2e46f49d2bb6/tumblr_npj5px4rG41sg9gi2o1_540.gif'>shokugeki no soma</a>",
                                    "<a href='http://68.media.tumblr.com/f026f5ef337b9db60e291b4c6cab0e38/tumblr_nnc2wqetfZ1s2c1h4o1_1280.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/b67670b9494a3c06372be154f018b811/tumblr_nms5yha74D1sg9gi2o2_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/f384b61c84489454f234aff75ced200c/tumblr_nmpq4ehyLM1sg9gi2o2_500.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/5aa45f286e9b73c8eb95d8f846d1df11/tumblr_nmnfi99rYt1qeph4io3_250.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/3b847a6d46247080fd88356ba0136331/tumblr_nm9p34Dnnt1sg9gi2o1_500.gif'>shokugeki no soma</a>",
                                    "<a href='http://68.media.tumblr.com/f9088d7172f9ec642ca5c5f94d62e330/tumblr_nm91uvPXef1toqhwfo1_540.gif'>shokugeki no soma</a>",
                                    "<a href='http://68.media.tumblr.com/b4beb6c54302a502dd1dae1bc75973da/tumblr_nm95dsxcho1toqhwfo1_540.gif'>shokugeki no soma</a>",
                                    "<a href='https://68.media.tumblr.com/ba86c08e07442d0a4654f979b8661a15/tumblr_nqxkf2EKnF1uoves2o1_500.gif'>shokugeki no soma</a>"],
                    "shakunetsu": [
                                    "<a href='https://68.media.tumblr.com/669da82d96e69ba059032f305c94d98d/tumblr_ofkieg0ynV1s4qvrdo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/ed2f91c93576f29e76e3cc8668ac1b41/tumblr_oigjfohifD1s4qvrdo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/4bfe0a4149f506b7680a82cb445ab416/tumblr_oek62w5wXq1vaigheo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/b277686186a46c173ec22efbc6b2549a/tumblr_ohi8fvSLTl1uqldi9o1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/041f721a1c3a91e41febd6b66bc6af07/tumblr_ohkg2q5ntm1t3uwllo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/a49ea5bb062e68e69e00c935a7047d10/tumblr_oei9cr9tBW1sn2bkjo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/aee4b743286dc242d9f67c0f9a8e845e/tumblr_ogns6nTSHP1rd6sdio1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/61805789bfdb5e9ce8ea2fbec71f59fe/tumblr_oi3qabB0601tjh5d1o1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/655d6f834013f5684920ed22bb6955a9/tumblr_oekb09sNhh1vvvyj7o1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/e9d78308b39cc93fa61bce34b04ca3d9/tumblr_oh19hzzpG81rd6sdio1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/bb9468526bf76869b67728b299c4ada7/tumblr_ohe9c25aLh1vaigheo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/f2eebb7d4afeb141cdb7e848a2881b1c/tumblr_ofm4eu9CXg1srr81uo1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/b9e8706938ed212f235f257ac6e4bd25/tumblr_oeuysxkvGr1twgfw0o1_500.gif'>shakunetsu no takkyuu musume</a>",
                                    "<a href='https://68.media.tumblr.com/84486804d1add2c5c18ebfddee607147/tumblr_ohbfbedzTP1tdriooo1_500.gif'>shakunetsu no takkyuu musume</a>"
                                    ],
                    "bestemmia": [
                                  "Dio canguro col soffitto basso",
                                  "Dio scalzo nella valle dei chiodi",
                                  "Dio scacciapreti assatanati",
                                  "Madonna incaprettata",
                                  "Dio lurido",
                                  "Gesù lavastoviglie",
                                  "Mannaggia Gesù Cristo in croce incaprettato da quella maialona della Madonna bastarda mentre si masturbava con il martello di Giuseppe",
                                  "Madonna stuprata",
                                  "Madonna spellata",
                                  "Gesù tavernello"
                            ],
                    "kh":["<a href='https://78.media.tumblr.com/00d071f6ec788a44d27e3431ecc94482/tumblr_mfrmcqEGy81roki0po1_500.gif'>kingdom hearts</a>",
                          "<a href='https://78.media.tumblr.com/c5735884573b7adc10ed8ddda2dc0406/tumblr_p1w2n5sRut1w0q2jqo6_400.gif'>kingdom heart</a>"],
                    "rip": [
                            "Chi è morto? nya~"
                           ]

                   }

        risposte2= {
            "ciao": ["Ciao papi"],
                    "uccidilo": [
                                 "Nya~\t \nNon uccido mio padre.\t \n*tira fuori un coltello e uccide {}*".format(name)
                                ],
                    "uccidila": [
                                 "Nya~\t \nNon uccido mio padre\t \n*tira fuori un coltello e uccide {}*".format(name)
                                ],
                    "abbraccialo": [
                                    "Nya~ subito\t \n*abbraccia papi*"
                                    ],
                    "abbracciala": [
                                    "Nya~ subito\t \n*abbraccia papi*"
                                    ],

                    "headpattalo": [
                                    "Nya~ *headpatta {}*".format(name2)
                                    ],
                    "headpattala": [
                                    "Nya~ *headpatta {}*".format(name2)
                                    ],
                    "impuzzolentiscilo": ["No, non impuzzolentisco il mio papi\t\n*butta {} nella spazzatura*\t\nEcco adesso puzzi".format(name)],

                    "impuzzolentiscila": ["No, non impuzzolentisco il mio papi\t\n*butta {} nella spazzatura*\t\nEcco adesso puzzi".format(name)],
                    }

        risposta3 = {"ciao": ["Ciao zia"],
                     "uccidilo": [
                         "Nya~\t \nNon uccido mio zia.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "Nya~\t \nNon uccido Tsun.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "No, visto che poi papi mi potrebbe cancellare"
                     ],
                     "uccidila": [
                         "Nya~\t \nNon uccido mia zia\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "Nya~\t \nNon uccido Tsun.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "No, visto che poi papi mi potrebbe cancellare"]

                     }

        risposta4 = {"ciao": ["Ciao zio"],
                     "uccidilo": [
                         "Nya~\t \nNon uccido mio zio.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "Nya~\t \nNon uccido mio zio.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "Nya~\t \nNon uccido mio zio.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "*tira fuori gli artigli e uccide {}*".format(name2)
                     ],
                     "uccidila": [
                         "Nya~\t \nNon uccido mio zio.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "Nya~\t \nNon uccido mio zio.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "Nya~\t \nNon uccido mio zio.\t \n*tira fuori un coltello e uccide {}*".format(name),
                         "*tira fuori gli artigli e uccide {}*".format(name2)
                     ]
                     }




        if msg.startswith(botname) or msg.endswith(botname):
            for interazione in trigger["interazioni"]:
                if interazione in msg:
                    if name2==None:
                        if interazione!="biscotto" and interazione!="bestemmia" and interazione!="ciao":
                            reply("No...", quote=False)
                    elif name2=="Kyoko-chan":
                        reply("Non posso", quote=False)
                    elif user_id2=="236408435":
                        reply(random.choice(risposte2[interazione]), quote=False)
                    elif user_id2=="410255671":
                        reply(random.choice(risposta3[interazione]))
                    elif user_id2=="403773124":
                        reply(random.choice(risposta4[interazione]))
                    else:
                        reply(random.choice(risposte[interazione]), quote=False)
                    if interazione=="biscotto":
                        reply(random.choice(risposte[interazione]), quote=False)
                    elif interazione=="bestemmia":
                        reply(random.choice(risposte[interazione]), quote=False)
                    elif interazione=="ciao":
                        if user_id==236408435:
                            reply(random.choice(risposte2[interazione]))
                        elif user_id==410255671:
                            reply(random.choice(risposta3[interazione]))
                        elif user_id==403773124:
                            reply(random.choice(risposta4[interazione]))
                        else:
                            reply(random.choice(risposte[interazione]))
                            print(user_id)


                    print(name + " ha usato " + interazione)

                    return

            for interazione3 in trigger["interazioni3"]:
                if interazione3 in msg:
                    bot.sendMessage(chat_id=chat_id, text=random.choice(risposte[interazione3]), parse_mode="HTML")
                    print(name+" ha usato "+interazione3)

                    return

            for interazione2 in trigger["interazioni2"]:
                if interazione2 in msg:
                    if "kyoko-chan" in contLower:
                        if contLower=="kyoko-chan":
                            reply(random.choice(risposte[interazione2]))
                            print(name + " ha usato kyoko-chan")

                    return



            return

        for eguale in trigger["equal"]:
            if eguale in msg:
                if "rip" in contLower:
                    if contLower=="rip":
                        reply(random.choice(risposte[eguale]))
                        print(name+" ha usato "+ eguale)

                return

    except Exception as err:
       print(err)



    return  # Se il messaggio non c'entra niente con il bot allora esci


def BenvenutoAddio1(bot, update):
    chat_id = update.message.chat.id
    chat_name = update.message.chat.title
    nuovo = update.message.new_chat_members
    uscito = update.message.left_chat_member

    try:

        if nuovo:
            nome = nuovo[0]['first_name']

            saluto = ["Benvenuto/a " + nome + " in " + chat_name + "\t\nnya~"]
            update.message.reply_text(random.choice(saluto))
            print(nome + " è entrato nel gruppo " + chat_name)
        if uscito:
            nome = nuovo[0]['first_name']

            update.message.reply_text("Prima paga e poi esci")
            print(nome + " è uscito dal gruppo " + chat_name)
    except Exception as err:
        print(err)


def reader1(bot, update):
    try:
        cont = update.message.text  # Contenuto del messaggio, è essenziale ovviamente per poterlo analizare
        contLower = cont.lower()  # Questo rende il testo tutto minuscolo
        idg = update.message.chat.id  # ID univoco del gruppo da cui proviene il messaggio
        # l'ID della chat se in privatosarebbe l'ID dell'utente
        idu = update.message.from_user.id  # ID univoco dell'utente da cui proviene il messaggio
        msg = update.message.text.lower()
        reply = update.message.reply_text
        rnq = bot.sendMessage
        name = update.message.from_user.first_name
        chat_id = update.message.chat.id
        user_id = update.message.from_user.id

        if update.message.reply_to_message is not None:
            name2 = update.message.reply_to_message.from_user.first_name
            nick2 = update.message.reply_to_message.from_user.username
            user_id2 = str(update.message.reply_to_message.from_user.id)
        else:
            name2 = None
            nick2 = None
            user_id2 = None
        botname = bot.first_name.lower()
        if " " in botname: botname = botname.split()
        botname = ''.join([i for i in botname if i.isalpha])

        trigger = {
            "interazioni": {
                "uccidilo", "uccidila", "abbraccialo", "abbracciala", "headpattalo", "headpattala", "biscotto",
                "bestemmia", "ciao"
            },
            "interazioni2": {
                ""
            },
            "interazioni3": {
                "bsd", "nanbaka", "naruto", "ft", "rakudai kishi", "shokugeki", "shakunetsu"
            },

            "equal": {
                "rip"
            }
        }

        risposte = {
            "ciao": [
                "Ciao {}".format(name)

            ],
            "uccidilo": [
                "*tira fuori gli artigli e uccide {}*".format(name2),
                "*richiama il Rashoumon Agito e disintegra {}*".format(name2)
            ],
            "uccidila": [
                "*tira fuori gli artigli e uccide {}*".format(name2),
                "*richiama il Rasoumon Agito e disintegra {}*".format(name2)
            ],
            "abbraccialo": [
                "Nya~\t \n*abbraccia {}*".format(name2), "No, non voglio abbracciarlo", "No, {} puzza!".format(name2)
            ],
            "abbracciala": [
                "Nya~\t \n*abbraccia {}*".format(name2), "No, non voglio abbracciarla", "No, {} puzza!".format(name2)
            ],
            "biscotto": [
                "Certo, tutti i biscotti che vuoi\t \nNya~",
                "Subito, *lancia un biscotto a {}*\t \nNya~".format(name), "Non voglio"
            ],
            "headpattalo": [
                "Nya~ *headpatta {}*".format(name2)
            ],
            "headpattala": [
                "Nya~ *headpatta {}*".format(name2)
            ],
            "": [
                "Eccomi, nya~"
            ],
            "bsd": [
                "<a href='https://68.media.tumblr.com/368aa48890196b6f04cc4b518e68c68a/tumblr_otnqnvSrWp1w2ucj8o1_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/f2986238ca783d0f073ef8b7f5c8dce6/tumblr_otnqnvSrWp1w2ucj8o9_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/8c13d51727e3fc7630909bbc84da475c/tumblr_otnqnvSrWp1w2ucj8o2_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/1a4c642adb4320570a3078ac2d89d09d/tumblr_otnqnvSrWp1w2ucj8o3_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/69f7ff259a551e00bec296c8b5c7c4cf/tumblr_otnqnvSrWp1w2ucj8o5_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/bac36c6e810ab310d41092921830df38/tumblr_otnqnvSrWp1w2ucj8o4_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/cc89a2d310794e8ed894c2e357805e05/tumblr_otjbgzbmWQ1wqyc4yo1_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/28c37184bf5f42592a3514dc45768c2d/tumblr_otgtfwYSqn1w2ucj8o1_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/4643373e9c069247a606a3d56f617e1e/tumblr_otgtfwYSqn1w2ucj8o3_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/dbba4aed080cfa20797e4ba18f944c33/tumblr_otgtfwYSqn1w2ucj8o2_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/103b14637e209dad31b4d87c61738611/tumblr_op6nvwUO7V1wnm2puo1_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/a28a2ec421e57fce2a3c0456058361f6/tumblr_op6nvwUO7V1wnm2puo2_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/a7266b87ebe9c4542eac77b2f5fdabc4/tumblr_op6nvwUO7V1wnm2puo3_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/c41f1de173661cef547677cf00d40404/tumblr_oib0i6W0HF1vl3h3so2_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/b9b761cacdf7ae80af58ea59295fdcbd/tumblr_oiaowlTZY41vl3h3so1_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/6ffa5fb3d55a006fd7549d191e13e8aa/tumblr_oiaowlTZY41vl3h3so2_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/bd89420994252120c2ac4b6fa2dcca61/tumblr_ofylf4RNAI1um42ooo1_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/72a68d7033496ba99da7e46982c444e5/tumblr_ofylf4RNAI1um42ooo8_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/5f38ad737d380af9984f16739333c5fe/tumblr_oesc7iHCj81qg7cgfo1_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/02ff1fe4431a2fd59605479228903ccd/tumblr_oesc7iHCj81qg7cgfo2_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/0e8de893dee50504d23b9e164312e35e/tumblr_oen3huDn1N1v9hzmko1_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/73643fd679042718fc2b3b18c281ce00/tumblr_odx40qmrwf1v9hzmko1_1280.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/9d3a24342a9ff0f8fc21051cb5dd4122/tumblr_ob5dc2vJ7c1v9hzmko1_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/11366bdf0d49d9465ed4b7fd17bd2fd9/tumblr_o9767sidda1vxlcoqo3_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/67634c11258ae853c646afc85ccf99a0/tumblr_o8z67h3rDF1vxlcoqo1_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/591d4d887fc5ad5f36f21a61f5daff73/tumblr_o8klfam9GY1vwdqc3o1_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/fdde355e0f40ec513f7e88ac76be62b4/tumblr_o8gvt9xGjw1s9jnzyo9_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/17046d02b4756cfcde4ef8e48fffab0c/tumblr_o8gvt9xGjw1s9jnzyo10_400.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/1e565ee798839b31caedcd8f19b4f351/tumblr_o5907je1fA1s2o7ljo1_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/1313ba48aa60334a89b7c42ef4b71a04/tumblr_o5907je1fA1s2o7ljo2_540.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/4d9c41c1cfc141a83a3ab743a76a8eff/tumblr_ofylf4RNAI1um42ooo10_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/c8b487a1051bd31274a6f37b454ebed9/tumblr_ofylf4RNAI1um42ooo9_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/2c79697fb57b5b4167cfd378a74c2da3/tumblr_ofylf4RNAI1um42ooo6_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/d7aa8b46a49d54f0d6538891d0e41039/tumblr_ofylf4RNAI1um42ooo5_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/b2629c1262a425b296481ac2f7c7df08/tumblr_ofylf4RNAI1um42ooo4_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/cc16c54a754818d04623a0672280aa70/tumblr_ofylf4RNAI1um42ooo3_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/11a676b94398a4177ecd59e3118add2b/tumblr_ofylf4RNAI1um42ooo2_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/dcc836615afb6ea203d9bc563aa3def5/tumblr_oib0i6W0HF1vl3h3so1_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/6a1b13f107f8881e8700c8cf77eebf56/tumblr_oib0i6W0HF1vl3h3so3_500.gif'>bsd</a>",
                "<a href='https://68.media.tumblr.com/720d4fca50c73f3847e2f9add0753d58/tumblr_op6nvwUO7V1wnm2puo5_500.gif'>bsd</a>"],
            "nanbaka": [
                "<a href='https://68.media.tumblr.com/1888abcd608c07e1069b7969da1eb460/tumblr_okb78lobrB1velul7o1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/ff152f8d2447bfafd225c618ac537dce/tumblr_on6rhf5crA1velul7o1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/6e7eb183be949ecadb26a2c19af5bec6/tumblr_ophnbxj3QG1v30j2so1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/d96b0e303b5521733deb5a786ce91550/tumblr_om45sfQYOS1velul7o1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/230e842304a762f4b5ee1c001a733932/tumblr_omtxs431JV1qlomhno1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/b4375c1aef7db4cad7f942ab5d6c1498/tumblr_on75ufFwkn1vjc1jro1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/d6e2d12c35f51e374f1652e46134f64c/tumblr_ohseypPMWJ1uku9tco1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/3e85902f5180f78e442397a5546c8fbf/tumblr_om40p4gzGI1tqsu3ro1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/5df93f1f5c072490e1da7b3589075d84/tumblr_okb709GT2m1vgfg91o2_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/92aa892495be63490f8fbc12aa0a538f/tumblr_oldxj8SvmP1qg9t1lo1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/697f7ef2f7741a1da1a5979f46ebbe06/tumblr_oiz1gcmGKR1r60zuio1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/44bb25be67cbf2845214d00d35c40cb0/tumblr_on4csiexPm1v30j2so1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/f32232c378e43d9e25c0a49b74144182/tumblr_olwoxtVrp61w58oyno1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/2a08e9464eb7cb11b17d0a1dd3a341d5/tumblr_oja191SrsV1s8gfjqo1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/ca59598d7df18367cb66d9ad030ccee4/tumblr_omwqg6xwxt1v30j2so1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/5a18291389626f04c2b9277e3438a1b4/tumblr_osufpkisui1vgfg91o1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/4644faf927b87c78002399fb637b0adc/tumblr_omy765Hj8G1v30j2so1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/c2669aac95842d2603f09d30e30273ed/tumblr_ohaujoruS11s8gfjqo1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/58c0dc6c6b44ba0f082b5a361526384e/tumblr_oewh07R74T1ri2bgao1_500.gif'>nanbaka</a>",
                "<a href='https://68.media.tumblr.com/cbe65de38842f044a0bd0a3eca3635df/tumblr_oh2h8vwG261velul7o1_500.gif'>nanbaka</a>"
            ],
            "naruto": [
                "<a href='https://68.media.tumblr.com/2b83f4b79cf0870ed93f98e619ecf96e/tumblr_ovw0yiDXR51vzjl3fo1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/f31dd7747bbc2944219c5bb85bec81be/tumblr_ovi4etA1GS1qfeem4o1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/14de17b54263e233a50684de69a2c69b/tumblr_ov4a7eVeSn1rddilvo1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/b2187640be59973b1d452991619de812/tumblr_ov2brajjdb1wrm9xio1_250.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/d5294b436fc58a90fda3f481e160bb64/tumblr_ov1tacuckd1wylmu4o1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/8d3b665014ba18f76f68ab4676ee531a/tumblr_ov0hoo7wFt1wya8szo2_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/ab81c43a7c2696585501c2ed391e5925/tumblr_ouy8hqdfDN1wof0cmo1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/2a48a35f06fb4071b6f194b532f12626/tumblr_otzkk233rO1te23s4o1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/d741f1e697e3d44c9a3c8436671f2bcf/tumblr_osydwh8cUR1ui7oe1o3_540.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/47f31149f550364058e91d452ed66f23/tumblr_osydwh8cUR1ui7oe1o4_540.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/7b51e17576b7ec740436a7f0e314370d/tumblr_osydwh8cUR1ui7oe1o1_540.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/f48197f1c143577d58020c4a559f035b/tumblr_oswqkiHSkq1wsjjgbo1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/050a6911c0d23609cf4bd534108cd97d/tumblr_ostd4g1aBO1wnugwfo2_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/73a3f63dafece1c0c0508676daabce45/tumblr_ostd4g1aBO1wnugwfo5_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/841c39ea93cca61a4768e26628db79a2/tumblr_ostd4g1aBO1wnugwfo6_400.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/a56520a3ca120e45558ee1fa256bdd93/tumblr_ostd4g1aBO1wnugwfo8_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/d31927b7626042eb762b66f048bd49c1/tumblr_ostd4g1aBO1wnugwfo10_500.gif'>naruto</a>",
                "<a href='http://68.media.tumblr.com/17656941d66d0b552c5c86a21f396d39/tumblr_osfpwqIofM1rqe0rbo1_540.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/19ce894fb7bfd6eb9170d7f780d0a58f/tumblr_orxfdzpTRW1vh89pzo1_500.gif'>naruto</a>",
                "<a href='https://68.media.tumblr.com/9666036b48b6564b1935c6758f82a1ad/tumblr_ora1ncworb1qfeem4o3_500.gif'>naruto</a>"
            ],
            "ft": [
                "<a href='https://68.media.tumblr.com/a91a79f02febe4ae443a97820769ae41/tumblr_ouoapa9MOU1unnwwto2_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/20f7e78d238b7099b97b5e5669256b57/tumblr_ouoapa9MOU1unnwwto3_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/43b4a717afec6c072b2c77287a5b0a5d/tumblr_ouoapa9MOU1unnwwto4_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/84ea11d3631162d2f702033039fa0ac8/tumblr_ouoapa9MOU1unnwwto5_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/d4af93b9e9e5dc3f35e3a0f7033c4fb1/tumblr_ouoapa9MOU1unnwwto6_540.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/f0c1a28dbf606ce3b059cc410d658179/tumblr_ouoapa9MOU1unnwwto8_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/ad4221b21c7ad358273e4e44f64881d6/tumblr_ouoapa9MOU1unnwwto9_540.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/1948c46462e9cc3cecc89742c958f6c0/tumblr_othzn7rWPL1taoarbo1_400.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/5ca92466cd9f5137331ed382b2dc0a45/tumblr_othzn7rWPL1taoarbo8_400.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/2c22eef6bfd43041d98456d4dc0692bf/tumblr_othz64xGrn1taoarbo6_400.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/1f7b9f8d501caccf98f3fd97e8d13298/tumblr_othz64xGrn1taoarbo2_400.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/93cbb2d7b0b44586b5cac8d4d673e5fa/tumblr_othz64xGrn1taoarbo7_400.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/a3c76857d4a20809035c6878ba0c9423/tumblr_othz64xGrn1taoarbo5_400.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/76f915e702621c49fcd58c4d3f90c66b/tumblr_os266bAaSL1unnwwto3_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/54fc4c4487a878d4b7c7a71df5291f33/tumblr_orzuxvfxrp1unnwwto1_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/c9443a0b776dfacb9ee1e61e3bc9ef08/tumblr_or71dmqrZK1uiz4mko3_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/b12ebced507a47fcf964a97171a76e79/tumblr_or71dmqrZK1uiz4mko5_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/d69c9d475f1292120d5522d3af8d24bd/tumblr_oqzy16h5w21uiz4mko4_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/5527ae07418e0759fafd6e4389162f48/tumblr_oqzy16h5w21uiz4mko3_500.gif'>ft</a>",
                "<a href='https://68.media.tumblr.com/5f206f30802bf8aefc01fb60112c388e/tumblr_omvdy8ly1w1rjf4f5o1_500.gif'>ft</a>"],
            "rakudai kishi": [
                "<a href='http://68.media.tumblr.com/e092c6421f7c1a06325e60e5ac3e3c9b/tumblr_nxkocnlR6H1unbsixo1_540.gif'>rakudai kishi no cavalry</a>",
                "<a href='http://68.media.tumblr.com/0a340fa186c68c5580339c00459c287a/tumblr_nxknazWYyI1unbsixo1_540.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/98024745bd68e96edc0922b5f24e255c/tumblr_nzmik9NfpN1qimk8ao3_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/e145706e668a00aab79f13dac6f564d2/tumblr_nxc0nx0PZL1tydz8to1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/681b88865885f36d016bedb402c8823e/tumblr_ol185zIZZv1uvxchjo4_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/6273e82719026046e6fbce9c738547b5/tumblr_nw0puiq7tv1s3dw0xo1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/a619ec0fd70a048644932d522624848d/tumblr_ny6s4zZsru1u0tkulo1_r2_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/cb2d9b43bcd7afb493b022a481c31afb/tumblr_nxboz95lWt1so2t73o1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/46ac9362b8e5e08480ea2b50aec46425/tumblr_nzn4dlwkVT1uq3u3ko2_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/1393d5f3218a3466f8d6323540ef9853/tumblr_nwdwdjDchr1ttu8odo1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/f020c3508fab3316da36585ef7e6dca7/tumblr_nzoflbEjPJ1s21xzoo1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/1efb66c07ce1fdf5aef5e5bba30cded1/tumblr_nx3j22CCSU1ttu8odo1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/57f08ef9b3f91cc15f368c923bdc14bf/tumblr_nwjov49t9i1smmps3o2_r1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/7da47846c8fb60190f28406eaa27cc02/tumblr_o6f62iFGR31snbyiqo3_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/136abd36fe7de45b57b25388c88f08ad/tumblr_nwz332rZGI1tydz8to1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/21ad799678dd1e0d7ad64dfe19e7c111/tumblr_nwqidiBVCJ1ttu8odo1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/17805ede69551301eb5e75ee09610e13/tumblr_nz11zfjLP21qekr89o1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/14a5b1683870c111c784a2595789c242/tumblr_o0z8b71cCx1uli1i6o1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/96099444b0db1ae9a63ac458da547600/tumblr_nwskb86GlG1tydz8to1_500.gif'>rakudai kishi no cavalry</a>",
                "<a href='https://68.media.tumblr.com/a05bc7fc4832892a33299cb4c1a708d3/tumblr_nz9f5gzxlO1rd6sdio1_500.gif-'>rakudai kishi no cavalry</a>"],
            "shokugeki": [
                "<a href='https://68.media.tumblr.com/4ff996131e9c9416b6b4ddade2b0e225/tumblr_ofof83nDNG1vi5fvdo1_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/c6b4646e08f252c147cbda4addfda6a4/tumblr_o7hqdcSkkR1vq4578o1_540.gif'>shokugeki no soma</a>",
                "<a href='http://68.media.tumblr.com/a02f496c695c710d1163eb1450d95beb/tumblr_nyp8o2XQu31src42wo1_540.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/de8d6a55b414b219f7bcbfdf1204a788/tumblr_nv92kcVxxA1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/ca1c6ee7ade81b7b009d5eb9ffaa515a/tumblr_nsgqpdTNEV1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/9b4ef8cef5998d4bb35a7bde79fbfb78/tumblr_nrosuqaQGB1uoves2o1_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/682cccf8963660ea4feb95db338fe384/tumblr_nqxkhtj7Z71uoves2o1_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/042a46475fae0aa0ba2dea30d232cf49/tumblr_nqxkcwHENE1uoves2o1_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/cf43daa9b41dc152b5e5ca3478796a83/tumblr_nqb3rzY4rH1tw9r1lo1_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/dd987307f124ea56d0e4c90ddf758282/tumblr_npv6ygGJEU1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/3ab126a426d5f3fea6785f04a4cf39e3/tumblr_nputlnSvCh1sg9gi2o1_540.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/c5ed358164cbb591cbbc2e46f49d2bb6/tumblr_npj5px4rG41sg9gi2o1_540.gif'>shokugeki no soma</a>",
                "<a href='http://68.media.tumblr.com/f026f5ef337b9db60e291b4c6cab0e38/tumblr_nnc2wqetfZ1s2c1h4o1_1280.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/b67670b9494a3c06372be154f018b811/tumblr_nms5yha74D1sg9gi2o2_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/f384b61c84489454f234aff75ced200c/tumblr_nmpq4ehyLM1sg9gi2o2_500.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/5aa45f286e9b73c8eb95d8f846d1df11/tumblr_nmnfi99rYt1qeph4io3_250.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/3b847a6d46247080fd88356ba0136331/tumblr_nm9p34Dnnt1sg9gi2o1_500.gif'>shokugeki no soma</a>",
                "<a href='http://68.media.tumblr.com/f9088d7172f9ec642ca5c5f94d62e330/tumblr_nm91uvPXef1toqhwfo1_540.gif'>shokugeki no soma</a>",
                "<a href='http://68.media.tumblr.com/b4beb6c54302a502dd1dae1bc75973da/tumblr_nm95dsxcho1toqhwfo1_540.gif'>shokugeki no soma</a>",
                "<a href='https://68.media.tumblr.com/ba86c08e07442d0a4654f979b8661a15/tumblr_nqxkf2EKnF1uoves2o1_500.gif'>shokugeki no soma</a>"],
            "shakunetsu": [
                "<a href='https://68.media.tumblr.com/669da82d96e69ba059032f305c94d98d/tumblr_ofkieg0ynV1s4qvrdo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/ed2f91c93576f29e76e3cc8668ac1b41/tumblr_oigjfohifD1s4qvrdo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/4bfe0a4149f506b7680a82cb445ab416/tumblr_oek62w5wXq1vaigheo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/b277686186a46c173ec22efbc6b2549a/tumblr_ohi8fvSLTl1uqldi9o1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/041f721a1c3a91e41febd6b66bc6af07/tumblr_ohkg2q5ntm1t3uwllo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/a49ea5bb062e68e69e00c935a7047d10/tumblr_oei9cr9tBW1sn2bkjo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/aee4b743286dc242d9f67c0f9a8e845e/tumblr_ogns6nTSHP1rd6sdio1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/61805789bfdb5e9ce8ea2fbec71f59fe/tumblr_oi3qabB0601tjh5d1o1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/655d6f834013f5684920ed22bb6955a9/tumblr_oekb09sNhh1vvvyj7o1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/e9d78308b39cc93fa61bce34b04ca3d9/tumblr_oh19hzzpG81rd6sdio1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/bb9468526bf76869b67728b299c4ada7/tumblr_ohe9c25aLh1vaigheo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/f2eebb7d4afeb141cdb7e848a2881b1c/tumblr_ofm4eu9CXg1srr81uo1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/b9e8706938ed212f235f257ac6e4bd25/tumblr_oeuysxkvGr1twgfw0o1_500.gif'>shakunetsu no takkyuu musume</a>",
                "<a href='https://68.media.tumblr.com/84486804d1add2c5c18ebfddee607147/tumblr_ohbfbedzTP1tdriooo1_500.gif'>shakunetsu no takkyuu musume</a>"
            ],
            "bestemmia": [
                "Dio canguro col soffitto basso",
                "Dio scalzo nella valle dei chiodi",
                "Dio scacciapreti assatanati",
                "Madonna incaprettata",
                "Dio lurido",
                "Gesù lavastoviglie",
                "Mannaggia Gesù Cristo in croce incaprettato da quella maialona della Madonna bastarda mentre si masturbava con il martello di Giuseppe",
                "Madonna stuprata",
                "Madonna spellata",
                "Gesù tavernello"
            ],
            "rip": [
                "Chi è morto? nya~"
            ],

        }

        risposte2 = {
            "uccidilo": [
                "Nya~\t \nNon uccido mio padre.\t \n*tira fuori un coltello e uccide {}*".format(name)
            ],
            "uccidila": [
                "Nya~\t \nNon uccido mio padre\t \n*tira fuori un coltello e uccide {}*".format(name)
            ],
            "abbraccialo": [
                "Nya~ subito\t \n*abbraccia {}*".format(name2)
            ],
            "abbracciala": [
                "Nya~ subito\t \n*abbraccia {}*".format(name2)
            ],

            "headpattalo": [
                "Nya~ *headpatta {}*".format(name2)
            ],
            "headpattala": [
                "Nya~ *headpatta {}*".format(name2)
            ],
        }

        risposte3 = {
            "ciao": [
                "Ciao zia\n\tNya~"

            ]}

        risposte4 = {
            "ciao": [
                "Ciao zio\n\tNya~"
            ]
        }

        if msg.startswith(botname) or msg.endswith(botname):
            for interazione in trigger["interazioni"]:
                if interazione in msg:
                    if name2 == None:
                        if interazione != "biscotto" and interazione != "bestemmia" and interazione != "ciao":
                            reply("No...", quote=False)
                    elif name2 == "Kyoko-chan":
                        reply("Non posso", quote=False)
                    elif user_id2 == "236408435":
                        reply(random.choice(risposte2[interazione]), quote=False)
                    else:
                        reply(random.choice(risposte[interazione]), quote=False)
                    if interazione == "biscotto":
                        reply(random.choice(risposte[interazione]), quote=False)
                    elif interazione == "bestemmia":
                        reply(random.choice(risposte[interazione]), quote=False)
                    elif interazione == "ciao":
                        if user_id == 410255671:
                            reply("Ciao zia\n\tya~")
                        elif user_id == 236408435:
                            reply(random.choice(risposte4[interazione]))
                            # if user_id!="410255671" or user_id!="403773124":
                            #   reply(random.choice(risposte[interazione]), quote=False)
                    print(user_id)
                    print(name + " ha usato " + interazione)
                    return

            for interazione3 in trigger["interazioni3"]:
                if interazione3 in msg:
                    bot.sendMessage(chat_id=chat_id, text=random.choice(risposte[interazione3]), parse_mode="HTML")
                    print(name + " ha usato " + interazione3)

                    return

            for interazione2 in trigger["interazioni2"]:
                if interazione2 in msg:
                    if "kyoko-chan" in contLower:
                        if contLower == "kyoko-chan":
                            reply(random.choice(risposte[interazione2]))
                            print(name + " ha usato kyoko-chan")

                    return

            return

        for eguale in trigger["equal"]:
            if eguale in msg:
                if "rip" in contLower:
                    if contLower == "rip":
                        reply(random.choice(risposte[eguale]))
                        print(name + " ha usato " + eguale)

                return


    except Exception as err:
        print(err)

    return  # Se il messaggio non c'entra niente con il bot allora esci

# Main che serve ad aggiungere comandi o handler
def main():
    updater = Updater("391016366:AAEasRwxU8d2NUYFdGV6rq7IvkZwN4a2IVM")  # Qui ci va l'api key che prendi da botfather

    dp = updater.dispatcher

    # Adesso per aggiungere COMANDI quindi quelli con /roba si fa così:
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # Quindi: dp.add_handler(CommandHandler("comando", funzione))
    dp.add_handler(MessageHandler(Filters.status_update, BenvenutoAddio))
    dp.add_handler(MessageHandler(Filters.text, reader))  # Questo inizializza ad esempio il reader

    updater.start_polling()
    updater.idle()

    updater1 = Updater("395338211:AAGfmw4H_0fqnZZN2ol9dBsvzNhK7qxNKkY")

    dp1 = updater1.dispatcher

    dp1.add_handler(MessageHandler(Filters.status_update, BenvenutoAddio1))
    dp1.add_handler(MessageHandler(Filters.text, reader1))




    updater1.start_polling()

    updater1.idle()

# Questo è ciò che fa partire tutto
if __name__ == '__main__':
    os.system("cls")
    print("Bot avviato")
    print("Premi Ctrl + C per fermare")
    main()
