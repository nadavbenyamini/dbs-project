from server.utils import *
from flask import request
from flask import Blueprint

artist_routes = Blueprint('artist_routes', __name__)


@artist_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    GETTER
    :param artist_id
    :return: Everything from Artists table
    """
    query = "select * from Artists where artist_id = %s;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_tracks_by_artist(artist_id):
    """
    :param artist_id
    :return: tracks: json of the artist's tracks
    """
    query = "select * from TracksView where artist_id = %s;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/similar_artists/<artist_id>', methods=['GET'])
def get_similar_artists(artist_id):
    return
[
  {
    "artist_name": "Peter Murphy"
  },
  {
    "artist_name": "Red Hot Chili Peppers"
  },
  {
    "artist_name": "Kings of Leon"
  },
  {
    "artist_name": "Handsome Furs"
  },
  {
    "artist_name": "The Rumour Said Fire"
  },
  {
    "artist_name": "The Killers"
  },
  {
    "artist_name": "Feist"
  },
  {
    "artist_name": "Rachel Goodrich"
  },
  {
    "artist_name": "Lykke Li"
  },
  {
    "artist_name": "The Cranberries"
  },
  {
    "artist_name": "The Cure"
  },
  {
    "artist_name": "Up Dharma Down"
  },
  {
    "artist_name": "Jamie Woon"
  },
  {
    "artist_name": "Imagine Dragons"
  },
  {
    "artist_name": "Coldplay"
  },
  {
    "artist_name": "M83"
  },
  {
    "artist_name": "Gossip"
  },
  {
    "artist_name": "Dotan"
  },
  {
    "artist_name": "Thomas Azier"
  },
  {
    "artist_name": "American Authors"
  },
  {
    "artist_name": "Caught a Ghost"
  },
  {
    "artist_name": "BANNERS"
  },
  {
    "artist_name": "Langhorne Slim & The Law"
  },
  {
    "artist_name": "Jamie N Commons feat. X Ambassadors"
  },
  {
    "artist_name": "Willow"
  },
  {
    "artist_name": "Gorillaz"
  },
  {
    "artist_name": "KALEO"
  },
  {
    "artist_name": "Florence + The Machine"
  },
  {
    "artist_name": "Kwabs"
  },
  {
    "artist_name": "Dominique Charpentier"
  },
  {
    "artist_name": "Rag'n'Bone Man"
  },
  {
    "artist_name": "Glass Animals"
  },
  {
    "artist_name": "Cigarettes After Sex"
  },
  {
    "artist_name": "King Gnu"
  },
  {
    "artist_name": "Billie Eilish"
  },
  {
    "artist_name": "Gerry Cinnamon"
  },
  {
    "artist_name": "Tove Lo"
  },
  {
    "artist_name": "Van William"
  },
  {
    "artist_name": "Welshly Arms"
  },
  {
    "artist_name": "The FAIM"
  },
  {
    "artist_name": "Lana Del Rey"
  },
  {
    "artist_name": "LP"
  },
  {
    "artist_name": "Banoffee"
  },
  {
    "artist_name": "Shatta Wale"
  },
  {
    "artist_name": "SHAED"
  },
  {
    "artist_name": "Dominic Fike"
  },
  {
    "artist_name": "Mac DeMarco"
  },
  {
    "artist_name": "Hindia"
  },
  {
    "artist_name": "Bastille"
  },
  {
    "artist_name": "Juan Luis"
  },
  {
    "artist_name": "Capital Cities"
  },
  {
    "artist_name": "All Time Low"
  },
  {
    "artist_name": "Nine Inch Nails"
  },
  {
    "artist_name": "London Grammar"
  },
  {
    "artist_name": "Lil Nas X"
  },
  {
    "artist_name": "Sheer Mag"
  },
  {
    "artist_name": "BENEE"
  },
  {
    "artist_name": "Tones and I"
  },
  {
    "artist_name": "Tems"
  },
  {
    "artist_name": "Milky Chance"
  },
  {
    "artist_name": "Sturgill Simpson"
  },
  {
    "artist_name": "Elaine"
  },
  {
    "artist_name": "Kofi Kinaata"
  },
  {
    "artist_name": "Kahraman Deniz"
  },
  {
    "artist_name": "Lady Gaga"
  },
  {
    "artist_name": "Katy Perry"
  },
  {
    "artist_name": "Flo Rida"
  },
  {
    "artist_name": "Laleh"
  },
  {
    "artist_name": "Fainal feat. Chino & Nacho"
  },
  {
    "artist_name": "Estefani Brolo"
  },
  {
    "artist_name": "Maroon 5 feat. Christina Aguilera"
  },
  {
    "artist_name": "Calvin Harris feat. Ellie Goulding"
  },
  {
    "artist_name": "Sia"
  },
  {
    "artist_name": "Vincenzo Salvia"
  },
  {
    "artist_name": "Major Lazer feat. M\u00d8 & DJ Snake"
  },
  {
    "artist_name": "The Chemical Brothers"
  },
  {
    "artist_name": "Lorde"
  },
  {
    "artist_name": "Ariana Grande feat. Zedd"
  },
  {
    "artist_name": "Pitbull feat. Marc Anthony"
  },
  {
    "artist_name": "Moby"
  },
  {
    "artist_name": "Ellie Goulding"
  },
  {
    "artist_name": "ZAYN"
  },
  {
    "artist_name": "Hippie Sabotage"
  },
  {
    "artist_name": "Kygo feat. Conrad Sewell"
  },
  {
    "artist_name": "Kygo feat. Parson James"
  },
  {
    "artist_name": "Marshmello"
  },
  {
    "artist_name": "Polo & Pan"
  },
  {
    "artist_name": "Maxi Trusso"
  },
  {
    "artist_name": "Kelly Clarkson"
  },
  {
    "artist_name": "Khainz"
  },
  {
    "artist_name": "Oliver Koletzki"
  },
  {
    "artist_name": "5 Seconds of Summer"
  },
  {
    "artist_name": "SHAUN"
  },
  {
    "artist_name": "Drake feat. Majid Jordan"
  },
  {
    "artist_name": "Dua Lipa"
  },
  {
    "artist_name": "Ava Max"
  },
  {
    "artist_name": "Rhye"
  },
  {
    "artist_name": "CVRTOON"
  },
  {
    "artist_name": "Ludmilla"
  },
  {
    "artist_name": "Taylor Swift"
  },
  {
    "artist_name": "Sun-El Musician feat. Ami Faku"
  },
  {
    "artist_name": "Sub Focus"
  },
  {
    "artist_name": "Jacques Greene"
  },
  {
    "artist_name": "Hi I'm Ghost"
  },
  {
    "artist_name": "Woodkid feat. Nils Frahm"
  },
  {
    "artist_name": "Elani"
  },
  {
    "artist_name": "Stan Getz & Luiz Bonfa"
  },
  {
    "artist_name": "Rihanna"
  },
  {
    "artist_name": "Davido"
  },
  {
    "artist_name": "Camila Cabello & Daddy Yankee"
  },
  {
    "artist_name": "Chris Brown"
  },
  {
    "artist_name": "David Bisbal feat. Sebastian Yatra"
  },
  {
    "artist_name": "FISHER"
  },
  {
    "artist_name": "Caza feat. Bizzey"
  },
  {
    "artist_name": "Various Artists"
  },
  {
    "artist_name": "Rob Thomas"
  },
  {
    "artist_name": "Coez"
  },
  {
    "artist_name": "Blake Shelton"
  },
  {
    "artist_name": "Ingrid Andress"
  },
  {
    "artist_name": "Rom\u00e9o Elvis"
  },
  {
    "artist_name": "Official Hige Dandizumu"
  },
  {
    "artist_name": "Stormzy"
  },
  {
    "artist_name": "Lil Nas X feat. Billy Ray Cyrus & Diplo"
  },
  {
    "artist_name": "Sea of Thieves"
  },
  {
    "artist_name": "Niels Destadsbader"
  },
  {
    "artist_name": "Sam Feldt feat. RANI"
  },
  {
    "artist_name": "JAY-Z feat. Alicia Keys"
  },
  {
    "artist_name": "Guy Sebastian"
  },
  {
    "artist_name": "Phan Manh Quynh"
  },
  {
    "artist_name": "Ant Saunders"
  },
  {
    "artist_name": "Leoni Torres feat. Gente De Zona"
  },
  {
    "artist_name": "Sasha Sloan"
  },
  {
    "artist_name": "Marco Borsato feat. Armin van Buuren & Davina Michelle"
  },
  {
    "artist_name": "Suzan & Freek"
  },
  {
    "artist_name": "LISA"
  },
  {
    "artist_name": "Billie Eilish feat. Justin Bieber"
  },
  {
    "artist_name": "Official HIGE DANdism"
  },
  {
    "artist_name": "\u65e5\u5411\u574246"
  },
  {
    "artist_name": "Snelle"
  },
  {
    "artist_name": "Blue Ivy feat. SAINt JHN, Beyonc\u00e9 & WizKid"
  },
  {
    "artist_name": "Beyonc\u00e9 feat. Shatta Wale & Major Lazer"
  },
  {
    "artist_name": "Mrs. Green Apple"
  },
  {
    "artist_name": "\u041c\u0430\u0440\u0438 \u041a\u0440\u0430\u0439\u043c\u0431\u0440\u0435\u0440\u0438"
  },
  {
    "artist_name": "Lost Frequencies"
  },
  {
    "artist_name": "Joeboy"
  },
  {
    "artist_name": "Miley Cyrus"
  },
  {
    "artist_name": "LOTTE feat. Max Giesinger"
  },
  {
    "artist_name": "James Blunt"
  },
  {
    "artist_name": "FictionJunction"
  },
  {
    "artist_name": "Kelsea Ballerini"
  },
  {
    "artist_name": "Niska"
  },
  {
    "artist_name": "Spada"
  },
  {
    "artist_name": "Fred De Palma"
  },
  {
    "artist_name": "Rene Karst"
  },
  {
    "artist_name": "Emir Can \u0130\u011frek"
  },
  {
    "artist_name": "Afro Brotherz"
  },
  {
    "artist_name": "Fernando Daniel"
  },
  {
    "artist_name": "Fred De Palma feat. Ana Mena"
  },
  {
    "artist_name": "Kenshi Yonezu"
  },
  {
    "artist_name": "Little Glee Monster"
  },
  {
    "artist_name": "Tina Naderer"
  },
  {
    "artist_name": "Killa Fonic"
  },
  {
    "artist_name": "Nebezao"
  },
  {
    "artist_name": "\u0110\u1ea1t G"
  },
  {
    "artist_name": "Brunori Sas"
  },
  {
    "artist_name": "Lauv"
  },
  {
    "artist_name": "Bebe Rexha"
  },
  {
    "artist_name": "JONY"
  },
  {
    "artist_name": "J SOUL BROTHERS III from EXILE TRIBE"
  },
  {
    "artist_name": "Andr\u00e9s Cepeda feat. Jesse & Joy"
  },
  {
    "artist_name": "Riley Green"
  },
  {
    "artist_name": "\u0e44\u0e02\u0e48\u0e21\u0e38\u0e01 \u0e23\u0e38\u0e48\u0e07\u0e23\u0e31\u0e15\u0e19\u0e4c"
  },
  {
    "artist_name": "Lady Antebellum"
  },
  {
    "artist_name": "Lous and The Yakuza"
  },
  {
    "artist_name": "Tommaso Paradiso"
  },
  {
    "artist_name": "Metejoor"
  },
  {
    "artist_name": "Lemo"
  },
  {
    "artist_name": "Mark Forster"
  },
  {
    "artist_name": "We The Kingdom"
  },
  {
    "artist_name": "Taner \u00c7olak"
  },
  {
    "artist_name": "Flume"
  },
  {
    "artist_name": "OSKIDO"
  },
  {
    "artist_name": "Matt Simons"
  },
  {
    "artist_name": "Pitbull feat. Ne-Yo, Lenier & El Micha"
  },
  {
    "artist_name": "Lukas Graham"
  },
  {
    "artist_name": "AIELLO"
  },
  {
    "artist_name": "Naza"
  },
  {
    "artist_name": "Marco Borsato feat. Snelle & John Ewbank"
  },
  {
    "artist_name": "Jean-Louis Aubert"
  },
  {
    "artist_name": "De Fam"
  },
  {
    "artist_name": "Elas"
  },
  {
    "artist_name": "\u0e14\u0e39\u0e42\u0e2d-\u0e40\u0e21\u0e22\u0e4c"
  },
  {
    "artist_name": "Summer Walker"
  },
  {
    "artist_name": "Rema"
  },
  {
    "artist_name": "Tyler, The Creator"
  },
  {
    "artist_name": "Kabza De Small x DJ Maphorisa"
  },
  {
    "artist_name": "\u0e40\u0e02\u0e35\u0e22\u0e19\u0e44\u0e02\u0e41\u0e25\u0e30\u0e27\u0e32\u0e19\u0e34\u0e0a"
  },
  {
    "artist_name": "Andmesh"
  },
  {
    "artist_name": "Carla"
  },
  {
    "artist_name": "Giordana Angi"
  },
  {
    "artist_name": "Fritz Kalkbrenner"
  },
  {
    "artist_name": "Izia"
  },
  {
    "artist_name": "Angga Candra"
  },
  {
    "artist_name": "Memba"
  },
  {
    "artist_name": "\u041f\u043e\u043b\u0438\u043d\u0430 \u0413\u0430\u0433\u0430\u0440\u0438\u043d\u0430"
  },
  {
    "artist_name": "Dadju"
  },
  {
    "artist_name": "GAYAZOV$ BROTHER$"
  },
  {
    "artist_name": "Static & Ben El"
  },
  {
    "artist_name": "Bich Phuong"
  },
  {
    "artist_name": "Flight Facilities"
  },
  {
    "artist_name": "Benji & Fede"
  },
  {
    "artist_name": "Pabllo Vittar feat. Psirico"
  },
  {
    "artist_name": "MC JottaP\u00ea"
  },
  {
    "artist_name": "Mustafa Ceceli"
  },
  {
    "artist_name": "LEA"
  },
  {
    "artist_name": "Maleek Berry"
  },
  {
    "artist_name": "Marius Bear"
  },
  {
    "artist_name": "Xindl X"
  },
  {
    "artist_name": "Miss Li"
  },
  {
    "artist_name": "Ho\u00e0ng Thu\u1ef3 Linh"
  },
  {
    "artist_name": "Emma Heesters feat. Rolf Sanchez"
  },
  {
    "artist_name": "Beret"
  },
  {
    "artist_name": "Duncan Laurence"
  },
  {
    "artist_name": "Selena Gomez"
  },
  {
    "artist_name": "Mabel Matiz"
  },
  {
    "artist_name": "Missy Elliott"
  },
  {
    "artist_name": "Stamp"
  },
  {
    "artist_name": "Try\u00f6"
  },
  {
    "artist_name": "Willie Peyote"
  },
  {
    "artist_name": "Achille Lauro"
  },
  {
    "artist_name": "Vasco Rossi"
  },
  {
    "artist_name": "Marco Mengoni"
  },
  {
    "artist_name": "Luke Bryan"
  },
  {
    "artist_name": "Fabri Fibra"
  },
  {
    "artist_name": "Ali Gatie"
  },
  {
    "artist_name": "Liam Payne feat. A Boogie Wit da Hoodie"
  },
  {
    "artist_name": "Ikiye On Kala"
  },
  {
    "artist_name": "Burkima"
  },
  {
    "artist_name": "Tame Impala"
  },
  {
    "artist_name": "Jah Khalib"
  },
  {
    "artist_name": "MYTH & ROID"
  },
  {
    "artist_name": "DOTSUITARE-HOMPO"
  },
  {
    "artist_name": "OTHERLiiNE, George FitzGerald & Lil Silva"
  },
  {
    "artist_name": "Marracash"
  },
  {
    "artist_name": "Superfly"
  },
  {
    "artist_name": "Sam Smith"
  },
  {
    "artist_name": "Niniola"
  },
  {
    "artist_name": "Peggy Zina"
  },
  {
    "artist_name": "\u5d50"
  },
  {
    "artist_name": "Terence Blanchard"
  },
  {
    "artist_name": "Trent Reznor & Atticus Ross"
  },
  {
    "artist_name": "Doja Cat"
  },
  {
    "artist_name": "Jessie Ware"
  },
  {
    "artist_name": "Fiersa Besari"
  },
  {
    "artist_name": "Max Pezzali"
  },
  {
    "artist_name": "3-\u0438\u0439 \u042f\u043d\u0432\u0430\u0440\u044c"
  },
  {
    "artist_name": "Mfr Souls"
  },
  {
    "artist_name": "Luke Combs"
  },
  {
    "artist_name": "Morgan Evans"
  },
  {
    "artist_name": "Aitch"
  },
  {
    "artist_name": "Mura Masa"
  },
  {
    "artist_name": "Ke$ha"
  },
  {
    "artist_name": "KSI"
  },
  {
    "artist_name": "tha Supreme"
  },
  {
    "artist_name": "Freschta Akbarzada"
  },
  {
    "artist_name": "Vetusta Morla"
  },
  {
    "artist_name": "Fireboy DML"
  },
  {
    "artist_name": "Indigo"
  },
  {
    "artist_name": "\u0e2a\u0e49\u0e21 \u0e21\u0e32\u0e23\u0e35"
  },
  {
    "artist_name": "Ofenbach"
  },
  {
    "artist_name": "Elisa"
  },
  {
    "artist_name": "Pind"
  },
  {
    "artist_name": "Camila Cabello"
  },
  {
    "artist_name": "Gavin D"
  },
  {
    "artist_name": "The Minds Of 99"
  },
  {
    "artist_name": "Little,Big"
  },
  {
    "artist_name": "Three Man Down"
  },
  {
    "artist_name": "Brad Cox"
  },
  {
    "artist_name": "Falling In Reverse"
  },
  {
    "artist_name": "Dj Afonso de Vic"
  },
  {
    "artist_name": "COLORPiTCH"
  },
  {
    "artist_name": "Dennis Lloyd"
  },
  {
    "artist_name": "YNW Melly"
  },
  {
    "artist_name": "Clara Luciani"
  },
  {
    "artist_name": "\u041c\u0430\u043a\u0441 \u0411\u0430\u0440\u0441\u043a\u0438\u0445"
  },
  {
    "artist_name": "\u042e\u043b\u0438\u0430\u043d\u043d\u0430 \u041a\u0430\u0440\u0430\u0443\u043b\u043e\u0432\u0430"
  },
  {
    "artist_name": "Goom Gum"
  },
  {
    "artist_name": "Bazart"
  },
  {
    "artist_name": "Nathan Goshen feat. Ishay Ribo"
  },
  {
    "artist_name": "\u041a\u043b\u0430\u0432\u0430 \u041a\u043e\u043a\u0430"
  },
  {
    "artist_name": "K-Billy"
  },
  {
    "artist_name": "Perfume"
  },
  {
    "artist_name": "Mikolas Josef"
  },
  {
    "artist_name": "GAMPER & DADONI"
  },
  {
    "artist_name": "Gest\u00f6rt aber GeiL"
  },
  {
    "artist_name": "Diodato"
  },
  {
    "artist_name": "Outsiders feat. Django Wagner"
  },
  {
    "artist_name": "School Is Cool"
  },
  {
    "artist_name": "Rozz Kalliope feat. Ece Se\u00e7kin"
  },
  {
    "artist_name": "Sunrise Avenue"
  },
  {
    "artist_name": "Foorin team E"
  },
  {
    "artist_name": "\u041c\u044d\u0432\u043b"
  },
  {
    "artist_name": "Avicii"
  },
  {
    "artist_name": "The Chainsmokers"
  },
  {
    "artist_name": "Bilal Sonses"
  },
  {
    "artist_name": "Rauf & Faik"
  },
  {
    "artist_name": "Ardhito Pramono"
  },
  {
    "artist_name": "Rin"
  },
  {
    "artist_name": "Roddy Ricch"
  },
  {
    "artist_name": "Checco Zalone"
  },
  {
    "artist_name": "Mr Belt feat. Wezol"
  },
  {
    "artist_name": "Kazka"
  },
  {
    "artist_name": "Juice WRLD"
  },
  {
    "artist_name": "Sound Of Legend"
  },
  {
    "artist_name": "Hael Husaini"
  },
  {
    "artist_name": "Carla's Dreams"
  },
  {
    "artist_name": "Griselda"
  },
  {
    "artist_name": "Mas Musiq"
  },
  {
    "artist_name": "Ti\u00ebsto"
  },
  {
    "artist_name": "KAYTRANADA"
  },
  {
    "artist_name": "Heuss L'enfoir\u00e9"
  },
  {
    "artist_name": "Maan"
  },
  {
    "artist_name": "Kim Loaiza"
  },
  {
    "artist_name": "Major Lazer"
  },
  {
    "artist_name": "Rotimi"
  },
  {
    "artist_name": "Kontrafakt"
  },
  {
    "artist_name": "FMK"
  },
  {
    "artist_name": "Vigro Deep"
  },
  {
    "artist_name": "Topic feat. A7S"
  },
  {
    "artist_name": "Celeste"
  },
  {
    "artist_name": "\u9ad8\u723e\u5ba3 OSN"
  },
  {
    "artist_name": "Tenille Arts"
  },
  {
    "artist_name": "Claudio Baglioni"
  },
  {
    "artist_name": "Andrew Lloyd Webber feat. Cast Of The Motion Picture \"Cats\""
  },
  {
    "artist_name": "Miguel Poveda feat. Mar\u00eda Jim\u00e9nez"
  },
  {
    "artist_name": "Sarkodie"
  },
  {
    "artist_name": "Young Thug"
  },
  {
    "artist_name": "M\u00f3nica Naranjo"
  },
  {
    "artist_name": "Why Don't We"
  },
  {
    "artist_name": "Lil Tjay"
  },
  {
    "artist_name": "Kodaline"
  },
  {
    "artist_name": "David Bisbal"
  },
  {
    "artist_name": "4Keus feat. Niska"
  },
  {
    "artist_name": "RAF Camora"
  },
  {
    "artist_name": "Lane 8"
  }
]

@artist_routes.route('/api/artists', methods=['GET'])
def get_all_artists():
    return get_all_from_table('Artists')


'''
@artist_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    GETTER
    :param artist_id
    :return: Everything from Artists table
    """
    query = "select * from Artists where artist_id = %s;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_tracks_by_artist(artist_id):
    """
    :param artist_id
    :return: tracks: json of the artist's tracks
    """
    query = "select * from TracksView where artist_id = %s;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/similar_artists/<artist_id>', methods=['GET'])
