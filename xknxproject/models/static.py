"""Contains static data from the project files that is not really important and doesn't change often."""
from enum import Enum


class SpaceType(Enum):
    """Supported space types according to Specs from XSD."""

    BUILDING = "Building"
    BUILDING_PART = "BuildingPart"
    FLOOR = "Floor"
    ROOM = "Room"
    DISTRIBUTION_BOARD = "DistributionBoard"
    STAIRWAY = "Stairway"
    CORRIDOR = "Corridor"
    AREA = "Area"
    GROUND = "Ground"
    SEGMENT = "Segment"


MEDIUM_TYPES: dict[str, str] = {
    "MT-0": "Twisted Pair (TP)",
    "MT-1": "Powerline (PL)",
    "MT-2": "KNX RF (RF)",
    "MT-5": "KNXnet/IP (IP)",
}

MANUFACTURERS: dict[str, str] = {
    "M-0001": "Siemens",
    "M-0002": "ABB",
    "M-0004": "Albrecht Jung",
    "M-0005": "Bticino",
    "M-0006": "Berker",
    "M-0007": "Busch-Jaeger Elektro",
    "M-0008": "GIRA Giersiepen",
    "M-0009": "Hager Electro",
    "M-000A": "Insta GmbH",
    "M-000B": "LEGRAND Appareillage électrique",
    "M-000C": "Merten",
    "M-000E": "ABB SpA-SACE Division",
    "M-0016": "Siedle &amp; Söhne",
    "M-0018": "Eberle",
    "M-0019": "GEWISS",
    "M-001B": "Albert Ackermann",
    "M-001C": "Schupa GmbH",
    "M-001D": "ABB SCHWEIZ",
    "M-001E": "Feller",
    "M-001F": "Glamox AS",
    "M-0020": "DEHN &amp; SÖHNE",
    "M-0021": "CRABTREE",
    "M-0022": "eVoKNX",
    "M-0024": "Paul Hochköpper",
    "M-0025": "Altenburger Electronic",
    "M-0029": "Grässlin",
    "M-002A": "Simon",
    "M-002C": "VIMAR",
    "M-002D": "Moeller Gebäudeautomation KG",
    "M-002E": "Eltako",
    "M-0031": "Bosch-Siemens Haushaltsgeräte",
    "M-0034": "RITTO GmbH&amp;Co.KG",
    "M-0035": "Power Controls",
    "M-0037": "ZUMTOBEL",
    "M-0039": "Phoenix Contact",
    "M-003D": "WAGO Kontakttechnik",
    "M-003E": "knXpresso",
    "M-0042": "Wieland Electric",
    "M-0043": "Hermann Kleinhuis",
    "M-0045": "Stiebel Eltron",
    "M-0047": "Tehalit",
    "M-0048": "Theben AG",
    "M-0049": "Wilhelm Rutenbeck",
    "M-004B": "Winkhaus",
    "M-004C": "Robert Bosch",
    "M-004E": "Somfy",
    "M-0050": "Woertz",
    "M-0051": "Viessmann Werke",
    "M-0052": "IMI Hydronic Engineering",
    "M-0053": "Joh. Vaillant",
    "M-0055": "AMP Deutschland",
    "M-0059": "Bosch Thermotechnik GmbH",
    "M-005A": "SEF - ECOTEC",
    "M-005C": "DORMA GmbH + Co. KG",
    "M-005D": "WindowMaster A/S",
    "M-005E": "Walther Werke",
    "M-005F": "ORAS",
    "M-0061": "Dätwyler",
    "M-0062": "Electrak",
    "M-0063": "Techem",
    "M-0064": "Schneider Electric Industries SAS",
    "M-0065": "WHD Wilhelm Huber + Söhne",
    "M-0066": "Bischoff Elektronik",
    "M-0068": "JEPAZ",
    "M-0069": "RTS Automation",
    "M-006A": "EIBMARKT GmbH",
    "M-006B": "WAREMA Renkhoff SE",
    "M-006C": "Eelectron",
    "M-006D": "Belden Wire &amp; Cable B.V.",
    "M-006E": "Becker-Antriebe GmbH",
    "M-006F": "J.Stehle+Söhne GmbH",
    "M-0070": "AGFEO",
    "M-0071": "Zennio",
    "M-0072": "TAPKO Technologies",
    "M-0073": "HDL",
    "M-0074": "Uponor",
    "M-0075": "se Lightmanagement AG",
    "M-0076": "Arcus-eds",
    "M-0077": "Intesis",
    "M-0078": "Herholdt Controls srl",
    "M-0079": "Niko-Zublin",
    "M-007A": "Durable Technologies",
    "M-007B": "Innoteam",
    "M-007C": "ise GmbH",
    "M-007D": "TEAM FOR TRONICS",
    "M-007E": "CIAT",
    "M-007F": "Remeha BV",
    "M-0080": "ESYLUX",
    "M-0081": "BASALTE",
    "M-0082": "Vestamatic",
    "M-0083": "MDT technologies",
    "M-0084": "Warendorfer Küchen GmbH",
    "M-0085": "Video-Star",
    "M-0086": "Sitek",
    "M-0087": "CONTROLtronic",
    "M-0088": "function Technology",
    "M-0089": "AMX",
    "M-008A": "ELDAT",
    "M-008B": "Panasonic",
    "M-008C": "Pulse Technologies",
    "M-008D": "Crestron",
    "M-008E": "STEINEL professional",
    "M-008F": "BILTON LED Lighting",
    "M-0090": "denro AG",
    "M-0091": "GePro",
    "M-0092": "preussen automation",
    "M-0093": "Zoppas Industries",
    "M-0094": "MACTECH",
    "M-0095": "TECHNO-TREND",
    "M-0096": "FS Cables",
    "M-0097": "Delta Dore",
    "M-0098": "Eissound",
    "M-0099": "Cisco",
    "M-009A": "Dinuy",
    "M-009B": "iKNiX",
    "M-009C": "Rademacher Geräte-Elektronik GmbH",
    "M-009D": "EGi Electroacustica General Iberica",
    "M-009E": "Bes – Ingenium",
    "M-009F": "ElabNET",
    "M-00A0": "Blumotix",
    "M-00A1": "Hunter Douglas",
    "M-00A2": "APRICUM",
    "M-00A3": "TIANSU Automation",
    "M-00A4": "Bubendorff",
    "M-00A5": "MBS GmbH",
    "M-00A6": "Enertex Bayern GmbH",
    "M-00A7": "BMS",
    "M-00A8": "Sinapsi",
    "M-00A9": "Embedded Systems SIA",
    "M-00AA": "KNX1",
    "M-00AB": "Tokka",
    "M-00AC": "NanoSense",
    "M-00AD": "PEAR Automation GmbH",
    "M-00AE": "DGA",
    "M-00AF": "Lutron",
    "M-00B0": "AIRZONE – ALTRA",
    "M-00B1": "Lithoss Design Switches",
    "M-00B2": "3ATEL",
    "M-00B3": "Philips Controls",
    "M-00B4": "VELUX A/S",
    "M-00B5": "LOYTEC",
    "M-00B6": "Ekinex S.p.A.",
    "M-00B7": "SIRLAN Technologies",
    "M-00B8": "ProKNX SAS",
    "M-00B9": "IT GmbH",
    "M-00BA": "RENSON",
    "M-00BB": "HEP Group",
    "M-00BC": "Balmart",
    "M-00BD": "GFS GmbH",
    "M-00BE": "Schenker Storen AG",
    "M-00BF": "Algodue Elettronica S.r.L.",
    "M-00C0": "ABB France",
    "M-00C1": "maintronic",
    "M-00C2": "Vantage",
    "M-00C3": "Foresis",
    "M-00C4": "Research &amp; Production Association SEM",
    "M-00C5": "Weinzierl Engineering GmbH",
    "M-00C6": "Möhlenhoff Wärmetechnik GmbH",
    "M-00C7": "PKC-GROUP Oyj",
    "M-00C8": "B.E.G.",
    "M-00C9": "Elsner Elektronik GmbH",
    "M-00CA": "Siemens Building Technologies (HK/China) Ltd.",
    "M-00CC": "Eutrac",
    "M-00CD": "Gustav Hensel GmbH &amp; Co. KG",
    "M-00CE": "GARO AB",
    "M-00CF": "Waldmann Lichttechnik",
    "M-00D0": "SCHÜCO",
    "M-00D1": "EMU",
    "M-00D2": "JNet Systems AG",
    "M-00D3": "Total Solution GmbH",
    "M-00D6": "O.Y.L. Electronics",
    "M-00D7": "Galax System",
    "M-00D8": "Disch",
    "M-00D9": "Aucoteam",
    "M-00DA": "Luxmate Controls",
    "M-00DB": "Danfoss",
    "M-00DC": "AST GmbH",
    "M-00DE": "WILA Leuchten",
    "M-00DF": "b+b Automations- und Steuerungstechnik",
    "M-00E1": "Lingg &amp; Janke",
    "M-00E3": "Sauter",
    "M-00E4": "SIMU",
    "M-00E8": "Theben HTS AG",
    "M-00E9": "Amann GmbH",
    "M-00EA": "BERG Energiekontrollsysteme GmbH",
    "M-00EB": "Hüppe Form Sonnenschutzsysteme GmbH",
    "M-00ED": "Oventrop KG",
    "M-00EE": "Griesser AG",
    "M-00EF": "IPAS GmbH",
    "M-00F0": "elero GmbH",
    "M-00F1": "Ardan Production and Industrial Controls Ltd.",
    "M-00F2": "Metec Meßtechnik GmbH",
    "M-00F4": "ELKA-Elektronik GmbH",
    "M-00F5": "ELEKTROANLAGEN D. NAGEL",
    "M-00F6": "Tridonic Bauelemente GmbH",
    "M-00F8": "Stengler Gesellschaft",
    "M-00F9": "Schneider Electric (MG)",
    "M-00FA": "KNX Association",
    "M-00FB": "VIVO",
    "M-00FC": "Hugo Müller GmbH &amp; Co KG",
    "M-00FD": "Siemens HVAC",
    "M-00FE": "APT",
    "M-0100": "HighDom",
    "M-0101": "Top Services",
    "M-0102": "ambiHome",
    "M-0103": "DATEC electronic AG",
    "M-0104": "ABUS Security-Center",
    "M-0105": "Lite-Puter",
    "M-0106": "Tantron Electronic",
    "M-0107": "Interra",
    "M-0108": "DKX Tech",
    "M-0109": "Viatron",
    "M-010A": "Nautibus",
    "M-010B": "ON Semiconductor",
    "M-010C": "Longchuang",
    "M-010D": "Air-On AG",
    "M-010E": "ib-company GmbH",
    "M-010F": "Sation Factory",
    "M-0110": "Agentilo GmbH",
    "M-0111": "Makel Elektrik",
    "M-0112": "Helios Ventilatoren",
    "M-0113": "Otto Solutions Pte Ltd",
    "M-0114": "Airmaster",
    "M-0115": "Vallox GmbH",
    "M-0116": "Dalitek",
    "M-0117": "ASIN",
    "M-0118": "Bridges Intelligence Technology Inc.",
    "M-0119": "ARBONIA",
    "M-011A": "KERMI",
    "M-011B": "PROLUX",
    "M-011C": "ClicHome",
    "M-011D": "COMMAX",
    "M-011E": "EAE",
    "M-011F": "Tense",
    "M-0120": "Seyoung Electronics",
    "M-0121": "Lifedomus",
    "M-0122": "EUROtronic Technology GmbH",
    "M-0123": "tci",
    "M-0124": "Rishun Electronic",
    "M-0125": "Zipato",
    "M-0126": "cm-security GmbH &amp; Co KG",
    "M-0127": "Qing Cables",
    "M-0128": "LABIO",
    "M-0129": "Coster Tecnologie Elettroniche S.p.A.",
    "M-012A": "E.G.E",
    "M-012B": "NETxAutomation",
    "M-012C": "tecalor",
    "M-012D": "Urmet Electronics (Huizhou) Ltd.",
    "M-012E": "Peiying Building Control",
    "M-012F": "BPT S.p.A. a Socio Unico",
    "M-0130": "Kanontec - KanonBUS",
    "M-0131": "ISER Tech",
    "M-0132": "Fineline",
    "M-0133": "CP Electronics Ltd",
    "M-0134": "Niko-Servodan A/S",
    "M-0135": "Simon",
    "M-0136": "GM modular pvt. Ltd.",
    "M-0137": "FU CHENG Intelligence",
    "M-0138": "NexKon",
    "M-0139": "FEEL s.r.l",
    "M-013A": "Not Assigned",
    "M-013B": "Shenzhen Fanhai Sanjiang Electronics Co., Ltd.",
    "M-013C": "Jiuzhou Greeble",
    "M-013D": "Aumüller Aumatic GmbH",
    "M-013E": "Etman Electric",
    "M-013F": "Black Nova",
    "M-0140": "ZidaTech AG",
    "M-0141": "IDGS bvba",
    "M-0142": "dakanimo",
    "M-0143": "Trebor Automation AB",
    "M-0144": "Satel sp. z o.o.",
    "M-0145": "Russound, Inc.",
    "M-0146": "Midea Heating &amp; Ventilating Equipment CO LTD",
    "M-0147": "Consorzio Terranuova",
    "M-0148": "Wolf Heiztechnik GmbH",
    "M-0149": "SONTEC",
    "M-014A": "Belcom Cables Ltd.",
    "M-014B": "Guangzhou SeaWin Electrical Technologies Co., Ltd.",
    "M-014C": "Acrel",
    "M-014D": "Franke Aquarotter GmbH",
    "M-014E": "Orion Systems",
    "M-014F": "Schrack Technik GmbH",
    "M-0150": "INSPRID",
    "M-0151": "Sunricher",
    "M-0152": "Menred automation system(shanghai) Co.,Ltd.",
    "M-0153": "Aurex",
    "M-0154": "Josef Barthelme GmbH &amp; Co. KG",
    "M-0155": "Architecture Numerique",
    "M-0156": "UP GROUP",
    "M-0157": "Teknos-Avinno",
    "M-0158": "Ningbo Dooya Mechanic &amp; Electronic Technology",
    "M-0159": "Thermokon Sensortechnik GmbH",
    "M-015A": "BELIMO Automation AG",
    "M-015B": "Zehnder Group International AG",
    "M-015C": "sks Kinkel Elektronik",
    "M-015D": "ECE Wurmitzer GmbH",
    "M-015E": "LARS",
    "M-015F": "URC",
    "M-0160": "LightControl",
    "M-0161": "ShenZhen YM",
    "M-0162": "MEAN WELL Enterprises Co. Ltd.",
    "M-0163": "OSix",
    "M-0164": "AYPRO Technology",
    "M-0165": "Hefei Ecolite Software",
    "M-0166": "Enno",
    "M-0167": "OHOSURE",
    "M-0168": "Garefowl",
    "M-0169": "GEZE",
    "M-016A": "LG Electronics Inc.",
    "M-016B": "SMC interiors",
    "M-016C": "Not Assigned",
    "M-016D": "SCS Cable",
    "M-016E": "Hoval",
    "M-016F": "CANST",
    "M-0170": "HangZhou Berlin",
    "M-0171": "EVN-Lichttechnik",
    "M-0172": "rutec",
    "M-0173": "Finder",
    "M-0174": "Fujitsu General Limited",
    "M-0175": "ZF Friedrichshafen AG",
    "M-0176": "Crealed",
    "M-0177": "Miles Magic Automation Private Limited",
    "M-0178": "E+",
    "M-0179": "Italcond",
    "M-017A": "SATION",
    "M-017B": "NewBest",
    "M-017C": "GDS DIGITAL SYSTEMS",
    "M-017D": "Iddero",
    "M-017E": "MBNLED",
    "M-017F": "VITRUM",
    "M-0180": "ekey biometric systems GmbH",
    "M-0181": "AMC",
    "M-0182": "TRILUX GmbH &amp; Co. KG",
    "M-0183": "WExcedo",
    "M-0184": "VEMER SPA",
    "M-0185": "Alexander Bürkle GmbH &amp; Co KG",
    "M-0186": "Citron",
    "M-0187": "Shenzhen HeGuang",
    "M-0188": "Not Assigned",
    "M-0189": "TRANE B.V.B.A",
    "M-018A": "CAREL",
    "M-018B": "Prolite Controls",
    "M-018C": "BOSMER",
    "M-018D": "EUCHIPS",
    "M-018E": "connect (Thinka connect)",
    "M-018F": "PEAKnx a DOGAWIST company ",
    "M-0190": "ACEMATIC",
    "M-0191": "ELAUSYS",
    "M-0192": "ITK Engineering AG",
    "M-0193": "INTEGRA METERING AG",
    "M-0194": "FMS Hospitality Pte Ltd",
    "M-0195": "Nuvo",
    "M-0196": "u::Lux GmbH",
    "M-0197": "Brumberg Leuchten",
    "M-0198": "Lime",
    "M-0199": "Great Empire International Group Co., Ltd.",
    "M-019A": "Kavoshpishro Asia",
    "M-019B": "V2 SpA",
    "M-019C": "Johnson Controls",
    "M-019D": "Arkud",
    "M-019E": "Iridium Ltd.",
    "M-019F": "bsmart",
    "M-01A0": "BAB TECHNOLOGIE GmbH",
    "M-01A1": "NICE Spa",
    "M-01A2": "Redfish Group Pty Ltd",
    "M-01A3": "SABIANA spa",
    "M-01A4": "Ubee Interactive Europe",
    "M-01A5": "Rexel",
    "M-01A6": "Ges Teknik A.S.",
    "M-01A7": "Ave S.p.A. ",
    "M-01A8": "Zhuhai Ltech Technology Co., Ltd. ",
    "M-01A9": "ARCOM",
    "M-01AA": "VIA Technologies, Inc.",
    "M-01AB": "FEELSMART.",
    "M-01AC": "SUPCON",
    "M-01AD": "MANIC",
    "M-01AE": "TDE GmbH",
    "M-01AF": "Nanjing Shufan Information technology Co.,Ltd.",
    "M-01B0": "EWTech",
    "M-01B1": "Kluger Automation GmbH",
    "M-01B2": "JoongAng Control",
    "M-01B3": "GreenControls Technology Sdn. Bhd.",
    "M-01B4": "IME S.p.a.",
    "M-01B5": "SiChuan HaoDing",
    "M-01B6": "Mindjaga Ltd.",
    "M-01B7": "RuiLi Smart Control",
    "M-01B8": "CODESYS GmbH",
    "M-01B9": "Moorgen Deutschland GmbH",
    "M-01BA": "CULLMANN TECH",
    "M-01BB": "Merck Window Technologies B.V. ",
    "M-01BC": "ABEGO",
    "M-01BD": "myGEKKO",
    "M-01BE": "Ergo3 Sarl",
    "M-01BF": "STmicroelectronics International N.V.",
    "M-01C0": "cjc systems",
    "M-01C1": "Sudoku",
    "M-01C3": "AZ e-lite Pte Ltd",
    "M-01C4": "Arlight",
    "M-01C5": "Grünbeck Wasseraufbereitung GmbH",
    "M-01C6": "Module Electronic",
    "M-01C7": "KOPLAT",
    "M-01C8": "Guangzhou Letour Life Technology Co., Ltd",
    "M-01C9": "ILEVIA",
    "M-01CA": "LN SYSTEMTEQ",
    "M-01CB": "Hisense SmartHome",
    "M-01CC": "Flink Automation System",
    "M-01CD": "xxter bv",
    "M-01CE": "lynxus technology",
    "M-01CF": "ROBOT S.A.",
    "M-01D0": "Shenzhen Atte Smart Life Co.,Ltd.",
    "M-01D1": "Noblesse",
    "M-01D2": "Advanced Devices",
    "M-01D3": "Atrina Building Automation Co. Ltd",
    "M-01D4": "Guangdong Daming Laffey electric Co., Ltd.",
    "M-01D5": "Westerstrand Urfabrik AB",
    "M-01D6": "Control4 Corporate",
    "M-01D7": "Ontrol",
    "M-01D8": "Starnet",
    "M-01D9": "BETA CAVI",
    "M-01DA": "EaseMore",
    "M-01DB": "Vivaldi srl",
    "M-01DC": "Gree Electric Appliances,Inc. of Zhuhai",
    "M-01DD": "HWISCON",
    "M-01DE": "Shanghai ELECON Intelligent Technology Co., Ltd.",
    "M-01DF": "Kampmann",
    "M-01E0": "Impolux GmbH / LEDIMAX",
    "M-01E1": "Evaux",
    "M-01E2": "Webro Cables &amp; Connectors Limited",
    "M-01E3": "Shanghai E-tech Solution",
    "M-01E4": "Guangzhou HOKO Electric Co.,Ltd.",
    "M-01E5": "LAMMIN HIGH TECH CO.,LTD",
    "M-01E6": "Shenzhen Merrytek Technology Co., Ltd",
    "M-01E7": "I-Luxus",
    "M-01E8": "Elmos Semiconductor AG",
    "M-01E9": "EmCom Technology Inc",
    "M-01EA": "project innovations GmbH",
    "M-01EB": "Itc",
    "M-01EC": "ABB LV Installation Materials Company Ltd, Beijing",
    "M-01ED": "Maico ",
    "M-01EF": "ELAN SRL",
    "M-01F0": "MinhHa Technology co.,Ltd",
    "M-01F1": "Zhejiang Tianjie Industrial CORP.",
    "M-01F2": "iAutomation Pty Limited",
    "M-01F3": "Extron",
    "M-01F4": "Freedompro",
    "M-01F5": "1Home",
    "M-01F6": "EOS Saunatechnik GmbH",
    "M-01F7": "KUSATEK GmbH",
    "M-01F8": "EisBär Scada",
    "M-01F9": "AUTOMATISMI BENINCA S.P.A.",
    "M-01FA": "Blendom",
    "M-01FB": "Madel Air Technical diffusion",
    "M-01FC": "NIKO",
    "M-01FD": "Bosch Rexroth AG",
    "M-0200": "C&amp;M Products",
    "M-0201": "Hörmann KG Verkaufsgesellschaft",
    "M-0202": "Shanghai Rajayasa co.,LTD",
    "M-0203": "SUZUKI",
    "M-0204": "Silent Gliss International Ltd.",
    "M-0205": "BEE Controls (ADGSC Group)",
    "M-0206": "xDTecGmbH",
    "M-0207": "OSRAM",
    "M-0208": "Lebenor",
    "M-0209": "automaneng",
    "M-020A": "Honeywell Automation Solution control(China)",
    "M-020B": "Hangzhou binthen Intelligence Technology Co.,Ltd",
    "M-020C": "ETA Heiztechnik",
    "M-020D": "DIVUS GmbH",
    "M-020E": "Nanjing Taijiesai Intelligent Technology Co. Ltd.",
    "M-020F": "Lunatone",
    "M-0210": "ZHEJIANG SCTECH BUILDING INTELLIGENT",
    "M-0211": "Foshan Qite Technology Co., Ltd.",
    "M-0212": "NOKE",
    "M-0213": "LANDCOM",
    "M-0214": "Stork AS",
    "M-0215": "Hangzhou Shendu Technology Co., Ltd.",
    "M-0216": "CoolAutomation",
    "M-0217": "Aprstern",
    "M-0218": "sonnen",
    "M-0219": "DNAKE",
    "M-021A": "Neuberger Gebäudeautomation GmbH",
    "M-021B": "Stiliger",
    "M-021C": "Berghof Automation GmbH",
    "M-021D": "Total Automation and controls GmbH",
    "M-021E": "dovit",
    "M-021F": "Instalighting GmbH",
    "M-0220": "UNI-TEC",
    "M-0221": "CasaTunes",
    "M-0222": "EMT",
    "M-0223": "Senfficient",
    "M-0224": "Aurolite electrical panyu guangzhou limited",
    "M-0225": "ABB Xiamen Smart Technology Co., Ltd.",
    "M-0226": "Samson Electric Wire",
    "M-0227": "T-Touching",
    "M-0228": "Core Smart Home",
    "M-0229": "GreenConnect Solutions SA",
    "M-022A": "ELETTRONICA CONDUTTORI",
    "M-022B": "MKFC",
    "M-022C": "Automation+",
    "M-022D": "blue and red",
    "M-022E": "frogblue",
    "M-022F": "SAVESOR",
    "M-0230": "App Tech",
    "M-0231": "sensortec AG",
    "M-0232": "nysa technology &amp; solutions",
    "M-0233": "FARADITE",
    "M-0234": "Optimus",
    "M-0235": "KTS s.r.l.",
    "M-0236": "Ramcro SPA",
    "M-0237": "Wuhan WiseCreate Universe Technology Co., Ltd",
    "M-0238": "BEMI Smart Home Ltd",
    "M-0239": "Ardomus",
    "M-023A": "ChangXing",
    "M-023B": "E-Controls",
    "M-023C": "AIB Technology",
    "M-023D": "NVC",
    "M-023E": "Kbox",
    "M-023F": "CNS",
    "M-0240": "Tyba",
    "M-0241": "Atrel",
    "M-0242": "Simon Electric (China) Co., LTD",
    "M-0243": "Kordz Group",
    "M-0244": "ND Electric",
    "M-0245": "Controlium",
    "M-0246": "FAMO GmbH &amp; Co. KG",
    "M-0247": "CDN Smart",
    "M-0248": "Heston",
    "M-0249": "ESLA CONEXIONES S.L.",
    "M-024A": "Weishaupt",
    "M-024B": "ASTRUM TECHNOLOGY",
    "M-024C": "WUERTH ELEKTRONIK STELVIO KONTEK S.p.A.",
    "M-024D": "NANOTECO corporation",
    "M-024E": "Nietian",
    "M-024F": "Sumsir",
    "M-0250": "ORBIS TECNOLOGIA ELECTRICA SA",
    "M-0251": "Nanjing Zhongyi IoT Technology Co., Ltd.",
    "M-0252": "Anlips",
    "M-0253": "GUANGDONG PAK CORPORATION CO., LTD",
    "M-0254": "BVK Technology",
    "M-0255": "Solomio srl",
    "M-0256": "Domotica Labs",
    "M-0257": "NVC International",
    "M-0258": "BA",
    "M-0259": "Iris Ceramica Group",
    "M-025A": "Wireeo",
    "M-025B": "nvclighting",
    "M-025C": "Jinan Tian Da Sheng Information Technology Co.",
    "M-025D": "Armiti trading",
    "M-025E": "ELEK",
    "M-025F": "Accordia sa",
    "M-0260": "OURICAN",
    "M-0261": "INLIWOSE",
    "M-0262": "Bosch (Shanghai) Smart Life Technology Ltd.",
    "M-0263": "SHK KNX",
    "M-0264": "Ampio",
    "M-0265": "Mingxing Wisdom",
    "M-0266": "ALTEN SW GmbH",
    "M-0267": "V.Y.C.srl",
    "M-0268": "TERMINUS GROUP",
    "M-0269": "Wonderful City Technology",
    "M-026A": "QbicTechnology",
    "M-026B": "Embedded Automation Equipment (Shanghai) Limited",
    "M-026C": "onework",
    "M-026D": "PL LINK",
    "M-026E": "Fasel GmbH Elektronik",
    "M-026F": "GoldenHome Smart",
    "M-0270": "Goldmedal",
    "M-0271": "Can'nX",
    "M-0273": "EGI - Earth Goodness",
    "M-0274": "Viega GmbH &amp; Co. KG",
    "M-0275": "Fredon Digital Buildings",
    "M-0276": "Helukabel (Thailand) Co.,Ltd.",
    "M-0277": "ACE Technology",
    "M-0278": "MEX Electric Technology (Shanghai) Co., Ltd",
    "M-0279": "SUMAMO",
    "M-027A": "SVIT",
    "M-027B": "tecget",
    "M-027C": "Xeropoint",
    "M-027D": "Honeywell Building Technologies",
    "M-027E": "ComfortClick",
    "M-027F": "DORBAS ELECTRIC",
    "M-0280": "REMKO GmbH &amp; Co. KG",
    "M-0281": "Shenzhen Congxun Intelligent Technology Co., LTD",
    "M-0282": "ANDAS",
    "M-0283": "Hefei Chuang Yue Intelligent Technology Co.,LTD",
    "M-0284": "Larfe",
    "M-ABB2": "ABB - reserved",
    "M-ABB7": "Busch-Jaeger Elektro - reserved",
}