def get_similar_artists(artist_id):
    """
    :param artist_id
    :return: List of similar artists
    """
    query = "SELECT DISTINCT a1.artist_name "\
            "FROM Artists a1, Tracks t1, Genres g1, "\
            "   (SELECT MAX(c.track_rank) AS max_rating , MIN(c.track_rank) AS min_rating "\
            "   FROM Artists a , Tracks t ,Charts c "\
            "   WHERE a.artist_id = t.artist_id AND "\
            "   c.track_id = t.track_id AND "\
            "   a.artist_id = %s) AS min_max_rating "\
            "WHERE a1.artist_id = t1.artist_id AND "\
            "t1.genre_id =g1.genre_id AND "\
            "g1.genre_id IN " \
            "   (SELECT DISTINCT  g0.genre_id "\
            "   FROM Artists a0, Tracks t0, Genres g0 "\
            "   WHERE a0.artist_id = t0.artist_id " \
            "     AND t0.genre_id = g0.genre_id " \
            "     AND a0.artist_id = %s) " \
            "AND t1.track_rating>=min_max_rating.min_rating " \
            "AND t1.track_rating<=min_max_rating.max_rating;"
    args = (artist_id, artist_id)
    return query_to_json(query, args)


@artist_routes.route('/api/artists', methods=['GET'])
def get_all_artists():
    return get_all_from_table('Artists')
'''